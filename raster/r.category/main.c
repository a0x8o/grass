/****************************************************************************
 *
 * MODULE:       r.category (formerly r.cats)
 *
 * AUTHOR(S):    Michael Shapiro - CERL
 *                 Hamish Bowman, Dunedin, New Zealand  (label creation opts)
 *
 * PURPOSE:      Prints category values and labels associated with
 *                 user-specified raster map layers.
 *
 * COPYRIGHT:    (C) 2006-2019 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 ***************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>
#include <grass/parson.h>
#include "local_proto.h"

static struct Categories cats;
static char *fs;

int main(int argc, char *argv[])
{
    const char *name;
    const char *mapset;

    long x, y;
    double dx;
    RASTER_MAP_TYPE map_type;
    int i;
    int from_stdin = FALSE;
    struct GModule *module;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    enum OutputFormat format;
    JSON_Value *root_value;
    JSON_Array *root_array;

    struct {
        struct Option *map, *fs, *cats, *vals, *raster, *file, *fmt_str,
            *fmt_coeff, *format;
=======
    struct {
        struct Option *map, *fs, *cats, *vals, *raster, *file, *fmt_str,
            *fmt_coeff;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    struct {
        struct Option *map, *fs, *cats, *vals, *raster, *file, *fmt_str,
            *fmt_coeff;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    } parm;

    G_gisinit(argv[0]);

    module = G_define_module();
    G_add_keyword(_("raster"));
    G_add_keyword(_("category"));
    module->description = _("Manages category values and labels associated "
                            "with user-specified raster map layers.");

    parm.map = G_define_standard_option(G_OPT_R_MAP);

    parm.cats = G_define_standard_option(G_OPT_V_CATS);
    parm.cats->multiple = YES;
    parm.cats->guisection = _("Selection");

    parm.vals = G_define_option();
    parm.vals->key = "values";
    parm.vals->type = TYPE_DOUBLE;
    parm.vals->multiple = YES;
    parm.vals->required = NO;
    parm.vals->label = _("Comma separated value list");
    parm.vals->description = _("Example: 1.4,3.8,13");
    parm.vals->guisection = _("Selection");

    parm.fs = G_define_standard_option(G_OPT_F_SEP);
    parm.fs->answer = "tab";

    parm.raster = G_define_standard_option(G_OPT_R_INPUT);
    parm.raster->key = "raster";
    parm.raster->required = NO;
    parm.raster->description =
        _("Raster map from which to copy category table");
    parm.raster->guisection = _("Define");

    parm.file = G_define_standard_option(G_OPT_F_INPUT);
    parm.file->key = "rules";
    parm.file->required = NO;
    parm.file->description =
        _("File containing category label rules (or \"-\" to read from stdin)");
    parm.file->guisection = _("Define");

    parm.fmt_str = G_define_option();
    parm.fmt_str->key = "format";
    parm.fmt_str->type = TYPE_STRING;
    parm.fmt_str->required = NO;
    parm.fmt_str->label =
        _("Default label or format string for dynamic labeling");
    parm.fmt_str->description =
        _("Used when no explicit label exists for the category");

    parm.fmt_coeff = G_define_option();
    parm.fmt_coeff->key = "coefficients";
    parm.fmt_coeff->type = TYPE_DOUBLE;
    parm.fmt_coeff->required = NO;
    parm.fmt_coeff->key_desc = "mult1,offset1,mult2,offset2";
    /*    parm.fmt_coeff->answer   = "0.0,0.0,0.0,0.0"; */
    parm.fmt_coeff->label = _("Dynamic label coefficients");
    parm.fmt_coeff->description =
        _("Two pairs of category multiplier and offsets, for $1 and $2");
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    parm.format = G_define_standard_option(G_OPT_F_FORMAT);
    parm.format->key = "output_format";
    parm.format->guisection = _("Print");

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    if (strcmp(parm.format->answer, "json") == 0) {
        format = JSON;
        root_value = json_value_init_array();
        if (root_value == NULL) {
            G_fatal_error(_("Failed to initialize JSON array. Out of memory?"));
        }
        root_array = json_array(root_value);
    }
    else {
        format = PLAIN;
    }
=======

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    name = parm.map->answer;

    fs = G_option_to_separator(parm.fs);

    mapset = G_find_raster2(name, "");
    if (mapset == NULL)
        G_fatal_error(_("Raster map <%s> not found"), name);

    map_type = Rast_map_type(name, mapset);

    /* create category labels */
    if (parm.raster->answer || parm.file->answer || parm.fmt_str->answer ||
        parm.fmt_coeff->answer) {

        /* restrict editing to current mapset */
        if (strcmp(mapset, G_mapset()) != 0)
            G_fatal_error(_("Raster map <%s> not found in current mapset"),
                          name);

        /* use cats from another map */
        if (parm.raster->answer) {
            int fd;
            const char *cmapset;

            cmapset = G_find_raster2(parm.raster->answer, "");
            if (cmapset == NULL)
                G_fatal_error(_("Raster map <%s> not found"),
                              parm.raster->answer);

            fd = Rast_open_old(name, mapset);

            Rast_init_cats("", &cats);

            if (0 > Rast_read_cats(parm.raster->answer, cmapset, &cats))
                G_fatal_error(
                    _("Unable to read category file of raster map <%s@%s>"),
                    parm.raster->answer, cmapset);

            Rast_write_cats(name, &cats);
            G_message(_("Category table for <%s> set from <%s>"), name,
                      parm.raster->answer);

            Rast_close(fd);
        }

        /* load cats from rules file */
        if (parm.file->answer) {
            FILE *fp;
            char **tokens;
            int ntokens;
            char *e1;
            char *e2;

            if (strcmp("-", parm.file->answer) == 0) {
                from_stdin = TRUE;
                fp = stdin;
            }
            else {
                fp = fopen(parm.file->answer, "r");
                if (!fp)
                    G_fatal_error(_("Unable to open file <%s>"),
                                  parm.file->answer);
            }

            Rast_init_cats("", &cats);

            for (;;) {
                char buf[1024];
                DCELL d1, d2;
                int parse_error = 0;

                if (!G_getl2(buf, sizeof(buf), fp))
                    break;

                G_debug(1, "rule input (separator: <%s>): <%s>", fs, buf);
                tokens = G_tokenize(buf, fs);
                ntokens = G_number_of_tokens(tokens);
                G_debug(1, "tokens found: <%d>", ntokens);

                if (ntokens == 3) {
                    d1 = strtod(tokens[0], &e1);
                    d2 = strtod(tokens[1], &e2);
                    G_debug(
                        1,
                        "d1: <%f>, d2: <%f>, tokens[0]: <%s>, tokens[1]: <%s>",
                        d1, d2, tokens[0], tokens[1]);
                    if (*e1 == 0 && *e2 == 0)
                        Rast_set_d_cat(&d1, &d2, tokens[2], &cats);
                    else
                        parse_error = 1;
                }
                else if (ntokens == 2) {
                    d1 = strtod(tokens[0], &e1);
                    G_debug(1, "d1: <%f>, tokens[0]: <%s>, tokens[1]: <%s>", d1,
                            tokens[0], tokens[1]);
                    if (*e1 == 0)
                        Rast_set_d_cat(&d1, &d1, tokens[1], &cats);
                    else
                        parse_error = 1;
                }
                else if (!strlen(buf))
                    continue;
                else
                    parse_error = 1;

                if (parse_error)
                    G_fatal_error(_("Incorrect format of input rules. "
                                    "Is the first column numeric? Or check "
                                    "separators. Invalid line is:\n%s"),
                                  buf);
            }
            G_free_tokens(tokens);
            Rast_write_cats(name, &cats);

            if (!from_stdin)
                fclose(fp);
        }

        /* set dynamic cat rules for cats without explicit labels */
        if (parm.fmt_str->answer || parm.fmt_coeff->answer) {
            char *fmt_str;
            double m1, a1, m2, a2;

            /* read existing values */
            Rast_init_cats("", &cats);

            if (0 > Rast_read_cats(name, G_mapset(), &cats))
                G_warning(
                    _("Unable to read category file of raster map <%s@%s>"),
                    name, G_mapset());

            if (parm.fmt_str->answer) {
                fmt_str =
                    G_malloc(strlen(parm.fmt_str->answer) > strlen(cats.fmt)
                                 ? strlen(parm.fmt_str->answer) + 1
                                 : strlen(cats.fmt) + 1);
                strcpy(fmt_str, parm.fmt_str->answer);
            }
            else {
                fmt_str = G_malloc(strlen(cats.fmt) + 1);
                strcpy(fmt_str, cats.fmt);
            }

            m1 = cats.m1;
            a1 = cats.a1;
            m2 = cats.m2;
            a2 = cats.a2;

            if (parm.fmt_coeff->answer) {
                m1 = atof(parm.fmt_coeff->answers[0]);
                a1 = atof(parm.fmt_coeff->answers[1]);
                m2 = atof(parm.fmt_coeff->answers[2]);
                a2 = atof(parm.fmt_coeff->answers[3]);
            }

            Rast_set_cats_fmt(fmt_str, m1, a1, m2, a2, &cats);

            Rast_write_cats(name, &cats);
        }

        Rast_free_cats(&cats);
        exit(EXIT_SUCCESS);
    }
    else {
        if (Rast_read_cats(name, mapset, &cats) < 0)
            G_fatal_error(
                _("Unable to read category file of raster map <%s> in <%s>"),
                name, mapset);
    }

    /* describe the category labels */
    /* if no cats requested, use r.describe to get the cats */
    if (parm.cats->answer == NULL) {
        if (map_type == CELL_TYPE) {
            get_cats(name, mapset);
            while (next_cat(&x))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
                print_label(x, format, root_array);
            if (format == JSON) {
                print_json(root_value);
            }
=======
                print_label(x);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
                print_label(x);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
                print_label(x);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
            exit(EXIT_SUCCESS);
        }
    }
    else {
        if (map_type != CELL_TYPE)
            G_warning(_("The map is floating point! Ignoring cats list, using "
                        "values list"));
        else { /* integer map */

            for (i = 0; parm.cats->answers[i]; i++)
                if (!scan_cats(parm.cats->answers[i], &x, &y)) {
                    G_usage();
                    exit(EXIT_FAILURE);
                }
            for (i = 0; parm.cats->answers[i]; i++) {
                scan_cats(parm.cats->answers[i], &x, &y);
                while (x <= y)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
                    print_label(x++, format, root_array);
            }
            if (format == JSON) {
                print_json(root_value);
=======
                    print_label(x++);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
                    print_label(x++);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
                    print_label(x++);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
            }
            exit(EXIT_SUCCESS);
        }
    }
    if (parm.vals->answer == NULL)
        G_fatal_error(
            _("Parameter 'values' is required for floating point map!"));
    for (i = 0; parm.vals->answers[i]; i++)
        if (!scan_vals(parm.vals->answers[i], &dx)) {
            G_usage();
            exit(EXIT_FAILURE);
        }
    for (i = 0; parm.vals->answers[i]; i++) {
        scan_vals(parm.vals->answers[i], &dx);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
        print_d_label(dx, format, root_array);
=======
        print_d_label(dx);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        print_d_label(dx);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        print_d_label(dx);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    }

    if (format == JSON) {
        print_json(root_value);
    }

    exit(EXIT_SUCCESS);
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
void print_json(JSON_Value *root_value)
{
    char *serialized_string = NULL;
    serialized_string = json_serialize_to_string_pretty(root_value);
    if (serialized_string == NULL) {
        G_fatal_error(_("Failed to initialize pretty JSON string."));
    }
    puts(serialized_string);
    json_free_serialized_string(serialized_string);
    json_value_free(root_value);
}

int print_label(long x, enum OutputFormat format, JSON_Array *root_array)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
int print_label(long x)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
{
    char *label;
    JSON_Value *category_value;
    JSON_Object *category;

    G_squeeze(label = Rast_get_c_cat((CELL *)&x, &cats));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    switch (format) {
    case PLAIN:
        fprintf(stdout, "%ld%s%s\n", x, fs, label);
        break;
    case JSON:
        category_value = json_value_init_object();
        category = json_object(category_value);
        json_object_set_number(category, "category", x);
        json_object_set_string(category, "description", label);
        json_array_append_value(root_array, category_value);
        break;
    }
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    fprintf(stdout, "%ld%s%s\n", x, fs, label);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    return 0;
}

int print_d_label(double x, enum OutputFormat format, JSON_Array *root_array)
{
    char *label, tmp[40];
    DCELL dtmp;
    JSON_Value *category_value;
    JSON_Object *category;

    dtmp = x;
    G_squeeze(label = Rast_get_d_cat(&dtmp, &cats));

    switch (format) {
    case PLAIN:
        sprintf(tmp, "%.10f", x);
        G_trim_decimal(tmp);
        fprintf(stdout, "%s%s%s\n", tmp, fs, label);
        break;
    case JSON:
        category_value = json_value_init_object();
        category = json_object(category_value);
        json_object_set_number(category, "category", x);
        json_object_set_string(category, "description", label);
        json_array_append_value(root_array, category_value);
        break;
    }

    return 0;
}

int scan_cats(const char *s, long *x, long *y)
{
    char dummy[2];

    *dummy = 0;
    if (sscanf(s, "%ld-%ld%1s", x, y, dummy) == 2)
        return (*dummy == 0 && *x <= *y);
    *dummy = 0;
    if (sscanf(s, "%ld%1s", x, dummy) == 1 && *dummy == 0) {
        *y = *x;
        return 1;
    }
    return 0;
}

int scan_vals(const char *s, double *x)
{
    char dummy[10];

    *dummy = 0;
    if (sscanf(s, "%lf%1s", x, dummy) == 1 && *dummy == 0)
        return 1;
    return 0;
}
