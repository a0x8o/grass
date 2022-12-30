/*!
 * \file lib/raster/range.c
 *
 * \brief Raster Library - Raster range file management
 *
 * (C) 2001-2009 GRASS Development Team
 *
 * This program is free software under the GNU General Public License
 * (>=v2). Read the file COPYING that comes with GRASS for details.
 *
 * \author Original author CERL
 */

#include <unistd.h>

#include <grass/raster.h>
#include <grass/glocale.h>

#include "R.h"

#define DEFAULT_CELL_MIN 1
#define DEFAULT_CELL_MAX 255

static void init_rstats(struct R_stats *);

/*!
   \brief Remove floating-point range

   Note: For internal use only.

   \param name map name
 */
void Rast__remove_fp_range(const char *name)
{
    G_remove_misc("cell_misc", "f_range", name);
}

/*!
 * \brief Construct default range
 *
 * Sets the integer range to [1,255]
 *
 * \param[out] r pointer to Range structure which holds range info
 */
void Rast_construct_default_range(struct Range *range)
{
    Rast_update_range(DEFAULT_CELL_MIN, range);
    Rast_update_range(DEFAULT_CELL_MAX, range);
}

/*!
 * \brief Read floating-point range
 *
 * Read the floating point range file <i>drange</i>. This file is
 * written in binary using XDR format.
 *
 * An empty range file indicates that the min, max are undefined. This
 * is a valid case, and the result should be an initialized range
 * struct with no defined min/max.  If the range file is missing and
 * the map is a floating-point map, this function will create a
 * default range by calling G_construct_default_range().
 *
 * \param name map name
 * \param mapset mapset name
 * \param drange pointer to FPRange structure which holds fp range
 *
 * \return 1 on success
 * \return 2 range is empty
 * \return -1 on error
 */
int Rast_read_fp_range(const char *name, const char *mapset,
                       struct FPRange *drange)
{
    struct Range range;
    int fd;
    char xdr_buf[2][XDR_DOUBLE_NBYTES];
    DCELL dcell1, dcell2;

    Rast_init();
    Rast_init_fp_range(drange);

    if (Rast_map_type(name, mapset) == CELL_TYPE) {
        /* if map is integer
           read integer range and convert it to double */

        if (Rast_read_range(name, mapset, &range) >= 0) {
            /* if the integer range is empty */
            if (range.first_time)
                return 2;

            Rast_update_fp_range((DCELL)range.min, drange);
            Rast_update_fp_range((DCELL)range.max, drange);
            return 1;
        }
        return -1;
    }

    fd = -1;

    if (G_find_file2_misc("cell_misc", "f_range", name, mapset)) {
        fd = G_open_old_misc("cell_misc", "f_range", name, mapset);
        if (fd < 0) {
            G_warning(_("Unable to read fp range file for <%s>"),
                      G_fully_qualified_name(name, mapset));
            return -1;
        }

        if (read(fd, xdr_buf, sizeof(xdr_buf)) != sizeof(xdr_buf)) {
            /* if the f_range file exists, but empty file, meaning Nulls */
            close(fd);
            G_debug(1, "Empty fp range file meaning Nulls for <%s>",
                    G_fully_qualified_name(name, mapset));
            return 2;
        }

        G_xdr_get_double(&dcell1, xdr_buf[0]);
        G_xdr_get_double(&dcell2, xdr_buf[1]);

        Rast_update_fp_range(dcell1, drange);
        Rast_update_fp_range(dcell2, drange);
        close(fd);
    }
    else {
        /* "f_range" file does not exist */
        G_warning(_("Missing fp range file for <%s> (run r.support -s)"),
                  G_fully_qualified_name(name, mapset));
        return -1;
    }

    return 1;
}

/*!
 * \brief Read raster range (CELL)
 *
 * This routine reads the range information for the raster map
 * <i>name</i> in <i>mapset</i> into the <i>range</i> structure.
 *
 * A diagnostic message is printed and -1 is returned if there is an error
 * reading the range file. Otherwise, 0 is returned.
 *
 * Old range file (those with 4 numbers) should treat zeros in this
 * file as NULL-values. New range files (those with just 2 numbers)
 * should treat these numbers as real data (zeros are real data in
 * this case).  An empty range file indicates that the min, max are
 * undefined. This is a valid case, and the result should be an
 * initialized range struct with no defined min/max. If the range file
 * is missing and the map is a floating-point map, this function will
 * create a default range by calling G_construct_default_range().
 *
 * \param name map name
 * \param mapset mapset name
 * \param[out] range pointer to Range structure which holds range info
 *
 * \return -1 on error
 * \return 1 on success
 * \return 2 if range is empty
 * \return 3 if raster map is floating-point, get range from quant rules
 */
int Rast_read_range(const char *name, const char *mapset, struct Range *range)
{
    FILE *fd;
    CELL x[4];
    char buf[200];
    int n, count;
    struct Quant quant;
    struct FPRange drange;

    Rast_init_range(range);
    fd = NULL;

    /* if map is not integer, read quant rules, and get limits */
    if (Rast_map_type(name, mapset) != CELL_TYPE) {
        DCELL dmin, dmax;

        if (Rast_read_quant(name, mapset, &quant) < 0) {
            G_warning(_("Unable to read quant rules for raster map <%s>"),
                      G_fully_qualified_name(name, mapset));
            return -1;
        }
        if (Rast_quant_is_truncate(&quant) || Rast_quant_is_round(&quant)) {
            if (Rast_read_fp_range(name, mapset, &drange) >= 0) {
                Rast_get_fp_range_min_max(&drange, &dmin, &dmax);
                if (Rast_quant_is_truncate(&quant)) {
                    x[0] = (CELL)dmin;
                    x[1] = (CELL)dmax;
                }
                else { /* round */

                    if (dmin > 0)
                        x[0] = (CELL)(dmin + .5);
                    else
                        x[0] = (CELL)(dmin - .5);
                    if (dmax > 0)
                        x[1] = (CELL)(dmax + .5);
                    else
                        x[1] = (CELL)(dmax - .5);
                }
            }
            else
                return -1;
        }
        else
            Rast_quant_get_limits(&quant, &dmin, &dmax, &x[0], &x[1]);

        Rast_update_range(x[0], range);
        Rast_update_range(x[1], range);
        return 3;
    }

    if (G_find_file2_misc("cell_misc", "range", name, mapset)) {
        fd = G_fopen_old_misc("cell_misc", "range", name, mapset);
        if (!fd) {
            G_warning(_("Unable to read range file for <%s>"),
                      G_fully_qualified_name(name, mapset));
            return -1;
        }

        /* if range file exists but empty */
        if (!fgets(buf, sizeof buf, fd)) {
            if (fd)
                fclose(fd);
            return 2;
        }

        x[0] = x[1] = x[2] = x[3] = 0;
        count = sscanf(buf, "%d%d%d%d", &x[0], &x[1], &x[2], &x[3]);

        /* if wrong format */
        if (count <= 0) {
            if (fd)
                fclose(fd);

            G_warning(_("Unable to read range file for <%s>"),
                      G_fully_qualified_name(name, mapset));
            return -1;
        }

        for (n = 0; n < count; n++) {
            /* if count==4, the range file is old (4.1) and 0's in it
               have to be ignored */
            if (count < 4 || x[n])
                Rast_update_range((CELL)x[n], range);
        }
        fclose(fd);
    }
    else {
        /* "range" file does not exist */
        G_warning(_("Missing range file for <%s> (run r.support -s)"),
                  G_fully_qualified_name(name, mapset));
        return -1;
    }

    return 1;
}

/*!
 * \brief Read raster stats
 *
 * Read the stats file <i>stats</i>. This file is
 * written in binary using XDR format.
 *
 * An empty stats file indicates that all cells are NULL. This
 * is a valid case, and the result should be an initialized rstats
 * struct with no defined stats.  If the stats file is missing
 * this function will create a default stats with count = 0.
 *
 * \param name map name
 * \param mapset mapset name
 * \param rstats pointer to R_stats structure which holds raster stats
 *
 * \return 1 on success
 * \return 2 stats is empty
 * \return -1 on error or stats file does not exist
 */
int Rast_read_rstats(const char *name, const char *mapset,
                     struct R_stats *rstats)
{
    int fd;
    char xdr_buf[2][XDR_DOUBLE_NBYTES];
    DCELL dcell1, dcell2;
    unsigned char cc[8];
    char nbytes;
    int i;
    grass_int64 count;

    Rast_init();
    init_rstats(rstats);

    fd = -1;

    if (!G_find_file2_misc("cell_misc", "stats", name, mapset)) {
        G_debug(1, "Stats file does not exist");
        return -1;
    }

    fd = G_open_old_misc("cell_misc", "stats", name, mapset);
    if (fd < 0) {
        G_warning(_("Unable to read stats file for <%s>"),
                  G_fully_qualified_name(name, mapset));
        return -1;
    }

    if (read(fd, xdr_buf, sizeof(xdr_buf)) != sizeof(xdr_buf)) {
        /* if the stats file exists, but empty file, meaning Nulls */
        close(fd);
        G_debug(1, "Empty stats file meaning Nulls for <%s>",
                G_fully_qualified_name(name, mapset));
        return 2;
    }

    G_xdr_get_double(&dcell1, xdr_buf[0]);
    G_xdr_get_double(&dcell2, xdr_buf[1]);

    rstats->sum = dcell1;
    rstats->sumsq = dcell2;

    /* count; see cell_values_int() in get_row.c */
    nbytes = 1;
    if (read(fd, &nbytes, 1) != 1) {
        /* if the stats file exists, but empty file, meaning Nulls */
        close(fd);
        G_debug(1, "Unable to read byte count in stats file for <%s>",
                G_fully_qualified_name(name, mapset));
        return -1;
    }

    count = 0;
    if (nbytes == 0)
        return 1;

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
>>>>>>> main
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81fd408422 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
>>>>>>> osgeo-main
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
<<<<<<< HEAD
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 81fd408422 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
    if (nbytes < 1 || (unsigned char)nbytes > sizeof(grass_int64)) {
=======
    if (nbytes < 1 || nbytes > sizeof(grass_int64)) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
        close(fd);
        G_debug(1, "Invalid byte count in stats file for <%s>",
                G_fully_qualified_name(name, mapset));
        return -1;
    }
    if (read(fd, cc, nbytes) != nbytes) {
        /* incorrect number of bytes for count */
        close(fd);
        G_debug(1, "Unable to read count in stats file for <%s>",
                G_fully_qualified_name(name, mapset));
        return -1;
    }

    /* copy byte by byte */
    for (i = nbytes - 1; i >= 0; i--) {
        count = (count << 8);
        count = count + cc[i];
    }
    rstats->count = count;

    close(fd);

    return 1;
}

/*!
 * \brief Write raster range file
 *
 * This routine writes the range information for the raster map
 * <i>name</i> in the current mapset from the <i>range</i> structure.
 * A diagnostic message is printed and -1 is returned if there is an
 * error writing the range file. Otherwise, 0 is returned.
 *
 * This routine only writes 2 numbers (min,max) to the range
 * file, instead of the 4 (pmin,pmax,nmin,nmax) previously written.
 * If there is no defined min,max, an empty file is written.
 *
 * \param name map name
 * \param range pointer to Range structure which holds range info
 */
void Rast_write_range(const char *name, const struct Range *range)
{
    FILE *fp;

    Rast_write_rstats(name, &(range->rstats));

    if (Rast_map_type(name, G_mapset()) != CELL_TYPE) {
        G_remove_misc("cell_misc", "range",
                      name); /* remove the old file with this name */
        G_fatal_error(_("Unable to write range file for <%s>"), name);
    }

    fp = G_fopen_new_misc("cell_misc", "range", name);
    if (!fp) {
        G_remove_misc("cell_misc", "range",
                      name); /* remove the old file with this name */
        G_fatal_error(_("Unable to write range file for <%s>"), name);
    }

    /* if range has been updated */
    if (!range->first_time)
        fprintf(fp, "%ld %ld\n", (long)range->min, (long)range->max);

    fclose(fp);
}

/*!
 * \brief Write raster range file (floating-point)
 *
 * Write the floating point range file <tt>f_range</tt>. This file is
 * written in binary using XDR format. If there is no defined min/max
 * in <em>range</em>, an empty <tt>f_range</tt> file is created.
 *
 * \param name map name
 * \param range pointer to FPRange which holds fp range info
 */
void Rast_write_fp_range(const char *name, const struct FPRange *range)
{
    int fd;
    char xdr_buf[2][XDR_DOUBLE_NBYTES];

    Rast_init();

    Rast_write_rstats(name, &(range->rstats));

    fd = G_open_new_misc("cell_misc", "f_range", name);
    if (fd < 0) {
        G_remove_misc("cell_misc", "f_range", name);
        G_fatal_error(_("Unable to write range file for <%s>"), name);
    }

    /* if range hasn't been updated, write empty file meaning Nulls */
    if (range->first_time) {
        close(fd);
        return;
    }

    G_xdr_put_double(xdr_buf[0], &range->min);
    G_xdr_put_double(xdr_buf[1], &range->max);

    if (write(fd, xdr_buf, sizeof(xdr_buf)) != sizeof(xdr_buf)) {
        G_remove_misc("cell_misc", "f_range", name);
        G_fatal_error(_("Unable to write range file for <%s>"), name);
    }

    close(fd);
}

/*!
 * \brief Write raster stats file
 *
 * Write the stats file <tt>stats</tt>. This file is
 * written in binary using XDR format. If the count is < 1
 * in <em>rstats</em>, an empty <tt>stats</tt> file is created.
 *
 * \param name map name
 * \param rstats pointer to R_stats which holds stats info
 */
void Rast_write_rstats(const char *name, const struct R_stats *rstats)
{
    int fd;
    char xdr_buf[2][XDR_DOUBLE_NBYTES];
    unsigned char cc[8];
    char nbytes;
    unsigned int i;
    grass_int64 count;

    Rast_init();

    fd = G_open_new_misc("cell_misc", "stats", name);
    if (fd < 0) {
        G_remove_misc("cell_misc", "stats", name);
        G_fatal_error(_("Unable to write stats file for <%s>"), name);
    }

    /* if count is zero, write empty file meaning Nulls */
    if (rstats->count < 1) {
        close(fd);
        return;
    }

    G_xdr_put_double(xdr_buf[0], &rstats->sum);
    G_xdr_put_double(xdr_buf[1], &rstats->sumsq);

    if (write(fd, xdr_buf, sizeof(xdr_buf)) != sizeof(xdr_buf)) {
        G_remove_misc("cell_misc", "stats", name);
        G_fatal_error(_("Unable to write stats file for <%s>"), name);
    }

    /* count; see convert_int() in put_row.c */
    count = rstats->count;
    nbytes = 0;
    /* copy byte by byte */
    for (i = 0; i < sizeof(grass_int64); i++) {
        cc[i] = count & 0xff;
        count >>= 8;
        if (cc[i])
            nbytes = i;
    }
    nbytes++;

    /* number of bytes needed for count */
    if (write(fd, &nbytes, 1) != 1) {
        G_remove_misc("cell_misc", "stats", name);
        G_fatal_error(_("Unable to write stats file for <%s>"), name);
    }

    if (nbytes > 0 && write(fd, cc, nbytes) != nbytes) {
        G_remove_misc("cell_misc", "stats", name);
        G_fatal_error(_("Unable to write stats file for <%s>"), name);
    }

    close(fd);
}

/*!
 * \brief Update range structure (CELL)
 *
 * Compares the <i>cat</i> value with the minimum and maximum values
 * in the <i>range</i> structure, modifying the range if <i>cat</i>
 * extends the range.
 *
 * NULL-values must be detected and ignored.
 *
 * \param cat raster value
 * \param range pointer to Range structure which holds range info
 */
void Rast_update_range(CELL cat, struct Range *range)
{
    if (!Rast_is_c_null_value(&cat)) {
        if (range->first_time) {
            range->first_time = 0;
            range->min = cat;
            range->max = cat;
            return;
        }
        if (cat < range->min)
            range->min = cat;
        if (cat > range->max)
            range->max = cat;
    }
}

/*!
 * \brief Update range structure (floating-point)
 *
 * Compares the <i>cat</i> value with the minimum and maximum values
 * in the <i>range</i> structure, modifying the range if <i>cat</i>
 * extends the range.
 *
 * NULL-values must be detected and ignored.
 *
 * \param val raster value
 * \param range pointer to Range structure which holds range info
 */
void Rast_update_fp_range(DCELL val, struct FPRange *range)
{
    if (!Rast_is_d_null_value(&val)) {
        if (range->first_time) {
            range->first_time = 0;
            range->min = val;
            range->max = val;
            return;
        }
        if (val < range->min)
            range->min = val;
        if (val > range->max)
            range->max = val;
    }
}

/*!
 * \brief Update range structure based on raster row (CELL)
 *
 * This routine updates the <i>range</i> data just like
 * Rast_update_range(), but for <i>n</i> values from the <i>cell</i>
 * array.
 *
 * \param cell raster values
 * \param n number of values
 * \param range pointer to Range structure which holds range info
 */
void Rast_row_update_range(const CELL *cell, int n, struct Range *range)
{
    Rast__row_update_range(cell, n, range, 0);
}

/*!
 * \brief Update range structure based on raster row
 *
 * Note: for internal use only.
 *
 * \param cell raster values
 * \param n number of values
 * \param range pointer to Range structure which holds range info
 * \param ignore_zeros ignore zeros
 */
void Rast__row_update_range(const CELL *cell, int n, struct Range *range,
                            int ignore_zeros)
{
    CELL cat;

    while (n-- > 0) {
        cat = *cell++;
        if (Rast_is_c_null_value(&cat) || (ignore_zeros && !cat))
            continue;
        if (range->first_time) {
            range->first_time = 0;
            range->min = cat;
            range->max = cat;

            range->rstats.sum = cat;
            range->rstats.sumsq = (DCELL)cat * cat;

            range->rstats.count = 1;

            continue;
        }
        if (cat < range->min)
            range->min = cat;
        if (cat > range->max)
            range->max = cat;

        range->rstats.sum += cat;
        range->rstats.sumsq += (DCELL)cat * cat;

        range->rstats.count += 1;
    }
}

/*!
 * \brief Update range structure based on raster row (floating-point)
 *
 * This routine updates the <i>range</i> data just like
 * Rast_update_range(), but for <i>n</i> values from the <i>cell</i>
 * array.
 *
 * \param cell raster values
 * \param n number of values
 * \param range pointer to Range structure which holds range info
 * \param data_type raster type (CELL, FCELL, DCELL)
 */
void Rast_row_update_fp_range(const void *rast, int n, struct FPRange *range,
                              RASTER_MAP_TYPE data_type)
{
    size_t size = Rast_cell_size(data_type);
    DCELL val = 0.0;

    while (n-- > 0) {
        switch (data_type) {
        case CELL_TYPE:
            val = (DCELL) * ((CELL *)rast);
            break;
        case FCELL_TYPE:
            val = (DCELL) * ((FCELL *)rast);
            break;
        case DCELL_TYPE:
            val = *((DCELL *)rast);
            break;
        }

        if (Rast_is_null_value(rast, data_type)) {
            rast = G_incr_void_ptr(rast, size);
            continue;
        }
        if (range->first_time) {
            range->first_time = 0;
            range->min = val;
            range->max = val;

            range->rstats.sum = val;
            range->rstats.sumsq = val * val;
            range->rstats.count = 1;
        }
        else {
            if (val < range->min)
                range->min = val;
            if (val > range->max)
                range->max = val;

            range->rstats.sum += val;
            range->rstats.sumsq += val * val;
            range->rstats.count += 1;
        }

        rast = G_incr_void_ptr(rast, size);
    }
}

/*!
 * \brief Initialize range structure
 *
 * Initializes the <i>range</i> structure for updates by
 * Rast_update_range() and Rast_row_update_range().
 *
 * Must set a flag in the range structure that indicates that no
 * min/max have been defined - probably a <tt>"first"</tt> boolean
 * flag.
 *
 * \param range pointer to Range structure which holds range info
 */
void Rast_init_range(struct Range *range)
{
    Rast_set_c_null_value(&(range->min), 1);
    Rast_set_c_null_value(&(range->max), 1);

    init_rstats(&range->rstats);

    range->first_time = 1;
}

/*!
 * \brief Get range min and max
 *
 * The minimum and maximum CELL values are extracted from the
 * <i>range</i> structure.
 *
 * If the range structure has no defined min/max (first!=0) there will
 * not be a valid range. In this case the min and max returned must be
 * the NULL-value.
 *
 * \param range pointer to Range structure which holds range info
 * \param[out] min minimum value
 * \param[out] max maximum value
 */
void Rast_get_range_min_max(const struct Range *range, CELL *min, CELL *max)
{
    if (range->first_time) {
        Rast_set_c_null_value(min, 1);
        Rast_set_c_null_value(max, 1);
    }
    else {
        if (Rast_is_c_null_value(&(range->min)))
            Rast_set_c_null_value(min, 1);
        else
            *min = range->min;

        if (Rast_is_c_null_value(&(range->max)))
            Rast_set_c_null_value(max, 1);
        else
            *max = range->max;
    }
}

/*!
 * \brief Initialize fp range
 *
 * Must set a flag in the range structure that indicates that no
 * min/max have been defined - probably a <tt>"first"</tt> boolean
 * flag.
 *
 * \param range pointer to FPRange which holds fp range info
 */
void Rast_init_fp_range(struct FPRange *range)
{
    Rast_set_d_null_value(&(range->min), 1);
    Rast_set_d_null_value(&(range->max), 1);

    init_rstats(&range->rstats);

    range->first_time = 1;
}

/*!
 * \brief Get minimum and maximum value from fp range
 *
 * Extract the min/max from the range structure <i>range</i>.  If the
 * range structure has no defined min/max (first!=0) there will not be
 * a valid range. In this case the min and max returned must be the
 * NULL-value.
 *
 * \param range pointer to FPRange which holds fp range info
 * \param[out] min minimum value
 * \param[out] max maximum value
 */
void Rast_get_fp_range_min_max(const struct FPRange *range, DCELL *min,
                               DCELL *max)
{
    if (range->first_time) {
        Rast_set_d_null_value(min, 1);
        Rast_set_d_null_value(max, 1);
    }
    else {
        if (Rast_is_d_null_value(&(range->min)))
            Rast_set_d_null_value(min, 1);
        else
            *min = range->min;

        if (Rast_is_d_null_value(&(range->max)))
            Rast_set_d_null_value(max, 1);
        else
            *max = range->max;
    }
}

static void init_rstats(struct R_stats *rstats)
{
    Rast_set_d_null_value(&(rstats->sum), 1);
    Rast_set_d_null_value(&(rstats->sumsq), 1);
    rstats->count = 0;
}
