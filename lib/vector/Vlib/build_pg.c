/*!
   \file lib/vector/Vlib/build_pg.c

   \brief Vector library - Building topology for PostGIS layers

   Higher level functions for reading/writing/manipulating vectors.

   Line offset (simple features only) is
   - centroids   : FID
   - other types : index of the first record (which is FID) in offset array.

   (C) 2012-2013 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Martin Landa <landa.martin gmail.com>
 */

#include <grass/vector.h>
#include <grass/glocale.h>

#include "local_proto.h"

#ifdef HAVE_POSTGRES
#include "pg_local_proto.h"

static int build_topo(struct Map_info *, int);
static int build_topogeom_stmt(const struct Format_info_pg *, int, int, int,
                               char *);
static int save_map_bbox(const struct Format_info_pg *,
                         const struct bound_box *);
static int create_topo_grass(const struct Format_info_pg *);
static int has_topo_grass(const struct Format_info_pg *);
static int write_nodes(const struct Plus_head *, const struct Format_info_pg *);
static int write_lines(const struct Plus_head *, const struct Format_info_pg *);
static int write_areas(const struct Plus_head *, const struct Format_info_pg *);
static int write_isles(const struct Plus_head *, const struct Format_info_pg *);
static void build_stmt_id(const void *, int, int, const struct Plus_head *,
                          char **, size_t *);
static int create_simple_feature_from_topo(struct Map_info *);
#define NOPG_UNUSED
#else
#define NOPG_UNUSED UNUSED
#endif

/*!
   \brief Build topology for PostGIS layer

   Build levels:
   - GV_BUILD_NONE
   - GV_BUILD_BASE
   - GV_BUILD_ATTACH_ISLES
   - GV_BUILD_CENTROIDS
   - GV_BUILD_ALL

   \param Map pointer to Map_info structure
   \param build build level

   \return 1 on success
   \return 0 on error
 */
int Vect_build_pg(struct Map_info *Map NOPG_UNUSED, int build NOPG_UNUSED)
{
#ifdef HAVE_POSTGRES
    struct Plus_head *plus;
    struct Format_info_pg *pg_info;

    plus = &(Map->plus);
    pg_info = &(Map->fInfo.pg);

    G_debug(1, "Vect_build_pg(): db='%s' table='%s', build=%d",
            pg_info->db_name, pg_info->table_name, build);

    /* commit transaction block (update mode only) */
    if (pg_info->inTransaction &&
        Vect__execute_pg(pg_info->conn, "COMMIT") == -1)
        return 0;
    pg_info->inTransaction = FALSE;

    if (pg_info->feature_type == SF_GEOMETRY)
        return 1;

    if (build == plus->built)
        return 1; /* do nothing */

    /* TODO move this init to better place (Vect_open_ ?), because in
       theory build may be reused on level2 */
    if (!pg_info->toposchema_name && build >= plus->built &&
        build > GV_BUILD_BASE) {
        G_free(pg_info->offset.array);
        G_zero(&(pg_info->offset), sizeof(struct Format_info_offset));
    }

    if (!pg_info->conn) {
        G_warning(_("No DB connection"));
        return 0;
    }

    if (!pg_info->fid_column && !pg_info->toposchema_name) {
        G_warning(_("Feature table <%s> has no primary key defined"),
                  pg_info->table_name);
        G_warning(_("Random read is not supported for this layer. "
                    "Unable to build topology."));
        return 0;
    }

    if (build > GV_BUILD_NONE) {
        G_message(_("Using external data format '%s' (feature type '%s')"),
                  Vect_get_finfo_format_info(Map),
                  Vect_get_finfo_geometry_type(Map));
        if (!pg_info->toposchema_name)
            G_message(_("Building pseudo-topology over simple features..."));
        else
            G_message(
                _("Building topology from PostGIS topology schema <%s>..."),
                pg_info->toposchema_name);
    }

    if (!pg_info->toposchema_name) /* pseudo-topology for simple features */
        return Vect__build_sfa(Map, build);

    /* PostGIS Topology */
    return build_topo(Map, build);
#else
    G_fatal_error(_("GRASS is not compiled with PostgreSQL support"));
    return 0;
#endif
}

#ifdef HAVE_POSTGRES
/*!
   \brief Build from PostGIS topology schema

   \todo Attach isles

   \param Map pointer to Map_info struct
   \param build build level

   \return 1 on success
   \return 0 on error
 */
int build_topo(struct Map_info *Map, int build)
{
    int line, type, s, n_nodes = 0;
    int area, nareas, isle, nisles;
    int face[2];
    char stmt[DB_SQL_MAX];
    char *def_file;

    struct Plus_head *plus;
    struct Format_info_pg *pg_info;

    struct P_line *Line;
    struct P_area *Area;
    struct P_topo_b *topo_b;
    struct P_isle *Isle;

    plus = &(Map->plus);
    pg_info = &(Map->fInfo.pg);

    /* check if upgrade or downgrade */
    if (build < plus->built) {
        /* -> downgrade */
        Vect__build_downgrade(Map, build);
        return 1;
    }
    /*     -> upgrade */

    if (build < GV_BUILD_BASE)
        return 1; /* nothing to print */

    /* cache features to speed-up random access (when attaching isles
       to areas) */
    if (build >= GV_BUILD_BASE) {
        /* clean-up GRASS topology tables in DB */
        if (!pg_info->topo_geo_only)
            Vect__clean_grass_db_topo(&(Map->fInfo.pg));

        if (Map->mode == GV_MODE_RW && pg_info->cache.lines_num > 0) {

            /* read line cache from scratch when map is open in update
             * mode, before building native topology read nodes from
             * PostGIS Topology */

            /* clean-up spatial a category indices */
            dig_free_plus(&(Map->plus));
            dig_init_plus(&(Map->plus));
            plus->Spidx_new = TRUE;
            plus->update_cidx = TRUE;

            /* reset cache for reading features */
            Vect__free_cache(&(pg_info->cache));
        }
    }

    if (plus->built >= GV_BUILD_BASE && pg_info->cache.lines_num < 1) {
        /* features are not cached, build from scratch */
        Vect_build_partial(Map, GV_BUILD_NONE);
    }

    if (plus->built < GV_BUILD_BASE) {
        /* force loading nodes from DB to get up-to-date node
         * offsets, see write_nodes() for details */
        Vect__free_offset(&(pg_info->offset));

        pg_info->cache.ctype = CACHE_FEATURE; /* do not cache nodes */
        n_nodes = Map->plus.n_nodes = Vect__load_map_nodes_pg(Map, TRUE);
        Vect__free_cache(&(pg_info->cache));
    }

    if (build > GV_BUILD_BASE)
        pg_info->cache.ctype = CACHE_MAP; /* cache all features */

    /* update TopoGeometry based on GRASS-like topology */
    Vect_build_nat(Map, build);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))

    if (n_nodes != Map->plus.n_nodes)
        G_warning(
            _("Inconsistency in topology: number of nodes %d (should be %d)"),
            Map->plus.n_nodes, n_nodes);
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))

    if (n_nodes != Map->plus.n_nodes)
        G_warning(
            _("Inconsistency in topology: number of nodes %d (should be %d)"),
            Map->plus.n_nodes, n_nodes);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))

    if (n_nodes != Map->plus.n_nodes)
        G_warning(
            _("Inconsistency in topology: number of nodes %d (should be %d)"),
            Map->plus.n_nodes, n_nodes);
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    if (n_nodes != Map->plus.n_nodes)
        G_warning(
            _("Inconsistency in topology: number of nodes %d (should be %d)"),
            Map->plus.n_nodes, n_nodes);
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))

    if (n_nodes != Map->plus.n_nodes)
        G_warning(
            _("Inconsistency in topology: number of nodes %d (should be %d)"),
            Map->plus.n_nodes, n_nodes);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))

    if (n_nodes != Map->plus.n_nodes)
        G_warning(
            _("Inconsistency in topology: number of nodes %d (should be %d)"),
            Map->plus.n_nodes, n_nodes);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))

    if (n_nodes != Map->plus.n_nodes)
        G_warning(
            _("Inconsistency in topology: number of nodes %d (should be %d)"),
            Map->plus.n_nodes, n_nodes);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))

    if (n_nodes != Map->plus.n_nodes)
        G_warning(
            _("Inconsistency in topology: number of nodes %d (should be %d)"),
            Map->plus.n_nodes, n_nodes);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    if (n_nodes != Map->plus.n_nodes)
        G_warning(
            _("Inconsistency in topology: number of nodes %d (should be %d)"),
            Map->plus.n_nodes, n_nodes);

    /* store map bounding box in DB */
    save_map_bbox(pg_info, &(plus->box));

    /* begin transaction */
    if (Vect__execute_pg(pg_info->conn, "BEGIN"))
        return 0;

    Vect__execute_pg(pg_info->conn, "SET CONSTRAINTS ALL DEFERRED");

    /* write full node topo info to DB if requested */
    if (!pg_info->topo_geo_only) {
        write_nodes(plus, pg_info);
        write_lines(plus, pg_info);
    }

    /* update faces from GRASS Topology */
    if (build >= GV_BUILD_AREAS) {
        /* do clean up (1-3)
           insert new faces (4)
           update edges (5)
         */

        G_message(_("Cleaning-up topology schema..."));
        /* 1) reset centroids to '0' (universal face) */
        sprintf(stmt,
                "UPDATE \"%s\".node SET containing_face = 0 WHERE "
                "containing_face IS NOT NULL",
                pg_info->toposchema_name);
        G_debug(2, "SQL: %s", stmt);
        if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
            Vect__execute_pg(pg_info->conn, "ROLLBACK");
            return 0;
        }

        /* 2) reset left|right edges */
        sprintf(stmt,
                "UPDATE \"%s\".edge_data SET left_face = 0, right_face = 0",
                pg_info->toposchema_name);
        G_debug(2, "SQL: %s", stmt);
        if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
            Vect__execute_pg(pg_info->conn, "ROLLBACK");
            return 0;
        }

        /* 3) delete faces (areas/isles) */
        sprintf(stmt,
                "DELETE FROM \"%s\".face WHERE "
                "face_id != 0",
                pg_info->toposchema_name);
        G_debug(2, "SQL: %s", stmt);
        if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
            Vect__execute_pg(pg_info->conn, "ROLLBACK");
            return 0;
        }
        if (!pg_info->topo_geo_only) {
            sprintf(stmt, "DELETE FROM \"%s\".%s", pg_info->toposchema_name,
                    TOPO_TABLE_AREA);
            G_debug(2, "SQL: %s", stmt);
            if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
                Vect__execute_pg(pg_info->conn, "ROLLBACK");
                return 0;
            }

            sprintf(stmt, "DELETE FROM \"%s\".%s", pg_info->toposchema_name,
                    TOPO_TABLE_ISLE);
            G_debug(2, "SQL: %s", stmt);
            if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
                Vect__execute_pg(pg_info->conn, "ROLLBACK");
                return 0;
            }
        }

        /* 4) insert faces & update nodes (containing_face) based on
         * GRASS topology */
        G_message(_("Updating faces..."));
        nareas = Vect_get_num_areas(Map);
        for (area = 1; area <= nareas; area++) {
            G_percent(area, nareas, 5);
            if (0 == Vect__insert_face_pg(Map, area)) {
                Vect__execute_pg(pg_info->conn, "ROLLBACK");
                return 0;
            }

            if (build < GV_BUILD_CENTROIDS)
                continue;

            /* update centroids (node -> containing_face) */
            Area = plus->Area[area];
            if (Area->centroid < 1) {
                G_debug(3, "Area %d without centroid, skipped", area);
                continue;
            }

            Line = plus->Line[Area->centroid];
            sprintf(stmt,
                    "UPDATE \"%s\".node SET "
                    "containing_face = %d WHERE node_id = %d",
                    pg_info->toposchema_name, area, (int)Line->offset);
            G_debug(2, "SQL: %s", stmt);

            if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
                Vect__execute_pg(pg_info->conn, "ROLLBACK");
                return 0;
            }
        }

        /* 5) update edges (left and right face) */
        G_message(_("Updating edges..."));
        for (line = 1; line <= plus->n_lines; line++) {
            G_percent(line, plus->n_lines, 5);
            type = Vect_read_line(Map, NULL, NULL, line);
            if (type != GV_BOUNDARY)
                continue;

            Line = Map->plus.Line[line];
            if (!Line) {
                G_warning(_("Inconsistency in topology detected. "
                            "Dead line found."));
                return 0;
            }

            topo_b = (struct P_topo_b *)Line->topo;

            for (s = 0; s < 2; s++) { /* for both sides */
                face[s] = s == 0 ? topo_b->left : topo_b->right;
                if (face[s] < 0) {
                    /* isle */
                    Isle = plus->Isle[abs(face[s])];
                    face[s] = Isle->area;
                }
            }
            G_debug(3, "update edge %d: left_face = %d, right_face = %d",
                    (int)Line->offset, face[0], face[1]);

            sprintf(stmt,
                    "UPDATE \"%s\".edge_data SET "
                    "left_face = %d, right_face = %d "
                    "WHERE edge_id = %d",
                    pg_info->toposchema_name, face[0], face[1],
                    (int)Line->offset);

            if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
                Vect__execute_pg(pg_info->conn, "ROLLBACK");
                return 0;
            }
        }

        /* write full area topo info to DB if requested */
        if (!pg_info->topo_geo_only) {
            write_areas(plus, pg_info);
        }
    } /* build >= GV_BUILD_AREAS */

    if (build >= GV_BUILD_ATTACH_ISLES) {
        /* insert isles as faces with negative face_id */
        nisles = Vect_get_num_islands(Map);
        for (isle = 1; isle <= nisles; isle++) {
            Isle = plus->Isle[isle];
            Vect__insert_face_pg(Map, -isle);
        }

        /* write full isles topo info to DB if requested */
        if (!pg_info->topo_geo_only) {
            write_isles(plus, pg_info);
        }
    } /* build >= GV_BUILD_ISLES */

    if (pg_info->feature_type == SF_POLYGON) {
        int centroid;

        struct P_line *Line;

        G_message(_("Updating TopoGeometry data..."));
        for (area = 1; area <= plus->n_areas; area++) {
            G_percent(area, plus->n_areas, 5);
            centroid = Vect_get_area_centroid(Map, area);
            if (centroid < 1)
                continue;

            Line = plus->Line[centroid];
            if (!Line)
                continue;

            /* update topogeometry object: centroid -> face */
            if (build_topogeom_stmt(pg_info, GV_CENTROID, area,
                                    (int)Line->offset, stmt) &&
                Vect__execute_pg(pg_info->conn, stmt) == -1) {
                Vect__execute_pg(pg_info->conn, "ROLLBACK");
                return 0;
            }

            Vect__define_topo_relation(pg_info, area, area);
        }
    }

    if (Vect__execute_pg(pg_info->conn, "COMMIT") == -1)
        return 0;

    /* check if we want to create simple features from topogeometry
       data */
    def_file = getenv("GRASS_VECTOR_PGFILE");

    if (G_find_file2("", def_file ? def_file : "PG", G_mapset())) {
        FILE *fp;
        const char *p;

        struct Key_Value *key_val;

        fp = G_fopen_old("", def_file ? def_file : "PG", G_mapset());
        if (!fp) {
            G_fatal_error(_("Unable to open PG file"));
        }
        key_val = G_fread_key_value(fp);
        fclose(fp);

        /* build simple features from topogeometry data */
        p = G_find_key_value("simple_feature", key_val);
        if (p && G_strcasecmp(p, "yes") == 0) {
            if (build > GV_BUILD_BASE)
                Map->level = LEVEL_2; /* force level to avoid errors */

            if (create_simple_feature_from_topo(Map) != 0)
                return 0;
        }

        G_free_key_value(key_val);
    }

    return 1;
}

/*!
   \brief Build UPDATE statement for topo geometry element stored in
   feature table

   \param pg_info so pointer to Format_info_pg
   \param type feature type (GV_POINT, ...)
   \param topo_id topology element id
   \param fid feature id
   \param[out] stmt string buffer

   \return 1 on success
   \return 0 on failure
 */
int build_topogeom_stmt(const struct Format_info_pg *pg_info, int type,
                        int topo_id, int fid, char *stmt)
{
    int topogeom_type;

    switch (type) {
    case GV_POINT:
        topogeom_type = 1;
        break;
    case GV_LINE:
    case GV_BOUNDARY:
        topogeom_type = 2;
        break;
    case GV_CENTROID:
        topogeom_type = 3;
        break;
    default:
        G_warning(_("Unsupported topo geometry type %d"), type);
        return 0;
    }

    sprintf(stmt,
            "UPDATE \"%s\".\"%s\" SET %s = "
            "'(%d, 1, %d, %d)'::topology.TopoGeometry "
            "WHERE (%s).id = %d",
            pg_info->schema_name, pg_info->table_name, pg_info->topogeom_column,
            pg_info->toposchema_id, topo_id, topogeom_type,
            pg_info->topogeom_column, fid);

    return 1;
}

/*!
   \brief Store map bounding box in DB head table

   \param pg_info pointer to Format_info_pg struct
   \param box pointer to bounding box

   \return 1 on success
   \return 0 on failure
 */
int save_map_bbox(const struct Format_info_pg *pg_info,
                  const struct bound_box *box)
{
    char stmt[DB_SQL_MAX];

    /* create if not exists */
    if (create_topo_grass(pg_info) == -1) {
        G_warning(_("Unable to create <%s.%s>"), TOPO_SCHEMA, TOPO_TABLE);
        return 0;
    }

    /* update bbox */
    if (has_topo_grass(pg_info)) {
        /* -> update */
        sprintf(stmt,
                "UPDATE \"%s\".\"%s\" SET %s = "
                "'BOX3D(%.12f %.12f %.12f, %.12f %.12f %.12f)'::box3d WHERE %s "
                "= %d",
                TOPO_SCHEMA, TOPO_TABLE, TOPO_BBOX, box->W, box->S, box->B,
                box->E, box->N, box->T, TOPO_ID, pg_info->toposchema_id);
    }
    else {
        /* -> insert */
        sprintf(
            stmt,
            "INSERT INTO \"%s\".\"%s\" (%s, %s) "
            "VALUES(%d, 'BOX3D(%.12f %.12f %.12f, %.12f %.12f %.12f)'::box3d)",
            TOPO_SCHEMA, TOPO_TABLE, TOPO_ID, TOPO_BBOX, pg_info->toposchema_id,
            box->W, box->S, box->B, box->E, box->N, box->T);
    }

    if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
        return -1;
    }

    return 1;
}

/*!
   \brief Creates 'topology.grass' table if not exists

   \return 0 table already exists
   \return 1 table successfully added
   \return -1 on error
 */
int create_topo_grass(const struct Format_info_pg *pg_info)
{
    char stmt[DB_SQL_MAX];

    PGresult *result;

    /* check if table exists */
    sprintf(stmt,
            "SELECT COUNT(*) FROM information_schema.tables "
            "WHERE table_schema = '%s' AND table_name = '%s'",
            TOPO_SCHEMA, TOPO_TABLE);
    result = PQexec(pg_info->conn, stmt);
    if (!result || PQresultStatus(result) != PGRES_TUPLES_OK) {
        PQclear(result);
        return -1;
    }

    if (atoi(PQgetvalue(result, 0, 0)) == 1) {
        /* table already exists */
        PQclear(result);
        return 1;
    }
    PQclear(result);

    G_debug(1, "<%s.%s> created", TOPO_SCHEMA, TOPO_TABLE);

    /* create table */
    sprintf(stmt, "CREATE TABLE \"%s\".\"%s\" (%s INTEGER, %s box3d)",
            TOPO_SCHEMA, TOPO_TABLE, TOPO_ID, TOPO_BBOX);
    if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
        return -1;
    }
    /* add primary key */
    sprintf(stmt, "ALTER TABLE \"%s\".\"%s\" ADD PRIMARY KEY (%s)", TOPO_SCHEMA,
            TOPO_TABLE, TOPO_ID);
    if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
        return -1;
    }

    /* add constraint */
    sprintf(
        stmt,
        "ALTER TABLE \"%s\".\"%s\" ADD CONSTRAINT \"%s_%s_fkey\" "
        "FOREIGN KEY (%s) REFERENCES topology.topology(id) ON DELETE CASCADE",
        TOPO_SCHEMA, TOPO_TABLE, TOPO_TABLE, TOPO_ID, TOPO_ID);
    if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
        return -1;
    }

    return 1;
}

/*!
   \brief Check if 'topology_id' exists in 'topology.grass'

   \param pg_info pointer to Format_info_pg struct

   \return TRUE if exists
   \return FALSE otherwise
   \return -1 on error
 */
int has_topo_grass(const struct Format_info_pg *pg_info)
{
    int has_topo;
    char stmt[DB_SQL_MAX];

    PGresult *result;

    sprintf(stmt,
            "SELECT COUNT(*) FROM \"%s\".\"%s\" "
            "WHERE %s = %d",
            TOPO_SCHEMA, TOPO_TABLE, TOPO_ID, pg_info->toposchema_id);
    result = PQexec(pg_info->conn, stmt);
    if (!result || PQresultStatus(result) != PGRES_TUPLES_OK) {
        PQclear(result);
        return -1;
    }

    has_topo = FALSE;
    if (atoi(PQgetvalue(result, 0, 0)) == 1) {
        /* table already exists */
        has_topo = TRUE;
    }
    PQclear(result);

    return has_topo;
}

/*!
   \brief Insert node into 'node_grass' table

   Writes (see P_node struct):
   - lines
   - angles

   Already stored in Topo-Geo:
   - x,y,z (geom)

   \param plus pointer to Plus_head struct
   \param pg_info pointer to Format_info_pg struct

   \return 0 on success
   \return -1 on error
 */
int write_nodes(const struct Plus_head *plus,
                const struct Format_info_pg *pg_info)
{
    int i, node_id;
    size_t stmt_lines_size, stmt_angles_size, stmt_size;
    char *stmt_lines, *stmt_angles, *stmt;

    const struct P_node *Node;
    const struct Format_info_offset *offset;

    offset = &(pg_info->offset);

    if (offset->array_num < 1) /* nothing to write */
        return 0;

    if (plus->n_nodes != offset->array_num) {
        G_warning(_("Unable to write nodes, offset array mismatch"));
        return -1;
    }

    stmt_size = 2 * DB_SQL_MAX + 512;
    stmt = (char *)G_malloc(stmt_size);

    stmt_lines = stmt_angles = NULL;
    for (i = 1; i <= plus->n_nodes; i++) {
        Node = plus->Node[i];
        if (!Node)
            continue; /* should not happen */

        node_id = offset->array[i - 1];

        /* 'lines' array */
        build_stmt_id(Node->lines, Node->n_lines, TRUE, plus, &stmt_lines,
                      &stmt_lines_size);
        /* 'angle' array */
        build_stmt_id(Node->angles, Node->n_lines, FALSE, NULL, &stmt_angles,
                      &stmt_angles_size);

        /* build SQL statement to add new node into 'node_grass' */
        if (stmt_lines_size + stmt_angles_size + 512 > stmt_size) {
            stmt_size = stmt_lines_size + stmt_angles_size + 512;
            stmt = (char *)G_realloc(stmt, stmt_size);
        }
        sprintf(stmt,
                "INSERT INTO \"%s\".%s VALUES ("
                "%d, '{%s}', '{%s}')",
                pg_info->toposchema_name, TOPO_TABLE_NODE, node_id, stmt_lines,
                stmt_angles);
        if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
            G_warning(_("Unable to write nodes"));
            return -1;
        }
    }

    G_free(stmt_lines);
    G_free(stmt_angles);
    G_free(stmt);

    return 0;
}

/*!
   \brief Insert lines into 'line_grass' table

   Writes (see P_line struct) - only for boundaries:
   - left, right area

   Already stored in Topo-Geo:
   - edge_id, left_face, right_face

   \param plus pointer to Plus_head struct
   \param pg_info pointer to Format_info_pg struct

   \return 0 on success
   \return -1 on error
 */
int write_lines(const struct Plus_head *plus,
                const struct Format_info_pg *pg_info)
{
    int i, row, offset;
    char stmt[DB_SQL_MAX];

    const struct P_line *Line;
    const struct P_topo_b *topo;

    PGresult *res;

    sprintf(stmt,
            "SELECT edge_id FROM \"%s\".edge_data WHERE "
            "left_face != 0 OR right_face != 0 ORDER BY edge_id",
            pg_info->toposchema_name);
    G_debug(2, "SQL: %s", stmt);
    res = PQexec(pg_info->conn, stmt);
    if (!res || PQresultStatus(res) != PGRES_TUPLES_OK ||
        (PQntuples(res) > 0 && PQntuples(res) != plus->n_blines)) {
        G_warning(_("Inconsistency in topology: number of "
                    "boundaries %d (should be %d)"),
                  PQntuples(res), plus->n_blines);
        if (res)
            PQclear(res);
        return -1;
    }

    for (row = 0, i = 1; i <= plus->n_lines; i++) {
        Line = plus->Line[i];
        if (!Line || Line->type != GV_BOUNDARY)
            continue;

        if (Line->offset == 0L)
            offset = atoi(PQgetvalue(res, row++, 0));
        else
            offset = (int)Line->offset;

        topo = (struct P_topo_b *)Line->topo;
        sprintf(stmt,
                "INSERT INTO \"%s\".%s VALUES ("
                "%d, %d, %d)",
                pg_info->toposchema_name, TOPO_TABLE_LINE, offset, topo->left,
                topo->right);
        if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
            G_warning(_("Unable to write lines"));
            return -1;
        }
    }

    return 0;
}

/*!
   \brief Insert area into 'area_grass' table

   Writes (see P_area struct):
   - lines
   - centroid
   - isles

   \param plus pointer to Plus_head struct
   \param pg_info pointer to Format_info_pg struct

   \return 0 on success
   \return -1 on error
 */
int write_areas(const struct Plus_head *plus,
                const struct Format_info_pg *pg_info)
{
    int area, centroid;
    size_t stmt_lines_size, stmt_isles_size, stmt_size;
    char *stmt_lines, *stmt_isles, *stmt;

    const struct P_line *Line;
    const struct P_area *Area;

    stmt_size = 2 * DB_SQL_MAX + 512;
    stmt = (char *)G_malloc(stmt_size);

    stmt_lines = stmt_isles = NULL;
    for (area = 1; area <= plus->n_areas; area++) {
        Area = plus->Area[area];
        if (!Area) {
            G_debug(3, "Area %d skipped (dead)", area);
            continue; /* should not happen */
        }

        /* 'lines' array */
        build_stmt_id(Area->lines, Area->n_lines, TRUE, NULL, &stmt_lines,
                      &stmt_lines_size);
        /* 'isles' array */
        build_stmt_id(Area->isles, Area->n_isles, TRUE, NULL, &stmt_isles,
                      &stmt_isles_size);

        if (Area->centroid != 0) {
            Line = plus->Line[Area->centroid];
            if (!Line) {
                G_warning(_("Topology for centroid %d not available. Area %d "
                            "skipped"),
                          Area->centroid, area);
                continue;
            }
            centroid = (int)Line->offset;
        }
        else {
            centroid = 0;
        }

        /* build SQL statement to add new node into 'node_grass' */
        if (stmt_lines_size + stmt_isles_size + 512 > stmt_size) {
            stmt_size = stmt_lines_size + stmt_isles_size + 512;
            stmt = (char *)G_realloc(stmt, stmt_size);
        }
        sprintf(stmt,
                "INSERT INTO \"%s\".%s VALUES ("
                "%d, '{%s}', %d, '{%s}')",
                pg_info->toposchema_name, TOPO_TABLE_AREA, area, stmt_lines,
                centroid, stmt_isles);
        if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
            return -1;
        }
    }

    G_free(stmt_lines);
    G_free(stmt_isles);
    G_free(stmt);

    return 0;
}

/*!
   \brief Insert isle into 'isle_grass' table

   Writes (see P_isle struct):
   - lines
   - area

   \param plus pointer to Plus_head struct
   \param pg_info pointer to Format_info_pg struct

   \return 0 on success
   \return -1 on error
 */
int write_isles(const struct Plus_head *plus,
                const struct Format_info_pg *pg_info)
{
    int isle;
    size_t stmt_lines_size, stmt_size;
    char *stmt_lines, *stmt;

    const struct P_isle *Isle;

    stmt_size = DB_SQL_MAX + 512;
    stmt = (char *)G_malloc(stmt_size);

    stmt_lines = NULL;
    for (isle = 1; isle <= plus->n_isles; isle++) {
        Isle = plus->Isle[isle];
        if (!Isle)
            continue; /* should not happen */

        /* 'lines' array */
        build_stmt_id(Isle->lines, Isle->n_lines, TRUE, NULL, &stmt_lines,
                      &stmt_lines_size);

        /* build SQL statement to add new node into 'node_grass' */
        if (stmt_lines_size + 512 > stmt_size) {
            stmt_size = stmt_lines_size + 512;
            stmt = (char *)G_realloc(stmt, stmt_size);
        }
        sprintf(stmt,
                "INSERT INTO \"%s\".%s VALUES ("
                "%d, '{%s}', %d)",
                pg_info->toposchema_name, TOPO_TABLE_ISLE, isle, stmt_lines,
                Isle->area);
        if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
            return -1;
        }
    }

    G_free(stmt_lines);
    G_free(stmt);

    return 0;
}

/*!
   \brief Create PG-like array for int/float array

   \param array array of items
   \param nitems number of items in the array
   \param is_int TRUE for array of integers otherwise floats
   \param plus pointer to Plus_head struct
   \param[in,out] output buffer (re-used)
   \param[in,out] buffer size
 */
void build_stmt_id(const void *array, int nitems, int is_int,
                   const struct Plus_head *plus, char **stmt, size_t *stmt_size)
{
    int i, ivalue;
    int *iarray;
    float *farray;

    size_t stmt_id_size;
    char *stmt_id, buf_id[128];

    struct P_line *Line;

    if (is_int)
        iarray = (int *)array;
    else
        farray = (float *)array;

    if (!(*stmt)) {
        stmt_id_size = DB_SQL_MAX;
        stmt_id = (char *)G_malloc(stmt_id_size);
    }
    else {
        stmt_id_size = *stmt_size;
        stmt_id = *stmt;
    }

    /* reset array */
    stmt_id[0] = '\0';

    for (i = 0; i < nitems; i++) {
        /* realloc array if needed */
        if (strlen(stmt_id) + 100 > stmt_id_size) {
            stmt_id_size = strlen(stmt_id) + DB_SQL_MAX;
            stmt_id = (char *)G_realloc(stmt_id, stmt_id_size);
        }

        if (is_int) {
            if (plus) {
                Line = plus->Line[abs(iarray[i])];
                ivalue = (int)Line->offset;
                if (iarray[i] < 0)
                    ivalue *= -1;
            }
            else {
                ivalue = iarray[i];
            }
            sprintf(buf_id, "%d", ivalue);
        }
        else {
            sprintf(buf_id, "%f", farray[i]);
        }

        if (i > 0)
            strcat(stmt_id, ",");
        strcat(stmt_id, buf_id);
    }

    *stmt = stmt_id;
    *stmt_size = stmt_id_size;
}

/*!
   \brief Clean-up GRASS Topology tables

   \param pg_info pointer to Format_info_pg pg_info

   \return 0 on success
   \return -1 on error
 */
int Vect__clean_grass_db_topo(struct Format_info_pg *pg_info)
{
    char stmt[DB_SQL_MAX];

    sprintf(stmt, "DELETE FROM \"%s\".\"%s\"", pg_info->toposchema_name,
            TOPO_TABLE_NODE);
    if (-1 == Vect__execute_pg(pg_info->conn, stmt))
        return -1;

    sprintf(stmt, "DELETE FROM \"%s\".\"%s\"", pg_info->toposchema_name,
            TOPO_TABLE_LINE);
    if (-1 == Vect__execute_pg(pg_info->conn, stmt))
        return -1;

    sprintf(stmt, "DELETE FROM \"%s\".\"%s\"", pg_info->toposchema_name,
            TOPO_TABLE_AREA);
    if (-1 == Vect__execute_pg(pg_info->conn, stmt))
        return -1;

    sprintf(stmt, "DELETE FROM \"%s\".\"%s\"", pg_info->toposchema_name,
            TOPO_TABLE_ISLE);
    if (-1 == Vect__execute_pg(pg_info->conn, stmt))
        return -1;

    return 0;
}

/*!
   \brief Create simple features geometry from topogeometry data

   \param Map pointer to Map_info struct

   \return 0 on success
   \return -1 on error
 */
int create_simple_feature_from_topo(struct Map_info *Map)
{
    char stmt[DB_SQL_MAX];

    struct Format_info_pg *pg_info;

    pg_info = &(Map->fInfo.pg);

    G_debug(1, "build_simple_feature_from_topo(): %d", pg_info->feature_type);

    G_message(_("Create simple features topology from topogeometry data..."));
    Vect__execute_pg(pg_info->conn, "BEGIN");
    if (pg_info->feature_type == SF_POINT ||
        pg_info->feature_type == SF_LINESTRING) {
        sprintf(stmt,
                "UPDATE \"%s\".\"%s\" SET %s = (SELECT geom FROM \"%s\".node "
                "WHERE node_id = (%s).id)",
                pg_info->schema_name, pg_info->table_name, pg_info->geom_column,
                pg_info->toposchema_name, pg_info->topogeom_column);

        if (Vect__execute_pg(pg_info->conn, stmt) == -1) {
            Vect__execute_pg(pg_info->conn, "ROLLBACK");
            return -1;
        }
    }
    else if (pg_info->feature_type == SF_POLYGON) {
        Vect__copy_areas(Map, 1, Map);
    }
    else {
        G_warning(_("Unable to build simple features from topogeometry data. "
                    "Unsupported type %d."),
                  pg_info->feature_type);
    }

    Vect__execute_pg(pg_info->conn, "COMMIT");

    return 0;
}
#endif
