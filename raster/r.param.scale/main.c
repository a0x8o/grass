/****************************************************************************
 *
 * MODULE:       r.param.scale
 * AUTHOR(S):    Jo Wood, V 1.1, 11th December, 1994 (original contributor)
 * PURPOSE:      GRASS module for extracting multi-scale surface parameters.
 * COPYRIGHT:    (C) 1999-2004 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <grass/glocale.h>
#include "param.h"

const char *rast_in_name;  /* Name of the raster file to process.  */
const char *rast_out_name; /* Name of the raster output file.      */
int constrained;           /* Flag that forces quadtratic through  */

/* the central cell of the window.      */
int fd_in,  /* File descriptor for input and        */
    fd_out, /* output raster files.                 */
    wsize,  /* Size of local processing window.     */
    mparam; /* Morphometric parameter to calculate. */

double resoln, /* Planimetric resolution.              */
    exponent,  /* Distance weighting exponent.         */
    zscale,    /* Vertical scaling factor.             */
    slope_tol, /* Vertical tolerences for surface      */
    curve_tol; /* feature identification.              */

int main(int argc, char **argv)
{
    interface(argc, argv);

    /* Make sure that the current projection is not lat/long */
    if ((G_projection() == PROJECTION_LL))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
        G_fatal_error(_("Lat/Long projects are not supported by this module"));
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long locations are not supported by this module"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main

    open_files();

    process();

    close_down();

    if (mparam == FEATURE) {
        write_cols();
        write_cats();
    }

    return 0;
}
