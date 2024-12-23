/****************************************************************************
 *
 * MODULE:       r.texture
 * AUTHOR(S):    Carmine Basco - basco@unisannio.it
 *               with hints from:
 *                         prof. Giulio Antoniol - antoniol@ieee.org
 *                         prof. Michele Ceccarelli - ceccarelli@unisannio.it
 *               Markus Metz (optimization and bug fixes)
 *
 * PURPOSE:      Create map raster with textural features.
 *
 * COPYRIGHT:    (C) 2003 by University of Sannio (BN), Benevento, Italy
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 * Permission to use, copy, modify, and distribute this software and its
 * documentation for any purpose and without fee is hereby granted. This
 * software is provided "as is" without express or implied warranty.
 *
 *****************************************************************************/
#if defined(_OPENMP)
#include <omp.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
#include "execute.h"

/* modify this table to add new measures */
static struct menu measure_menu[] = {
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
struct menu {
    char *name;   /* measure name */
    char *desc;   /* menu display - full description */
    char *suffix; /* output suffix */
    char useme;   /* calculate this measure if set */
    int idx;      /* measure index */
};

/* modify this table to add new measures */
static struct menu menu[] = {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
#include "execute.h"

/* modify this table to add new measures */
static struct menu measure_menu[] = {
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    {"asm", "Angular Second Moment", "_ASM", 0, 1},
    {"contrast", "Contrast", "_Contr", 0, 2},
    {"corr", "Correlation", "_Corr", 0, 3},
    {"var", "Variance", "_Var", 0, 4},
    {"idm", "Inverse Diff Moment", "_IDM", 0, 5},
    {"sa", "Sum Average", "_SA", 0, 6},
    {"sv", "Sum Variance", "_SV", 0, 7},
    {"se", "Sum Entropy", "_SE", 0, 8},
    {"entr", "Entropy", "_Entr", 0, 9},
    {"dv", "Difference Variance", "_DV", 0, 10},
    {"de", "Difference Entropy", "_DE", 0, 11},
    {"moc1", "Measure of Correlation-1", "_MOC-1", 0, 12},
    {"moc2", "Measure of Correlation-2", "_MOC-2", 0, 13},
    {NULL, NULL, NULL, 0, -1}};

static int find_measure(const char *measure_name)
{
    int i;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    for (i = 0; measure_menu[i].name; i++)
        if (strcmp(measure_menu[i].name, measure_name) == 0)
=======
    for (i = 0; menu[i].name; i++)
        if (strcmp(menu[i].name, measure_name) == 0)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    for (i = 0; measure_menu[i].name; i++)
        if (strcmp(measure_menu[i].name, measure_name) == 0)
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
            return i;

    G_fatal_error(_("Unknown measure <%s>"), measure_name);

    return -1;
}

int main(int argc, char *argv[])
{
    struct Cell_head cellhd;
    char *name, *result;
    char **mapname;
    int *measure_idx, overwrite;
    int i, j;
    CELL **data; /* Data structure containing image */
    DCELL *dcell_row;
    struct FPRange range;
    DCELL min, max, inscale;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    FCELL measure;  /* Containing measure done */
    int dist, size; /* dist = value of distance, size = s. of moving window */
    int offset;
    int have_px, have_py, have_pxpys, have_pxpyd;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    int infd, *outfd;

    RASTER_MAP_TYPE out_data_type;
    struct GModule *module;
    struct {
        struct Option *input, *output, *size, *dist, *measure, *nproc;
    } parm;
    struct {
        struct Flag *ind, *all, *null;
    } flag;
    struct History history;

    struct dimensions dim;
    struct output_setting out_set;
    char p[1024];
    int threads;

    G_gisinit(argv[0]);

    module = G_define_module();
    G_add_keyword(_("raster"));
    G_add_keyword(_("algebra"));
    G_add_keyword(_("statistics"));
    G_add_keyword(_("texture"));
    G_add_keyword(_("parallel"));
    module->description =
        _("Generate images with textural features from a raster map.");

    /* Define the different options */

    parm.input = G_define_standard_option(G_OPT_R_INPUT);

    parm.output = G_define_standard_option(G_OPT_R_BASENAME_OUTPUT);

    parm.nproc = G_define_standard_option(G_OPT_M_NPROCS);
<<<<<<< HEAD
=======

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    parm.size = G_define_option();
    parm.size->key = "size";
    parm.size->key_desc = "value";
    parm.size->type = TYPE_INTEGER;
    parm.size->required = NO;
    parm.size->description = _("The size of moving window (odd and >= 3)");
    parm.size->answer = "3";
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))

<<<<<<< HEAD
<<<<<<< HEAD
    parm.size = G_define_option();
    parm.size->key = "size";
    parm.size->key_desc = "value";
    parm.size->type = TYPE_INTEGER;
    parm.size->required = NO;
    parm.size->description = _("The size of moving window (odd and >= 3)");
    parm.size->answer = "3";

    /* Textural character is in direct relation of the spatial size of the
     * texture primitives. */

    parm.dist = G_define_option();
    parm.dist->key = "distance";
    parm.dist->key_desc = "value";
    parm.dist->type = TYPE_INTEGER;
    parm.dist->required = NO;
    parm.dist->label = _("The distance between two samples (>= 1)");
    parm.dist->description =
        _("The distance must be smaller than the size of the moving window");
    parm.dist->answer = "1";

    for (i = 0; measure_menu[i].name; i++) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    /* Textural character is in direct relation of the spatial size of the
     * texture primitives. */

    parm.dist = G_define_option();
    parm.dist->key = "distance";
    parm.dist->key_desc = "value";
    parm.dist->type = TYPE_INTEGER;
    parm.dist->required = NO;
    parm.dist->label = _("The distance between two samples (>= 1)");
    parm.dist->description =
<<<<<<< HEAD
        _("The distance must be smaller than the size of the moving window");
    parm.dist->answer = "1";

<<<<<<< HEAD
    for (i = 0; menu[i].name; i++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    for (i = 0; measure_menu[i].name; i++) {
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    /* Textural character is in direct relation of the spatial size of the
     * texture primitives. */

    opt_dist = G_define_option();
    opt_dist->key = "distance";
    opt_dist->key_desc = "value";
    opt_dist->type = TYPE_INTEGER;
    opt_dist->required = NO;
    opt_dist->label = _("The distance between two samples (>= 1)");
    opt_dist->description =
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
        _("The distance must be smaller than the size of the moving window");
    parm.dist->answer = "1";

<<<<<<< HEAD
    for (i = 0; menu[i].name; i++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    for (i = 0; measure_menu[i].name; i++) {
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
        if (i)
            strcat(p, ",");
        else
            *p = 0;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
        strcat(p, measure_menu[i].name);
=======
        strcat(p, menu[i].name);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        strcat(p, menu[i].name);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        strcat(p, measure_menu[i].name);
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        strcat(p, menu[i].name);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    }
    parm.measure = G_define_option();
    parm.measure->key = "method";
    parm.measure->type = TYPE_STRING;
    parm.measure->required = NO;
    parm.measure->multiple = YES;
    parm.measure->options = p;
    parm.measure->description = _("Textural measurement method");

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    flag.ind = G_define_flag();
    flag.ind->key = 's';
    flag.ind->label = _("Separate output for each angle (0, 45, 90, 135)");
    flag.ind->description =
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
=======
    flag_ind = G_define_flag();
    flag_ind->key = 's';
    flag_ind->label = _("Separate output for each angle (0, 45, 90, 135)");
    flag_ind->description =
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
        _("Angles are counterclockwise from east: "
          "0 is East to West, 45 is North-East to South-West");

    flag.all = G_define_flag();
    flag.all->key = 'a';
    flag.all->description = _("Calculate all textural measurements");

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    flag.null = G_define_flag();
    flag.null->key = 'n';
    flag.null->label = _("Allow NULL cells in a moving window");
    flag.null->description =
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
=======
    flag_null = G_define_flag();
    flag_null->key = 'n';
    flag_null->label = _("Allow NULL cells in a moving window");
    flag_null->description =
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
        _("This will also avoid cropping along edges of the current region");

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    name = parm.input->answer;
    result = parm.output->answer;
    dim.size = atoi(parm.size->answer);
    dim.dist = atoi(parm.dist->answer);

    if (dim.size <= 0)
<<<<<<< HEAD
        G_fatal_error(_("Size of the moving window must be > 0"));
    if (dim.size % 2 != 1)
        G_fatal_error(_("Size of the moving window must be odd"));
    if (dim.dist <= 0)
        G_fatal_error(_("The distance between two samples must be > 0"));
    if (dim.dist >= dim.size)
        G_fatal_error(_("The distance between two samples must be smaller than "
                        "the size of the moving window"));

    dim.n_measures = 0;
    if (flag.all->answer) {
        for (i = 0; measure_menu[i].name; i++) {
            measure_menu[i].useme = 1;
        }
        dim.n_measures = i;
    }
    else {
        for (i = 0; parm.measure->answers[i]; i++) {
            if (parm.measure->answers[i]) {
                const char *measure_name = parm.measure->answers[i];
                int n = find_measure(measure_name);

                measure_menu[n].useme = 1;
                dim.n_measures++;
            }
        }
    }
    if (!dim.n_measures)
        G_fatal_error(
            _("Nothing to compute. Use at least one textural measure."));

    measure_idx = G_malloc(dim.n_measures * sizeof(int));
    j = 0;
    for (i = 0; measure_menu[i].name; i++) {
        if (measure_menu[i].useme == 1) {
=======
    name = opt_input->answer;
    result = opt_output->answer;
    size = atoi(opt_size->answer);
    if (size <= 0)
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
        G_fatal_error(_("Size of the moving window must be > 0"));
    if (dim.size % 2 != 1)
        G_fatal_error(_("Size of the moving window must be odd"));
    if (dim.dist <= 0)
        G_fatal_error(_("The distance between two samples must be > 0"));
    if (dim.dist >= dim.size)
        G_fatal_error(_("The distance between two samples must be smaller than "
                        "the size of the moving window"));

    dim.n_measures = 0;
    if (flag.all->answer) {
        for (i = 0; measure_menu[i].name; i++) {
            measure_menu[i].useme = 1;
        }
        dim.n_measures = i;
    }
    else {
        for (i = 0; parm.measure->answers[i]; i++) {
            if (parm.measure->answers[i]) {
                const char *measure_name = parm.measure->answers[i];
                int n = find_measure(measure_name);

                measure_menu[n].useme = 1;
                dim.n_measures++;
            }
        }
    }
    if (!dim.n_measures)
        G_fatal_error(
            _("Nothing to compute. Use at least one textural measure."));

    measure_idx = G_malloc(dim.n_measures * sizeof(int));
    j = 0;
<<<<<<< HEAD
    for (i = 0; menu[i].name; i++) {
        if (menu[i].useme == 1) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    for (i = 0; measure_menu[i].name; i++) {
        if (measure_menu[i].useme == 1) {
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
=======
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
        G_fatal_error(_("Size of the moving window must be > 0"));
    if (dim.size % 2 != 1)
        G_fatal_error(_("Size of the moving window must be odd"));
    if (dim.dist <= 0)
        G_fatal_error(_("The distance between two samples must be > 0"));
    if (dim.dist >= dim.size)
        G_fatal_error(_("The distance between two samples must be smaller than "
                        "the size of the moving window"));

    dim.n_measures = 0;
    if (flag.all->answer) {
        for (i = 0; measure_menu[i].name; i++) {
            measure_menu[i].useme = 1;
        }
        dim.n_measures = i;
    }
    else {
        for (i = 0; parm.measure->answers[i]; i++) {
            if (parm.measure->answers[i]) {
                const char *measure_name = parm.measure->answers[i];
                int n = find_measure(measure_name);

                measure_menu[n].useme = 1;
                dim.n_measures++;
            }
        }
    }
    if (!dim.n_measures)
        G_fatal_error(
            _("Nothing to compute. Use at least one textural measure."));

    measure_idx = G_malloc(dim.n_measures * sizeof(int));
    j = 0;
<<<<<<< HEAD
    for (i = 0; menu[i].name; i++) {
        if (menu[i].useme == 1) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    for (i = 0; measure_menu[i].name; i++) {
        if (measure_menu[i].useme == 1) {
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
            measure_idx[j] = i;
            j++;
        }
    }

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
=======
    /* variables needed */
    if (menu[2].useme || menu[11].useme || menu[12].useme)
        have_px = 1;
    else
        have_px = 0;
    if (menu[11].useme || menu[12].useme)
        have_py = 1;
    else
        have_py = 0;
    if (menu[5].useme || menu[6].useme || menu[7].useme)
        have_pxpys = 1;
    else
        have_pxpys = 0;
    if (menu[9].useme || menu[10].useme)
        have_pxpyd = 1;
    else
        have_pxpyd = 0;

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    infd = Rast_open_old(name, "");

    Rast_get_cellhd(name, "", &cellhd);

    out_data_type = FCELL_TYPE;
    /* Allocate output buffers, use FCELL data_type */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    dim.n_outputs = dim.n_measures;
    if (flag.ind->answer) {
        dim.n_outputs = dim.n_measures * 4;
    }

    mapname = G_malloc(dim.n_outputs * sizeof(char *));
    for (i = 0; i < dim.n_outputs; i++)
        mapname[i] = G_malloc(GNAME_MAX * sizeof(char));
=======
    n_outputs = n_measures;
    if (flag_ind->answer) {
        n_outputs = n_measures * 4;
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
=======
    dim.n_outputs = dim.n_measures;
    if (flag.ind->answer) {
        dim.n_outputs = dim.n_measures * 4;
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
    }

    mapname = G_malloc(dim.n_outputs * sizeof(char *));
    for (i = 0; i < dim.n_outputs; i++)
        mapname[i] = G_malloc(GNAME_MAX * sizeof(char));
<<<<<<< HEAD
        fbuf[i] = Rast_allocate_buf(out_data_type);
    }
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    }

    mapname = G_malloc(dim.n_outputs * sizeof(char *));
    for (i = 0; i < dim.n_outputs; i++)
        mapname[i] = G_malloc(GNAME_MAX * sizeof(char));
<<<<<<< HEAD
        fbuf[i] = Rast_allocate_buf(out_data_type);
    }
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))

    overwrite = G_check_overwrite(argc, argv);

    /* open output maps */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    outfd = G_malloc(dim.n_outputs * sizeof(int));
    for (i = 0; i < dim.n_measures; i++) {
        if (flag.ind->answer) {
            for (j = 0; j < 4; j++) {
                sprintf(mapname[i * 4 + j], "%s%s_%d", result,
                        measure_menu[measure_idx[i]].suffix, j * 45);
=======
    outfd = G_malloc(n_outputs * sizeof(int));
    for (i = 0; i < n_measures; i++) {
        if (flag_ind->answer) {
            for (j = 0; j < 4; j++) {
                sprintf(mapname[i * 4 + j], "%s%s_%d", result,
                        menu[measure_idx[i]].suffix, j * 45);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    outfd = G_malloc(dim.n_outputs * sizeof(int));
    for (i = 0; i < dim.n_measures; i++) {
        if (flag.ind->answer) {
            for (j = 0; j < 4; j++) {
                sprintf(mapname[i * 4 + j], "%s%s_%d", result,
                        measure_menu[measure_idx[i]].suffix, j * 45);
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
                if (!G_find_raster(mapname[i * 4 + j], G_mapset()) ||
                    overwrite) {
                    outfd[i * 4 + j] =
                        Rast_open_new(mapname[i * 4 + j], out_data_type);
                }
                else {
                    G_fatal_error(_("At least one of the requested output maps "
                                    "exists. Use --o to overwrite."));
                }
            }
        }
        else {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
            sprintf(mapname[i], "%s%s", result,
                    measure_menu[measure_idx[i]].suffix);
=======
            sprintf(mapname[i], "%s%s", result, menu[measure_idx[i]].suffix);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
            sprintf(mapname[i], "%s%s", result, menu[measure_idx[i]].suffix);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            sprintf(mapname[i], "%s%s", result,
                    measure_menu[measure_idx[i]].suffix);
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
            sprintf(mapname[i], "%s%s", result, menu[measure_idx[i]].suffix);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
            if (!G_find_raster(mapname[i], G_mapset()) || overwrite) {
                outfd[i] = Rast_open_new(mapname[i], out_data_type);
            }
            else {
                G_fatal_error(_("At least one of the requested output maps "
                                "exists. Use --o to overwrite."));
            }
        }
    }
    dim.nrows = Rast_window_rows();
    dim.ncols = Rast_window_cols();

    /* Load raster map. */

    /* allocate the space for one row of cell map data *A* */
    dcell_row = Rast_allocate_d_buf();

    /* Allocate appropriate memory for the structure containing the image */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    data = (int **)G_malloc(dim.nrows * sizeof(int *));
    for (i = 0; i < dim.nrows; i++) {
        data[i] = (int *)G_malloc(dim.ncols * sizeof(int));
=======
    data = (int **)G_malloc(nrows * sizeof(int *));
    for (i = 0; i < nrows; i++) {
        data[i] = (int *)G_malloc(ncols * sizeof(int));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    data = (int **)G_malloc(dim.nrows * sizeof(int *));
    for (i = 0; i < dim.nrows; i++) {
        data[i] = (int *)G_malloc(dim.ncols * sizeof(int));
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    }

    /* read input range */
    Rast_init_fp_range(&range);
    Rast_read_fp_range(name, "", &range);
    Rast_get_fp_range_min_max(&range, &min, &max);
    inscale = 0;
    if (min < 0 || max > 255) {
        inscale = 255. / (max - min);
    }
    /* input has 0 - 1 range */
    else if (max <= 1.) {
        inscale = 255. / (max - min);
    }

    /* Read in cell map values */
    /* TODO: use r.proj cache */
    G_important_message(_("Reading raster map..."));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    for (j = 0; j < dim.nrows; j++) {
        Rast_get_row(infd, dcell_row, j, DCELL_TYPE);
        for (i = 0; i < dim.ncols; i++) {
=======
    for (j = 0; j < nrows; j++) {
        Rast_get_row(infd, dcell_row, j, DCELL_TYPE);
        for (i = 0; i < ncols; i++) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    for (j = 0; j < dim.nrows; j++) {
        Rast_get_row(infd, dcell_row, j, DCELL_TYPE);
        for (i = 0; i < dim.ncols; i++) {
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
            if (Rast_is_d_null_value(&(dcell_row[i])))
                data[j][i] = -1;
            else if (inscale) {
                data[j][i] = (CELL)((dcell_row[i] - min) * inscale);
            }
            else
                data[j][i] = (CELL)dcell_row[i];
        }
    }

    /* close input cell map and release the row buffer */
    Rast_close(infd);
    G_free(dcell_row);

    /* variables needed */
    out_set.outfd = outfd;
    out_set.out_data_type = out_data_type;
    out_set.flag_null = flag.null;
    out_set.flag_ind = flag.ind;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
=======
>>>>>>> osgeo-main
    /* *************************************************************************************************
     *
     * Compute of the matrix S.G.L.D. (Spatial Gray-Level Dependence Matrices)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
     *or co-occurrence matrix. The image is analized for piece, every piece is
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
     *or co-occurrence matrix. The image is analyzed for piece, every piece is
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
     *naming moving window (s.w.). The s.w. must be square with number of size's
     *samples odd, that because we want the sample at the center of matrix.
     *
     ***************************************************************************************************/
<<<<<<< HEAD
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
>>>>>>> ef6bae8fb5 (r.texture: Refactor code, remove global variables (#3785))
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> d0d53c2f4a (r.texture: Refactor code, remove global variables (#3785))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
     *or co-occurrence matrix. The image is analyzed for piece, every piece is
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
     *naming moving window (s.w.). The s.w. must be square with number of size's
     *samples odd, that because we want the sample at the center of matrix.
     *
     ***************************************************************************************************/
<<<<<<< HEAD
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
>>>>>>> ef6bae8fb5 (r.texture: Refactor code, remove global variables (#3785))
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
=======
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
    threads = G_set_omp_num_threads(parm.nproc);
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
     *or co-occurrence matrix. The image is analyzed for piece, every piece is
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
     *naming moving window (s.w.). The s.w. must be square with number of size's
     *samples odd, that because we want the sample at the center of matrix.
     *
     ***************************************************************************************************/
<<<<<<< HEAD
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
>>>>>>> ef6bae8fb5 (r.texture: Refactor code, remove global variables (#3785))
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
=======
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
    threads = atoi(parm.nproc->answer);
#if defined(_OPENMP)
    /* Set the number of threads */
    omp_set_num_threads(threads);
    if (threads > 1)
        G_message(_("Using %d threads for parallel computing."), threads);
#else
    if (threads > 1) {
        G_warning(_("GRASS GIS is not compiled with OpenMP support, parallel "
                    "computation is disabled."));
        threads = 1;
    }
#endif
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set, threads);
=======
<<<<<<< HEAD
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d0d53c2f4a (r.texture: Refactor code, remove global variables (#3785))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
    /* *************************************************************************************************
     *
     * Compute of the matrix S.G.L.D. (Spatial Gray-Level Dependence Matrices)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
     *or co-occurrence matrix. The image is analyzed for piece, every piece is
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
     *naming moving window (s.w.). The s.w. must be square with number of size's
     *samples odd, that because we want the sample at the center of matrix.
     *
     ***************************************************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
>>>>>>> ef6bae8fb5 (r.texture: Refactor code, remove global variables (#3785))
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
=======
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
    /* *************************************************************************************************
     *
     * Compute of the matrix S.G.L.D. (Spatial Gray-Level Dependence Matrices)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
     *or co-occurrence matrix. The image is analyzed for piece, every piece is
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
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
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
     *naming moving window (s.w.). The s.w. must be square with number of size's
     *samples odd, that because we want the sample at the center of matrix.
     *
     ***************************************************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
=======
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
>>>>>>> ef6bae8fb5 (r.texture: Refactor code, remove global variables (#3785))
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
=======
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
    /* *************************************************************************************************
     *
     * Compute of the matrix S.G.L.D. (Spatial Gray-Level Dependence Matrices)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
     *or co-occurrence matrix. The image is analyzed for piece, every piece is
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
     *or co-occurrence matrix. The image is analized for piece, every piece is
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
     *naming moving window (s.w.). The s.w. must be square with number of size's
     *samples odd, that because we want the sample at the center of matrix.
     *
     ***************************************************************************************************/
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
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
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))

<<<<<<< HEAD
    for (i = 0; i < dim.n_outputs; i++) {
        Rast_close(outfd[i]);
        Rast_short_history(mapname[i], "raster", &history);
        Rast_command_history(&history);
        Rast_write_history(mapname[i], &history);
        Rast_free_history(&history);
=======
    offset = size / 2;

    if (!flag_null->answer) {
        first_row = first_col = offset;
        last_row = nrows - offset;
        last_col = ncols - offset;
    }
    else {
        /* no cropping at window margins */
        first_row = first_col = 0;
        last_row = nrows;
        last_col = ncols;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    }

    /* Free allocated memory */
    for (i = 0; i < dim.n_outputs; i++)
        G_free(mapname[i]);
    for (i = 0; i < dim.nrows; i++)
        G_free(data[i]);

<<<<<<< HEAD
    G_free(measure_idx);
    G_free(mapname);
=======
    for (row = 0; row < first_row; row++) {
        for (i = 0; i < n_outputs; i++) {
            Rast_put_row(outfd[i], fbuf[0], out_data_type);
        }
    }
    if (n_measures > 1)
        G_message(n_("Calculating %d texture measure",
                     "Calculating %d texture measures", n_measures),
                  n_measures);
    else
        G_message(_("Calculating %s..."), menu[measure_idx[0]].desc);
    alloc_vars(size);
    for (row = first_row; row < last_row; row++) {
        G_percent(row, nrows, 2);

        for (i = 0; i < n_outputs; i++)
            Rast_set_f_null_value(fbuf[i], ncols);

        /*process the data */
        for (col = first_col; col < last_col; col++) {

            if (!set_vars(data, row, col, size, offset, dist,
                          flag_null->answer)) {
                for (i = 0; i < n_outputs; i++)
                    Rast_set_f_null_value(&(fbuf[i][col]), 1);
                continue;
            }

            /* for all angles (0, 45, 90, 135) */
            for (i = 0; i < 4; i++) {
                set_angle_vars(i, have_px, have_py, have_pxpys, have_pxpyd);
                /* for all requested textural measures */
                for (j = 0; j < n_measures; j++) {

                    measure = (FCELL)h_measure(menu[measure_idx[j]].idx);

                    if (flag_ind->answer) {
                        /* output for each angle separately */
                        fbuf[j * 4 + i][col] = measure;
                    }
                    else {
                        /* use average over all angles for each measure */
                        if (i == 0)
                            fbuf[j][col] = measure;
                        else if (i < 3)
                            fbuf[j][col] += measure;
                        else
                            fbuf[j][col] = (fbuf[j][col] + measure) / 4.0;
                    }
                }
            }
        }
        for (i = 0; i < n_outputs; i++) {
            Rast_put_row(outfd[i], fbuf[i], out_data_type);
        }
    }
    Rast_set_f_null_value(fbuf[0], ncols);
    for (row = last_row; row < nrows; row++) {
        for (i = 0; i < n_outputs; i++) {
            Rast_put_row(outfd[i], fbuf[0], out_data_type);
        }
    }
    G_percent(nrows, nrows, 1);

    for (i = 0; i < n_outputs; i++) {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
=======
=======
    execute_texture(data, &dim, measure_menu, measure_idx, &out_set);
>>>>>>> ef6bae8fb5 (r.texture: Refactor code, remove global variables (#3785))
<<<<<<< HEAD

    for (i = 0; i < dim.n_outputs; i++) {
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
        Rast_close(outfd[i]);
        Rast_short_history(mapname[i], "raster", &history);
        Rast_command_history(&history);
        Rast_write_history(mapname[i], &history);
    }

<<<<<<< HEAD
    G_free(fbuf);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    /* Free allocated memory */
    for (i = 0; i < dim.n_outputs; i++)
        G_free(mapname[i]);
    for (i = 0; i < dim.nrows; i++)
        G_free(data[i]);

    G_free(measure_idx);
    G_free(mapname);
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
        Rast_close(outfd[i]);
=======
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))

    for (i = 0; i < dim.n_outputs; i++) {
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
        Rast_close(outfd[i]);
        Rast_short_history(mapname[i], "raster", &history);
        Rast_command_history(&history);
        Rast_write_history(mapname[i], &history);
    }

<<<<<<< HEAD
    G_free(fbuf);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
    /* Free allocated memory */
    for (i = 0; i < dim.n_outputs; i++)
        G_free(mapname[i]);
    for (i = 0; i < dim.nrows; i++)
        G_free(data[i]);

    G_free(measure_idx);
    G_free(mapname);
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
>>>>>>> efb5ecd6aa (r.texture: Refactor code, remove global variables (#3785))
    G_free(data);

    exit(EXIT_SUCCESS);
}
