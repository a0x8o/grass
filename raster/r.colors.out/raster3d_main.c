/****************************************************************************
 *
 * MODULE:       r3.colors.out
 *
 * AUTHOR(S):    Glynn Clements
 *
 * PURPOSE:      Allows export of the color table for a 3D raster map.
 *
 * COPYRIGHT:    (C) 2008, 2010-2011 Glynn Clements and the GRASS Development
 *               Team
 *
 *               This program is free software under the GNU General
 *               Public License (>=v2). Read the file COPYING that
 *               comes with GRASS for details.
 *
 ***************************************************************************/

#include <stdlib.h>
#include <string.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/raster3d.h>
#include <grass/glocale.h>
#include <grass/parson.h>

#include "local_proto.h"

/* Run in raster3d mode */
int main(int argc, char **argv)
{
    struct GModule *module;
    struct {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
        struct Option *map, *file, *format, *color_format;
=======
        struct Option *map, *file;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        struct Option *map, *file;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        struct Option *map, *file, *format, *color_format;
>>>>>>> 6bac3385ba (r.colors.out: Add JSON support (#4555))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        struct Option *map, *file;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    } opt;
    struct {
        struct Flag *p;
    } flag;

    const char *file;
    FILE *fp;
    struct Colors colors;
    struct FPRange range;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    enum ColorFormat clr_frmt;

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    enum ColorFormat clr_frmt;

>>>>>>> 6bac3385ba (r.colors.out: Add JSON support (#4555))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    G_gisinit(argv[0]);

    module = G_define_module();
    G_add_keyword(_("raster3d"));
    G_add_keyword(_("color table"));
    G_add_keyword(_("export"));
    module->description =
        _("Exports the color table associated with a 3D raster map.");

    opt.map = G_define_standard_option(G_OPT_R3_MAP);

    opt.file = G_define_standard_option(G_OPT_F_OUTPUT);
    opt.file->key = "rules";
    opt.file->label = _("Path to output rules file");
    opt.file->description = _("If not given write to standard output");
    opt.file->required = NO;

    opt.format = G_define_standard_option(G_OPT_F_FORMAT);
    opt.format->guisection = _("Print");

    opt.color_format = G_define_standard_option(G_OPT_C_FORMAT);
    opt.color_format->guisection = _("Color");

    flag.p = G_define_flag();
    flag.p->key = 'p';
    flag.p->description = _("Output values as percentages");

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    file = opt.file->answer;

    if (Rast3d_read_colors(opt.map->answer, "", &colors) < 0)
        G_fatal_error(_("Unable to read color table for raster3d map <%s>"),
                      opt.map->answer);

    Rast3d_read_range(opt.map->answer, "", &range);

    if (!file || strcmp(file, "-") == 0)
        fp = stdout;
    else {
        fp = fopen(file, "w");
        if (!fp)
            G_fatal_error(_("Unable to open output file <%s>"), file);
    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6bac3385ba (r.colors.out: Add JSON support (#4555))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    if (strcmp(opt.format->answer, "json") == 0) {
        if (strcmp(opt.color_format->answer, "rgb") == 0) {
            clr_frmt = RGB;
        }
        else if (strcmp(opt.color_format->answer, "triplet") == 0) {
            clr_frmt = TRIPLET;
        }
        else if (strcmp(opt.color_format->answer, "hsv") == 0) {
            clr_frmt = HSV;
        }
        else {
            clr_frmt = HEX;
        }
        print_json_colors(&colors, range.min, range.max, fp,
                          flag.p->answer ? 1 : 0, clr_frmt);
    }
    else {
        Rast_print_colors(&colors, range.min, range.max, fp,
                          flag.p->answer ? 1 : 0);
    }
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
    Rast_print_colors(&colors, range.min, range.max, fp,
                      flag.p->answer ? 1 : 0);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    Rast_print_colors(&colors, range.min, range.max, fp,
                      flag.p->answer ? 1 : 0);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 6bac3385ba (r.colors.out: Add JSON support (#4555))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    exit(EXIT_SUCCESS);
}
