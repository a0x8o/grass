/*!
 * \file lib/gis/view.c
 *
 * \brief GIS Library - 3D View functions.
 *
 * (C) 2001-2014 by the GRASS Development Team
 *
 * This program is free software under the GNU General Public License
 * (>=v2). Read the file COPYING that comes with GRASS for details.
 *
 * \author Bill Brown - US Army CERL
 *
 * \date 1992-2008
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <grass/gis.h>
#include <grass/glocale.h>

#define REQ_KEYS 8

static int compare_wind(const struct Cell_head *, const struct Cell_head *);
static int get_bool(const char *);
static void pr_winerr(int, const char *);
static void edge_sort(float sides[4]);
static int read_old_format(struct G_3dview *, FILE *);

static const int vers_major = 4;
static const int vers_minor = 1;

static int Suppress_warn = 0;

/**
 * \brief Turns 3D View warnings on and off.
 *
 * If Suppress_warn is 0, a warning will be printed if less than 95% of
 * the window when the view was saved overlaps the current window.
 *
 * \param[in] b
 * \return
 */

void G_3dview_warning(int b)
{
    Suppress_warn = b ? 0 : 1;
}

/**
 * \brief Sets default for <b>v</b> based on <b>w</b>.
 *
 * \param[in,out] v
 * \param[in] w
 * \return always returns 1
 */

int G_get_3dview_defaults(struct G_3dview *v, struct Cell_head *w)
{
    if (!v || !w)
        return (-1);

    v->exag = 1.0;
    v->fov = 40.0;
    v->from_to[0][0] = (w->east + w->west) / 2.0;
    v->from_to[0][1] = w->south - (w->north - w->south);
    v->from_to[0][2] = w->north - w->south;
    v->from_to[1][0] = (w->east + w->west) / 2.0;
    v->from_to[1][1] = (w->north + w->south) / 2.0;
    v->from_to[1][2] = 0.0;

    v->twist = 0.0;
    v->mesh_freq = 15;
    v->poly_freq = 1;
    v->display_type = 2;
    v->colorgrid = v->fringe = v->surfonly = v->lightson = v->doavg = 0;
    v->dozero = v->shading = 1;
    strcpy(v->bg_col, "black");
    strcpy(v->grid_col, "white");
    strcpy(v->other_col, "red");
    v->ambient = v->shine = 0.3;
    v->lightcol[0] = v->lightcol[1] = v->lightcol[2] = 0.8;
    v->lightpos[0] = w->west;
    v->lightpos[1] = w->north;
    v->lightpos[2] = (w->east - w->west) / 2.0;
    v->lightpos[3] = 1.0; /* local source */

    v->vwin.north = w->north;
    v->vwin.south = w->south;
    v->vwin.east = w->east;
    v->vwin.west = w->west;
    v->vwin.format = w->format;
    v->vwin.compressed = w->compressed;
    v->vwin.proj = w->proj;
    v->vwin.zone = w->zone;
    v->vwin.ew_res = w->ew_res;
    v->vwin.ns_res = w->ns_res;
    v->vwin.cols = w->cols;
    v->vwin.rows = w->rows;

    return (1);
}

/**
 * \brief Saves info to a 3d.view file in the current mapset.
 *
 * The address of a window (struct Cell_head *) may be passed, or if
 * NULL is passed, the Cell_head structure inside the G_3dview struct
 * will be used.  e.g., if you called <i>G_get_3dview_defaults</i> with
 * the Cell_head you want saved, the G_3dview returned already contains
 * the new Cell_head. But if you're using all the keywords, so didn't
 * need defaults, pass this routine the address of a Cell_head.<br>
 *
 * User should call <i>G_get_3dview_defaults</i> before filling a
 * G_3dview struct to be written if not using all of the optional
 * keywords.<br>
 *
 * These keywords are constant in all 3d.view files:<br>
 * PGM_ID<br>
 * <b>cell keywords:</b><br>
 * north<br>
 * south<br>
 * east<br>
 * west<br>
 * rows<br>
 * cols<br>
 * <b>required keywords:</b><br>
 * TO_EASTING<br>
 * TO_NORTHING<br>
 * TO_HEIGHT<br>
 * FROM_EASTING<br>
 * FROM_NORTHING<br>
 * FROM_HEIGHT<br>
 * Z_EXAG<br>
 * FIELD_VIEW<br>
 * <b>optional keywords:</b> (defaults provided when reading)<br>
 * TWIST<br>
 * MESH_FREQ<br>
 * POLY_RES<br>
 * DOAVG<br>
 * DISPLAY_TYPE<br>
 * DOZERO<br>
 * COLORGRID<br>
 * SHADING<br>
 * FRINGE<br>
 * BG_COL<br>
 * GRID_COL<br>
 * OTHER_COL<br>
 * LIGHTS_ON<br>
 * LIGHTPOS<br>
 * LIGHTCOL<br>
 * LIGHTAMBIENT<br>
 * SHINE<br>
 * SURFACEONLY<br>
 *
 * \param[in] fname file name
 * \param[in] View
 * \param[in] Win
 * \return 1 on success
 * \return -1 on error
 */

<<<<<<< HEAD
int G_put_3dview(const char *fname, const struct G_3dview *View,
                 const struct Cell_head *Win)
=======
int G_put_3dview(const char *fname, const char *mapset,
                 const struct G_3dview *View, const struct Cell_head *Win)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
{
    FILE *fp;

    if (NULL == (fp = G_fopen_new("3d.view", fname))) {
        G_warning(_("Unable to open %s for writing"), fname);
        return (-1);
    }

    fprintf(fp, "# %01d.%02d\n", vers_major, vers_minor);
    fprintf(fp, "PGM_ID: %s\n", View->pgm_id);

    if (Win) {
        fprintf(fp, "north: %f\n", Win->north);
        fprintf(fp, "south: %f\n", Win->south);
        fprintf(fp, "east: %f\n", Win->east);
        fprintf(fp, "west: %f\n", Win->west);
        fprintf(fp, "rows: %d\n", Win->rows);
        fprintf(fp, "cols: %d\n", Win->cols);
    }
    else {
        fprintf(fp, "north: %f\n", View->vwin.north);
        fprintf(fp, "south: %f\n", View->vwin.south);
        fprintf(fp, "east: %f\n", View->vwin.east);
        fprintf(fp, "west: %f\n", View->vwin.west);
        fprintf(fp, "rows: %d\n", View->vwin.rows);
        fprintf(fp, "cols: %d\n", View->vwin.cols);
    }

    fprintf(fp, "TO_EASTING: %f\n", View->from_to[1][0]);
    fprintf(fp, "TO_NORTHING: %f\n", View->from_to[1][1]);
    fprintf(fp, "TO_HEIGHT: %f\n", View->from_to[1][2]);
    fprintf(fp, "FROM_EASTING: %f\n", View->from_to[0][0]);
    fprintf(fp, "FROM_NORTHING: %f\n", View->from_to[0][1]);
    fprintf(fp, "FROM_HEIGHT: %f\n", View->from_to[0][2]);
    fprintf(fp, "Z_EXAG: %f\n", View->exag);
    fprintf(fp, "TWIST: %f\n", View->twist);
    fprintf(fp, "FIELD_VIEW: %f\n", View->fov);
    fprintf(fp, "MESH_FREQ: %d\n", View->mesh_freq);
    fprintf(fp, "POLY_RES: %d\n", View->poly_freq);
    fprintf(fp, "DOAVG: %d\n", View->doavg);
    fprintf(fp, "DISPLAY_TYPE: %d\n", View->display_type);
    fprintf(fp, "DOZERO: %d\n", View->dozero);

    fprintf(fp, "COLORGRID: %d\n", View->colorgrid); /* 1 = use color */
    fprintf(fp, "SHADING: %d\n", View->shading);
    fprintf(fp, "FRINGE: %d\n", View->fringe);
    fprintf(fp, "BG_COL: %s\n", View->bg_col);
    fprintf(fp, "GRID_COL: %s\n", View->grid_col);
    fprintf(fp, "OTHER_COL: %s\n", View->other_col);
    fprintf(fp, "SURFACEONLY: %d\n", View->surfonly);
    fprintf(fp, "LIGHTS_ON: %d\n", View->lightson);
    fprintf(fp, "LIGHTPOS: %f %f %f %f\n", View->lightpos[0], View->lightpos[1],
            View->lightpos[2], View->lightpos[3]);
    fprintf(fp, "LIGHTCOL: %f %f %f\n", View->lightcol[0], View->lightcol[1],
            View->lightcol[2]);
    fprintf(fp, "LIGHTAMBIENT: %f\n", View->ambient);
    fprintf(fp, "SHINE: %f\n", View->shine);

    fclose(fp);

    return (1);
}

/**
 * \brief Gets a 3D View.
 *
 * If reading an old format, the window boundaries are not checked
 * against the current window since boundaries weren't saved.
 *
 * \param[in] fname
 * \param[in] mapset
 * \param[in,out] View
 * \return -1 on error
 * \return 1 on success
 * \return 2 if <b>fname</b> was written with this version of routine
 * \return 0 if is older format (through 4.0)
 */

int G_get_3dview(const char *fname, const char *mapset, struct G_3dview *View)
{
    struct Cell_head curwin;
    FILE *fp;
    char buffer[80], keystring[24], boo[8], nbuf[128], ebuf[128];
    int lap, v_maj, v_min, wind_keys = 0, reqkeys = 0;
    int current = 0; /* current version flag */

    mapset = G_find_file2("3d.view", fname, mapset);
    if (mapset != NULL) {
        if (NULL == (fp = G_fopen_old("3d.view", fname, mapset))) {
            G_warning(_("Unable to open %s for reading"), fname);
            return (-1);
        }

        G_get_set_window(&curwin);
        G_get_3dview_defaults(View, &curwin);

        if (NULL != fgets(buffer, 80, fp)) {
            if (buffer[0] != '#') { /* old d.3d format */
                rewind(fp);
                if (0 <= read_old_format(View, fp))
                    return (0);
                else
                    return (-1);
            }
            else {
                sscanf(buffer, "#%d.%d\n", &v_maj, &v_min);
                if (v_maj == vers_major && v_min == vers_minor)
                    current = 1; /* same version */
            }
        }

        while (NULL != fgets(buffer, 75, fp)) {
            if (buffer[0] != '#') {

                sscanf(buffer, "%[^:]:", keystring);

                if (!strcmp(keystring, "PGM_ID")) {
                    sscanf(buffer, "%*s%s", (View->pgm_id));
                    continue;
                }
                if (!strcmp(keystring, "north")) {
                    sscanf(buffer, "%*s%lf", &(View->vwin.north));
                    ++wind_keys;
                    continue;
                }
                if (!strcmp(keystring, "south")) {
                    sscanf(buffer, "%*s%lf", &(View->vwin.south));
                    ++wind_keys;
                    continue;
                }
                if (!strcmp(keystring, "east")) {
                    sscanf(buffer, "%*s%lf", &(View->vwin.east));
                    ++wind_keys;
                    continue;
                }
                if (!strcmp(keystring, "west")) {
                    sscanf(buffer, "%*s%lf", &(View->vwin.west));
                    ++wind_keys;
                    continue;
                }
                if (!strcmp(keystring, "rows")) {
                    sscanf(buffer, "%*s%d", &(View->vwin.rows));
                    ++wind_keys;
                    continue;
                }
                if (!strcmp(keystring, "cols")) {
                    sscanf(buffer, "%*s%d", &(View->vwin.cols));
                    ++wind_keys;
                    continue;
                }
                if (!strcmp(keystring, "TO_EASTING")) {
                    sscanf(buffer, "%*s%f", &(View->from_to[1][0]));
                    ++reqkeys;
                    continue;
                }
                if (!strcmp(keystring, "TO_NORTHING")) {
                    sscanf(buffer, "%*s%f", &(View->from_to[1][1]));
                    ++reqkeys;
                    continue;
                }
                if (!strcmp(keystring, "TO_HEIGHT")) {
                    sscanf(buffer, "%*s%f", &(View->from_to[1][2]));
                    ++reqkeys;
                    continue;
                }
                if (!strcmp(keystring, "FROM_EASTING")) {
                    sscanf(buffer, "%*s%f", &(View->from_to[0][0]));
                    ++reqkeys;
                    continue;
                }
                if (!strcmp(keystring, "FROM_NORTHING")) {
                    sscanf(buffer, "%*s%f", &(View->from_to[0][1]));
                    ++reqkeys;
                    continue;
                }
                if (!strcmp(keystring, "FROM_HEIGHT")) {
                    sscanf(buffer, "%*s%f", &(View->from_to[0][2]));
                    ++reqkeys;
                    continue;
                }
                if (!strcmp(keystring, "Z_EXAG")) {
                    sscanf(buffer, "%*s%f", &(View->exag));
                    ++reqkeys;
                    continue;
                }
                if (!strcmp(keystring, "MESH_FREQ")) {
                    sscanf(buffer, "%*s%d", &(View->mesh_freq));
                    continue;
                }
                if (!strcmp(keystring, "POLY_RES")) {
                    sscanf(buffer, "%*s%d", &(View->poly_freq));
                    continue;
                }
                if (!strcmp(keystring, "DOAVG")) {
                    sscanf(buffer, "%*s%d", &(View->doavg));
                    continue;
                }
                if (!strcmp(keystring, "FIELD_VIEW")) {
                    sscanf(buffer, "%*s%f", &(View->fov));
                    ++reqkeys;
                    continue;
                }
                if (!strcmp(keystring, "TWIST")) {
                    sscanf(buffer, "%*s%f", &(View->twist));
                    continue;
                }
                if (!strcmp(keystring, "DISPLAY_TYPE")) {
                    sscanf(buffer, "%*s%d", &View->display_type);
                    continue;
                }
                if (!strcmp(keystring, "DOZERO")) {
                    sscanf(buffer, "%*s%s", boo);
                    View->dozero = get_bool(boo);
                    continue;
                }
                if (!strcmp(keystring, "COLORGRID")) {
                    sscanf(buffer, "%*s%s", boo);
                    View->colorgrid = get_bool(boo);
                    continue;
                }
                if (!strcmp(keystring, "FRINGE")) {
                    sscanf(buffer, "%*s%s", boo);
                    View->fringe = get_bool(boo);
                    continue;
                }
                if (!strcmp(keystring, "SHADING")) {
                    sscanf(buffer, "%*s%s", boo);
                    View->shading = get_bool(boo);
                    continue;
                }
                if (!strcmp(keystring, "BG_COL")) {
                    sscanf(buffer, "%*s%s", View->bg_col);
                    continue;
                }
                if (!strcmp(keystring, "GRID_COL")) {
                    sscanf(buffer, "%*s%s", View->grid_col);
                    continue;
                }
                if (!strcmp(keystring, "OTHER_COL")) {
                    sscanf(buffer, "%*s%s", View->other_col);
                    continue;
                }
                if (!strcmp(keystring, "SURFACEONLY")) {
                    sscanf(buffer, "%*s%s", boo);
                    View->surfonly = get_bool(boo);
                    continue;
                }
                if (!strcmp(keystring, "LIGHTS_ON")) {
                    sscanf(buffer, "%*s%s", boo);
                    View->lightson = get_bool(boo);
                    continue;
                }
                if (!strcmp(keystring, "LIGHTPOS")) {
                    sscanf(buffer, "%*s%f%f%f%f", &(View->lightpos[0]),
                           &(View->lightpos[1]), &(View->lightpos[2]),
                           &(View->lightpos[3]));
                    continue;
                }
                if (!strcmp(keystring, "LIGHTCOL")) {
                    sscanf(buffer, "%*s%f%f%f", &(View->lightcol[0]),
                           &(View->lightcol[1]), &(View->lightcol[2]));
                    continue;
                }
                if (!strcmp(keystring, "LIGHTAMBIENT")) {
                    sscanf(buffer, "%*s%f", &(View->ambient));
                    continue;
                }
                if (!strcmp(keystring, "SHINE")) {
                    sscanf(buffer, "%*s%f", &(View->shine));
                    continue;
                }
            }
        }

        fclose(fp);

        if (reqkeys != REQ_KEYS) /* required keys not found */
            return (-1);

        /* fill rest of View->vwin */
        if (wind_keys == 6) {
            View->vwin.ew_res =
                (View->vwin.east - View->vwin.west) / View->vwin.cols;
            View->vwin.ns_res =
                (View->vwin.north - View->vwin.south) / View->vwin.rows;
        }
        else
            return (0); /* older format */

        if (!Suppress_warn) {
            if (95 > (lap = compare_wind(&(View->vwin), &curwin))) {

                fprintf(stderr, _("GRASS window when view was saved:\n"));
                G_format_northing(View->vwin.north, nbuf, G_projection());
                fprintf(stderr, "north:   %s\n", nbuf);
                G_format_northing(View->vwin.south, nbuf, G_projection());
                fprintf(stderr, "south:   %s\n", nbuf);
                G_format_easting(View->vwin.east, ebuf, G_projection());
                fprintf(stderr, "east:    %s\n", ebuf);
                G_format_easting(View->vwin.west, ebuf, G_projection());
                fprintf(stderr, "west:    %s\n", ebuf);
                pr_winerr(lap, fname);
            }
        }
    }
    else {
        G_warning(_("Unable to open %s for reading"), fname);
        return (-1);
    }

    if (current)
        return (2);

    return (1);
}

/* returns the percentage of savedwin that overlaps curwin */

static int compare_wind(const struct Cell_head *savedwin,
                        const struct Cell_head *curwin)
{
    float e_ings[4], n_ings[4], area_lap, area_saved;
    int outside = 0;

    if (savedwin->north < curwin->south)
        outside = 1;
    if (savedwin->south > curwin->north)
        outside = 1;
    if (savedwin->east < curwin->west)
        outside = 1;
    if (savedwin->west > curwin->east)
        outside = 1;
    if (outside)
        return (0);

    e_ings[0] = savedwin->west;
    e_ings[1] = savedwin->east;
    e_ings[2] = curwin->west;
    e_ings[3] = curwin->east;
    edge_sort(e_ings);

    n_ings[0] = savedwin->south;
    n_ings[1] = savedwin->north;
    n_ings[2] = curwin->south;
    n_ings[3] = curwin->north;
    edge_sort(n_ings);

    area_lap = (e_ings[2] - e_ings[1]) * (n_ings[2] - n_ings[1]);
    area_saved =
        (savedwin->east - savedwin->west) * (savedwin->north - savedwin->south);

    return ((int)(area_lap * 100.0 / area_saved));
}

static int get_bool(const char *str)
{
    if (str[0] == 'y' || str[0] == 'Y')
        return (1);
    if (str[0] == 'n' || str[0] == 'N')
        return (0);

    return (atoi(str) ? 1 : 0);
}

static void
pr_winerr(int vis, /* % of saved window overlapping current window */
          const char *viewname)
{
    switch (vis) {
    case 0:
        G_warning(_(" Window saved in \"%s\" is completely outside of current "
                    "GRASS window."),
                  viewname);
        break;
    default:
        G_warning(_(" Only %d%% of window saved in \"%s\" overlaps with "
                    "current GRASS window."),
                  vis, viewname);
        break;
    }
}

/*********************************************************************/
/* sorts 4 floats from lowest to highest */

static void edge_sort(float sides[4])
{
    int i, j;
    float temp;

    for (i = 0; i < 4; ++i) {
        for (j = i + 1; j < 4; ++j) {
            if (sides[j] < sides[i]) { /* then swap */
                temp = sides[i];
                sides[i] = sides[j];
                sides[j] = temp;
            }
        }
    }
}

static int read_old_format(struct G_3dview *v, FILE *fp)
{
    char buffer[80];
    int req_keys = 0;
    double td;
    char boo[8];

    strcpy((v->pgm_id), "d.3d");
    if (1 == sscanf(fgets(buffer, 80, fp), "%f", &(v->from_to[1][0])))
        ++req_keys;
    if (1 == sscanf(fgets(buffer, 80, fp), "%f", &(v->from_to[1][1])))
        ++req_keys;
    if (1 == sscanf(fgets(buffer, 80, fp), "%f", &(v->from_to[1][2])))
        ++req_keys;
    if (1 == sscanf(fgets(buffer, 80, fp), "%f", &(v->from_to[0][0])))
        ++req_keys;
    if (1 == sscanf(fgets(buffer, 80, fp), "%f", &(v->from_to[0][1])))
        ++req_keys;
    if (1 == sscanf(fgets(buffer, 80, fp), "%f", &(v->from_to[0][2])))
        ++req_keys;
    if (1 == sscanf(fgets(buffer, 80, fp), "%f", &(v->exag)))
        ++req_keys;
    sscanf(fgets(buffer, 80, fp), "%d", &(v->mesh_freq));
    if (1 == sscanf(fgets(buffer, 80, fp), "%f", &(v->fov)))
        ++req_keys;
    if (1 == sscanf(fgets(buffer, 80, fp), "%lf", &td)) { /* resolution */
        v->vwin.rows = (v->vwin.north - v->vwin.south) / td;
        v->vwin.cols = (v->vwin.east - v->vwin.west) / td;
        v->vwin.ew_res = v->vwin.ns_res = td;
    }

    sscanf(fgets(buffer, 80, fp), "%s", boo); /* linesonly */
    v->display_type = get_bool(boo) ? 1 : 3;
    sscanf(fgets(buffer, 80, fp), "%s", boo);
    v->dozero = get_bool(boo);
    sscanf(fgets(buffer, 80, fp), "%s", v->grid_col);
    if (!strcmp(v->grid_col, "color"))
        v->colorgrid = 1;

    sscanf(fgets(buffer, 80, fp), "%s", v->other_col);
    sscanf(fgets(buffer, 80, fp), "%s", v->bg_col);
    sscanf(fgets(buffer, 80, fp), "%s", boo);
    v->doavg = get_bool(boo);

    if (v->exag) { /* old 3d.view files saved height with no exag */
        v->from_to[0][2] /= v->exag;
        v->from_to[1][2] /= v->exag;
    }

    fclose(fp);
    if (req_keys == REQ_KEYS)
        return (1);
    else
        return (-1);
}
