/*
 * Copyright (C) 2000 by the GRASS Development Team
 * Author: Bob Covill <bcovill@tekmap.ns.ca>
 *
 * This Program is free software under the GPL (>=v2)
 * Read the file COPYING coming with GRASS for details
 *
 */

#include <stdlib.h>
#include <grass/parson.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>

#include "local_proto.h"

int clr;
struct Colors colors;

static double dist, e, n;

int main(int argc, char *argv[])
{
    char *name, *outfile;
    const char *unit;
    int unit_id;
    double factor;
    int fd, projection;
    FILE *fp, *coor_fp;
    double res;
    char *null_string;
    char ebuf[256], nbuf[256], label[512], formatbuff[256];
    char b1[100], b2[100];
    int n;
    int havefirst = FALSE;
    int coords = 0, i, k = -1;
    double e1, e2, n1, n2;
    RASTER_MAP_TYPE data_type;
    struct Cell_head window;
    struct {
        struct Option *opt1, *profile, *res, *output, *null_str, *coord_file,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            *units, *format;
=======
            *units;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            *units;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            *units, *format;
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
        struct Flag *g, *c, *m;
    } parm;
    struct GModule *module;
    enum OutputFormat format;
    JSON_Value *array_value;
    JSON_Array *array;

    G_gisinit(argv[0]);

    /* Set description */
    module = G_define_module();
    G_add_keyword(_("raster"));
    G_add_keyword(_("profile"));
    G_add_keyword(_("transect"));
    module->description =
        _("Outputs the raster map layer values lying on user-defined line(s).");

    parm.opt1 = G_define_standard_option(G_OPT_R_INPUT);

    parm.output = G_define_standard_option(G_OPT_F_OUTPUT);
    parm.output->required = NO;
    parm.output->answer = "-";
    parm.output->description =
        _("Name of file for output (use output=- for stdout)");

    parm.profile = G_define_standard_option(G_OPT_M_COORDS);
    parm.profile->required = NO;
    parm.profile->multiple = YES;
    parm.profile->description = _("Profile coordinate pairs");

    parm.coord_file = G_define_standard_option(G_OPT_F_INPUT);
    parm.coord_file->key = "file";
    parm.coord_file->required = NO;
    parm.coord_file->label =
        _("Name of input file containing coordinate pairs");
    parm.coord_file->description = _("Use instead of the 'coordinates' option. "
                                     "\"-\" reads from stdin.");

    parm.res = G_define_option();
    parm.res->key = "resolution";
    parm.res->type = TYPE_DOUBLE;
    parm.res->required = NO;
    parm.res->description =
        _("Resolution along profile (default = current region resolution)");

    parm.null_str = G_define_standard_option(G_OPT_M_NULL_VALUE);
    parm.null_str->answer = "*";

    parm.g = G_define_flag();
    parm.g->key = 'g';
    parm.g->description = _("Output easting and northing in first two columns "
                            "of four column output");

    parm.c = G_define_flag();
    parm.c->key = 'c';
    parm.c->description =
        _("Output RRR:GGG:BBB color values for each profile point");

    parm.units = G_define_standard_option(G_OPT_M_UNITS);
    parm.units->options = "meters,kilometers,feet,miles";
    parm.units->label = parm.units->description;
    parm.units->description =
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        _("If units are not specified, current location units are used. "
          "Meters are used by default in geographic (latlon) locations.");
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
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
        _("If units are not specified, current location units are used. "
          "Meters are used by default in geographic (latlon) locations.");
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
        _("If units are not specified, current project units are used. "
          "Meters are used by default in geographic (latlon) projects.");
=======
        _("If units are not specified, current location units are used. "
          "Meters are used by default in geographic (latlon) locations.");
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
        _("If units are not specified, current location units are used. "
          "Meters are used by default in geographic (latlon) locations.");
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

    parm.format = G_define_standard_option(G_OPT_F_FORMAT);
    parm.units->guisection = _("Print");
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))

    parm.format = G_define_standard_option(G_OPT_F_FORMAT);
    parm.units->guisection = _("Print");
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
        _("If units are not specified, current location units are used. "
          "Meters are used by default in geographic (latlon) locations.");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
        _("If units are not specified, current location units are used. "
          "Meters are used by default in geographic (latlon) locations.");
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))

    parm.format = G_define_standard_option(G_OPT_F_FORMAT);
    parm.units->guisection = _("Print");
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    clr = 0;
    if (parm.c->answer)
        clr = 1; /* color output */

    null_string = parm.null_str->answer;

    if ((parm.profile->answer && parm.coord_file->answer) ||
        (!parm.profile->answer && !parm.coord_file->answer))
        G_fatal_error(_("Either use profile option or coordinate_file "
                        " option, but not both"));

    G_get_window(&window);
    projection = G_projection();

    /* get conversion factor and units name */
    if (parm.units->answer) {
        unit_id = G_units(parm.units->answer);
        factor = 1. / G_meters_to_units_factor(unit_id);
        unit = G_get_units_name(unit_id, 1, 0);
    }
    /* keep meters in case of latlon */
    else if (projection == PROJECTION_LL) {
        factor = 1;
        unit = "meters";
    }
    else {
        /* get conversion factor to current units */
        unit = G_database_unit_name(1);
        factor = G_database_units_to_meters_factor();
    }

    if (parm.res->answer) {
        res = atof(parm.res->answer);
        /* Catch bad resolution ? */
        if (res <= 0)
            G_fatal_error(_("Illegal resolution %g [%s]"), res / factor, unit);
    }
    else {
        /* Do average of EW and NS res */
        res = (window.ew_res + window.ns_res) / 2;
<<<<<<< HEAD
<<<<<<< HEAD
    }

    if (strcmp(parm.format->answer, "json") == 0) {
        format = JSON;
        array_value = json_value_init_array();
        array = json_array(array_value);
    }
    else {
        format = PLAIN;
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    }

    if (strcmp(parm.format->answer, "json") == 0) {
        format = JSON;
        array_value = json_value_init_array();
        array = json_array(array_value);
    }
    else {
        format = PLAIN;
    }

    G_message(_("Using resolution: %g [%s]"), res / factor, unit);

    G_begin_distance_calculations();

    /* Open Input File for reading */
    /* Get Input Name */
    name = parm.opt1->answer;
    if (parm.g->answer)
        coords = 1;

    /* Open Raster File */
    fd = Rast_open_old(name, "");

    /* initialize color structure */
    if (clr)
        Rast_read_colors(name, "", &colors);

    /* Open ASCII file for output or stdout */
    outfile = parm.output->answer;

    if ((strcmp("-", outfile)) == 0) {
        fp = stdout;
    }
    else if (NULL == (fp = fopen(outfile, "w")))
        G_fatal_error(_("Unable to open file <%s>"), outfile);

    /* Get Raster Type */
    data_type = Rast_get_map_type(fd);
    /* Done with file */

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
    if (format == PLAIN) {
        /* Show message giving output format */
        G_message(_("Output columns:"));
        if (coords == 1)
            sprintf(formatbuff,
                    _("Easting, Northing, Along track dist. [%s], Elevation"),
                    unit);
        else
            sprintf(formatbuff, _("Along track dist. [%s], Elevation"), unit);
        if (clr)
            strcat(formatbuff, _(" RGB color"));
        G_message("%s", formatbuff);
    }
<<<<<<< HEAD
=======
    /* Show message giving output format */
    G_message(_("Output columns:"));
    if (coords == 1)
        sprintf(formatbuff,
                _("Easting, Northing, Along track dist. [%s], Elevation"),
                unit);
    else
        sprintf(formatbuff, _("Along track dist. [%s], Elevation"), unit);
    if (clr)
        strcat(formatbuff, _(" RGB color"));
    G_message("%s", formatbuff);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))

    /* Get Profile Start Coords */
    if (parm.coord_file->answer) {
        if (strcmp("-", parm.coord_file->answer) == 0)
            coor_fp = stdin;
        else
            coor_fp = fopen(parm.coord_file->answer, "r");

        if (coor_fp == NULL)
            G_fatal_error(_("Could not open <%s>"), parm.coord_file->answer);

        for (n = 1; input(b1, ebuf, b2, nbuf, label, coor_fp); n++) {
            G_debug(4, "stdin line %d: ebuf=[%s]  nbuf=[%s]", n, ebuf, nbuf);
            if (!G_scan_easting(ebuf, &e2, G_projection()) ||
                !G_scan_northing(nbuf, &n2, G_projection()))
                G_fatal_error(_("Invalid coordinates %s %s"), ebuf, nbuf);

            if (havefirst)
                do_profile(e1, e2, n1, n2, coords, res, fd, data_type, fp,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                           null_string, unit, factor, format, name, array);
=======
                           null_string, unit, factor);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                           null_string, unit, factor);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                           null_string, unit, factor, format, name, array);
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
            e1 = e2;
            n1 = n2;
            havefirst = TRUE;
        }

        if (coor_fp != stdin)
            fclose(coor_fp);
    }
    else {
        /* Coords given on the Command Line using the profile= option */
        for (i = 0; parm.profile->answers[i]; i += 2) {
            /* Test for number coordinate pairs */
            k = i;
        }

        if (k == 0) {
            /* Only one coordinate pair supplied */
            G_scan_easting(parm.profile->answers[0], &e1, G_projection());
            G_scan_northing(parm.profile->answers[1], &n1, G_projection());
            e2 = e1;
            n2 = n1;

            /* Get profile info */
            do_profile(e1, e2, n1, n2, coords, res, fd, data_type, fp,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                       null_string, unit, factor, format, name, array);
=======
                       null_string, unit, factor);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                       null_string, unit, factor);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                       null_string, unit, factor, format, name, array);
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
        }
        else {
            for (i = 0; i <= k - 2; i += 2) {
                G_scan_easting(parm.profile->answers[i], &e1, G_projection());
                G_scan_northing(parm.profile->answers[i + 1], &n1,
                                G_projection());
                G_scan_easting(parm.profile->answers[i + 2], &e2,
                               G_projection());
                G_scan_northing(parm.profile->answers[i + 3], &n2,
                                G_projection());

                /* Get profile info */
                do_profile(e1, e2, n1, n2, coords, res, fd, data_type, fp,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                           null_string, unit, factor, format, name, array);
            }
        }
    }

    if (format == JSON) {
        char *serialized_string = json_serialize_to_string_pretty(array_value);
        if (serialized_string == NULL) {
            G_fatal_error(_("Failed to initialize pretty JSON string."));
        }
        puts(serialized_string);
        json_free_serialized_string(serialized_string);
        json_value_free(array_value);
=======
                           null_string, unit, factor);
=======
                           null_string, unit, factor, format, name, array);
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
            }
        }
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                           null_string, unit, factor);
            }
        }
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    }

    if (format == JSON) {
        char *serialized_string = json_serialize_to_string_pretty(array_value);
        if (serialized_string == NULL) {
            G_fatal_error(_("Failed to initialize pretty JSON string."));
        }
        puts(serialized_string);
        json_free_serialized_string(serialized_string);
        json_value_free(array_value);
    }

    Rast_close(fd);
    fclose(fp);

    if (clr)
        Rast_free_colors(&colors);

    exit(EXIT_SUCCESS);
} /* Done with main */

/* Calculate the Profile Now */
/* Establish parameters */
int do_profile(double e1, double e2, double n1, double n2, int coords,
               double res, int fd, int data_type, FILE *fp, char *null_string,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
               const char *unit, double factor, enum OutputFormat format,
               char *name, JSON_Array *array)
=======
               const char *unit, double factor)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
               const char *unit, double factor)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
               const char *unit, double factor, enum OutputFormat format,
               char *name, JSON_Array *array)
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
{
    double rows, cols, LEN;
    double Y, X, k;

    cols = e1 - e2;
    rows = n1 - n2;

    LEN = G_distance(e1, n1, e2, n2);
    G_message(_("Approx. transect length: %f [%s]"), LEN / factor, unit);

    if (!G_point_in_region(e2, n2))
        G_warning(
            _("Endpoint coordinates are outside of current region settings"));

    /* Calculate Azimuth of Line */
    if (rows == 0 && cols == 0) {
        /* Special case for no movement */
        e = e1;
        n = n1;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        read_rast(e, n, dist / factor, fd, coords, data_type, fp, null_string,
                  format, name, array);
=======
        read_rast(e, n, dist / factor, fd, coords, data_type, fp, null_string);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        read_rast(e, n, dist / factor, fd, coords, data_type, fp, null_string);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        read_rast(e, n, dist / factor, fd, coords, data_type, fp, null_string,
                  format, name, array);
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
    }

    k = res / hypot(rows, cols);
    Y = k * rows;
    X = k * cols;
    if (Y < 0)
        Y = Y * -1.;
    if (X < 0)
        X = X * -1.;

    if (e != 0.0 && (e != e1 || n != n1)) {
        dist -= G_distance(e, n, e1, n1);
    }

    if (rows >= 0 && cols < 0) {
        /* SE Quad or due east */
        for (e = e1, n = n1; e < e2 || n > n2; e += X, n -= Y) {
            read_rast(e, n, dist / factor, fd, coords, data_type, fp,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                      null_string, format, name, array);
=======
                      null_string);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                      null_string);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                      null_string, format, name, array);
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
            /* d+=res; */
            dist += G_distance(e - X, n + Y, e, n);
        }
    }

    if (rows < 0 && cols <= 0) {
        /* NE Quad  or due north */
        for (e = e1, n = n1; e < e2 || n < n2; e += X, n += Y) {
            read_rast(e, n, dist / factor, fd, coords, data_type, fp,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                      null_string, format, name, array);
=======
                      null_string);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                      null_string);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                      null_string, format, name, array);
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
            /* d+=res; */
            dist += G_distance(e - X, n - Y, e, n);
        }
    }

    if (rows > 0 && cols >= 0) {
        /* SW Quad or due south */
        for (e = e1, n = n1; e > e2 || n > n2; e -= X, n -= Y) {
            read_rast(e, n, dist / factor, fd, coords, data_type, fp,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                      null_string, format, name, array);
=======
                      null_string);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                      null_string);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                      null_string, format, name, array);
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
            /* d+=res; */
            dist += G_distance(e + X, n + Y, e, n);
        }
    }

    if (rows <= 0 && cols > 0) {
        /* NW Quad  or due west */
        for (e = e1, n = n1; e > e2 || n < n2; e -= X, n += Y) {
            read_rast(e, n, dist / factor, fd, coords, data_type, fp,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                      null_string, format, name, array);
=======
                      null_string);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                      null_string);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                      null_string, format, name, array);
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
            /* d+=res; */
            dist += G_distance(e + X, n - Y, e, n);
        }
    }
    /*
     * return dist;
     */
    return 0;
} /* done with do_profile */
