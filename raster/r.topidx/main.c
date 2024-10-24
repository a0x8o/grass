/****************************************************************************
 *
 * MODULE:       r.topidx
 *
 * AUTHOR(S):    Huidae Cho <grass4u gmail.com>, Hydro Laboratory,
 *               Kyungpook National University
 *               Based on GRIDATB.FOR by Keith Beven <k.beven lancaster.ac.uk>
 *
 * PURPOSE:      Creates a topographic index raster map from an elevation
 *               raster map.
 *
 * COPYRIGHT:    (C) 2000-2014 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#define _MAIN_C_
#include <stdlib.h>
#include <grass/gis.h>
#include <grass/glocale.h>
#include "global.h"

int main(int argc, char **argv)
{
    struct GModule *module;
    struct {
        struct Option *input;
        struct Option *output;
    } params;

    G_gisinit(argv[0]);

    module = G_define_module();
    G_add_keyword(_("raster"));
    G_add_keyword(_("hydrology"));
    G_add_keyword(_("wetness"));
    G_add_keyword(_("topographic index"));
    module->description = _("Creates a topographic index (wetness index) "
                            "raster map from an elevation raster map.");

    params.input = G_define_standard_option(G_OPT_R_ELEV);
    params.input->key = "input";

    params.output = G_define_standard_option(G_OPT_R_OUTPUT);
    params.output->description =
        _("Name for output topographic index raster map");

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    /* Make sure that the current projection is not lat/long */
    if (G_projection() == PROJECTION_LL)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
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
        G_fatal_error(_("Lat/Long project is not supported by %s. Please "
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
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
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
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
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        G_fatal_error(_("Lat/Long location is not supported by %s. Please "
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                        "reproject map first."),
                      G_program_name());

    input = params.input->answer;
    output = params.output->answer;

    G_get_window(&window);

    read_cells();
    initialize();
    calculate_atanb();
    write_cells();

    exit(EXIT_SUCCESS);
}
