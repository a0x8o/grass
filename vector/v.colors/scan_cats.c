#include <grass/vector.h>
#include <grass/raster.h>
#include <grass/glocale.h>

#include "local_proto.h"

static void scan_layer(int, const struct line_cats *, int *, int *);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void scan_cats(const struct Map_info *Map, int field, const char *style,
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
void scan_cats(struct Map_info *Map, int field, const char *style,
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
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
void scan_cats(const struct Map_info *Map, int field, const char *style,
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
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void scan_cats(const struct Map_info *Map, int field, const char *style,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
               const char *rules, const struct FPRange *range,
               struct Colors *colors)
{
    int ltype, lmin, lmax, cmin, cmax, line;
    struct line_cats *Cats;

    cmin = cmax = -1;
    Cats = Vect_new_cats_struct();

    G_message(_("Reading features..."));
    line = 0;
    while (TRUE) {
        ltype = Vect_read_next_line(Map, NULL, Cats);
        if (ltype == -1)
            G_fatal_error(_("Unable to read vector map"));
        if (ltype == -2)
            break; /* EOF */

        G_progress(++line, 1e4);

        scan_layer(field, Cats, &lmin, &lmax);

        if (cmin == -1 || lmin <= cmin)
            cmin = lmin;
        if (cmax == -1 || lmax >= cmax)
            cmax = lmax;
    }
    G_progress(1, 1);

    if (range) {
        if (range->min >= cmin && range->min <= cmax)
            cmin = range->min;
        else
            G_warning(_("Min value (%d) is out of range %d,%d"),
                      (int)range->min, cmin, cmax);

        if (range->max <= cmax && range->max >= cmin)
            cmax = range->max;
        else
            G_warning(_("Max value (%d) is out of range %d,%d"),
                      (int)range->max, cmin, cmax);
    }

    if (style)
        make_colors(colors, style, (DCELL)cmin, (DCELL)cmax, FALSE);
    else if (rules)
        load_colors(colors, rules, (DCELL)cmin, (DCELL)cmax, FALSE);

    Vect_destroy_cats_struct(Cats);
}

void scan_layer(int field, const struct line_cats *Cats, int *cmin, int *cmax)
{
    int n, cat;

    *cmin = *cmax = -1;
    for (n = 0; n < Cats->n_cats; n++) {
        if (Cats->field[n] == field) {
            cat = Cats->cat[n];
            if (*cmin == -1 || cat <= *cmin)
                *cmin = cat;
            if (*cmax == -1 || cat >= *cmax)
                *cmax = cat;
        }
    }
}
