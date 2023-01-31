/****************************************************************
 *
 * MODULE:     v.generalize
 *
 * AUTHOR(S):  Daniel Bundala
 *
 * PURPOSE:    Methods for displacement
 *
 * COPYRIGHT:  (C) 2002-2005 by the GRASS Development Team
 *
 *             This program is free software under the
 *             GNU General Public License (>=v2).
 *             Read the file COPYING that comes with GRASS
 *             for details.
 *
 ****************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <grass/gis.h>
#include <grass/vector.h>
#include <grass/glocale.h>
#include "point.h"
#include "matrix.h"

/* snakes method modified for displacement.
 * Function returns something. This function affects only the
 * lines specified in varray (or all lines if varray is null).
 Other lines are copied */
int snakes_displacement(struct Map_info *In, struct Map_info *Out,
                        double threshold, double alpha, double beta,
                        double gama, double delta, int iterations,
                        struct cat_list *cat_list, int layer)
{

    int n_points;
    int n_lines;
    int i, j, index, pindex, iter, type;
    int with_z = 0;
    struct line_pnts *Points;
    struct line_cats *Cats;
    MATRIX k, dx, dy, fx, fy, kinv, dx_old, dy_old;
    POINT *parray;
    POINT *pset;
    int *point_index;
    int *first, *line_index, *need, *sel, *tmp_index;
    double threshold2;
    int selected;

    /* initialize structrures and read the number of points */
    Points = Vect_new_line_struct();
    Cats = Vect_new_cats_struct();
    n_lines = Vect_get_num_lines(In);
    n_points = 0;

    for (i = 1; i <= n_lines; i++) {
        type = Vect_read_line(In, Points, Cats, i);
        if (layer > 0 && !Vect_cats_in_constraint(Cats, layer, cat_list))
            continue;
        if (type & GV_LINE)
            n_points += Points->n_points;
    }

    parray = (POINT *)G_calloc(n_points, sizeof(POINT));
    pset = (POINT *)G_calloc(n_points, sizeof(POINT));
    point_index = (int *)G_calloc(n_points, sizeof(int));
    first = (int *)G_calloc(n_points, sizeof(int));
    line_index = (int *)G_calloc(n_points, sizeof(int));
    need = (int *)G_calloc(n_points, sizeof(int));
    sel = (int *)G_calloc(n_points, sizeof(int));
    tmp_index = (int *)G_calloc(n_points, sizeof(int));

    /* read points
     * TODO: some better/faster method for determining whether two points are
     * the same */
    G_percent_reset();
    G_message(_("Reading data..."));
    index = 0;
    pindex = 0;
    for (i = 1; i <= n_lines; i++) {
        G_percent(i, n_lines, 1);
        type = Vect_read_line(In, Points, Cats, i);
        if (type != GV_LINE)
            continue;
        if (layer > 0 && !Vect_cats_in_constraint(Cats, layer, cat_list))
            continue;

        for (j = 0; j < Points->n_points; j++) {
            int q, findex;
            POINT cur;

            point_assign(Points, j, with_z, &cur, 0);
            /* check whether we alerady have point with the same
             * coordinates */
            findex = pindex;
            for (q = 0; q < pindex; q++)
                if (point_dist_square(cur, pset[q]) < 0.5) {
                    findex = q;
                    break;
                }

            point_index[index] = findex;
            if (findex == pindex) {
                point_assign(Points, j, with_z, &pset[pindex], 0);
                pindex++;
            }
            first[index] = (j == 0);
            line_index[index] = i;
            point_assign(Points, j, with_z, &parray[index], 0);
            index++;
        }
    }

    threshold2 = threshold * threshold;
    /*select only the points which need to be displaced */
    for (i = 0; i < index; i++) {
        if (need[point_index[i]])
            continue;
        for (j = 1; j < index; j++) {
            if (line_index[i] == line_index[j] || first[j] ||
                point_index[i] == point_index[j] ||
                point_index[i] == point_index[j - 1])
                continue;
            double d = point_dist_segment_square(parray[i], parray[j],
                                                 parray[j - 1], with_z);

            if (d < 4 * threshold2)
                need[point_index[i]] = 1;
        }
    }

    /* then for each selected point ensure that the neighbours to the both
     * sides are selected as well */
    for (i = 0; i < index; i++) {
        int l = line_index[i];

        tmp_index[i] = -1;
        if (!need[point_index[i]])
            continue;
        for (j = -2; j <= 2; j++)
            if (i + j >= 0 && i + j < index && line_index[i + j] == l)
                sel[point_index[i + j]] = 1;
    }

    /* finally, recalculate indices */
    selected = 0;
    for (i = 0; i < pindex; i++)
        if (sel[i])
            tmp_index[i] = selected++;

    for (i = 0; i < index; i++)
        point_index[i] = tmp_index[point_index[i]];
    pindex = selected;

    G_debug(3, "Number of conflicting points: %d", pindex);

    /* initialize matrices */
    matrix_init(pindex, pindex, &k);
    matrix_init(pindex, 1, &dx);
    matrix_init(pindex, 1, &dy);
    matrix_init(pindex, 1, &fx);
    matrix_init(pindex, 1, &fy);
    matrix_init(pindex, 1, &dx_old);
    matrix_init(pindex, 1, &dy_old);

    matrix_mult_scalar(0.0, &k);

    double a = 2.0 * alpha + 6.0 * beta;
    double b = -alpha - 4.0 * beta;
    double c = beta;

    /* build matrix */
    for (i = 0; i < index; i++) {
        int r = point_index[i];
        int l = line_index[i];

        if (r == -1)
            continue;
        k.a[r][r] += a;
        if (i + 1 < index && line_index[i + 1] == l && point_index[i + 1] != -1)
            k.a[r][point_index[i + 1]] += b;
        if (i + 2 < index && line_index[i + 2] == l && point_index[i + 2] != -1)
            k.a[r][point_index[i + 2]] += c;
        if (i >= 1 && line_index[i - 1] == l && point_index[i - 1] != -1)
            k.a[r][point_index[i - 1]] += b;
        if (i >= 2 && line_index[i - 2] == l && point_index[i - 2] != -1)
            k.a[r][point_index[i - 2]] += c;
    }

    matrix_add_identity(gama, &k);
    matrix_mult_scalar(0.0, &dx);
    matrix_mult_scalar(0.0, &dy);

    /*calculate the inverse */
    G_message(_("Inverting matrix..."));
    if (!matrix_inverse(&k, &kinv, 1))
        G_fatal_error(_("Unable to calculate the inverse matrix"));

    G_percent_reset();
    G_message(_("Resolving conflicts..."));
    for (iter = 0; iter < iterations; iter++) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

=======
        int conflicts = 0;

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
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
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        int conflicts = 0;

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
        int conflicts = 0;

=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

=======
=======
        int conflicts = 0;

<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
=======
        int conflicts = 0;

>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
<<<<<<< HEAD
<<<<<<< HEAD
=======
                conflicts++;
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
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
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

=======
=======
        int conflicts = 0;

<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
=======
        int conflicts = 0;

>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
<<<<<<< HEAD
<<<<<<< HEAD
=======
                conflicts++;
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        int conflicts = 0;

        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
                conflicts++;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        int conflicts = 0;

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
        G_percent(iter, iterations, 1);

        matrix_mult_scalar(0.0, &fx);
        matrix_mult_scalar(0.0, &fy);

        matrix_mult_scalar(0.0, &dx_old);
        matrix_mult_scalar(0.0, &dy_old);

        matrix_add(&dx_old, &dx, &dx_old);
        matrix_add(&dy_old, &dy, &dy_old);

        /* calculate force vectors */
        for (i = 0; i < index; i++) {

            double cx, cy, f;

            if (point_index[i] == -1)
                continue;
            cx = dx.a[point_index[i]][0];
            cy = dy.a[point_index[i]][0];
            f = sqrt(cx * cx + cy * cy) * alpha;
            f /= threshold2;
            fx.a[point_index[i]][0] -= cx * f;
            fy.a[point_index[i]][0] -= cy * f;

            for (j = 1; j < index; j++) {
                if (line_index[i] == line_index[j] || first[j] ||
                    point_index[i] == point_index[j] ||
                    point_index[i] == point_index[j - 1])
                    continue;
                /* if ith point is close to some segment then
                 * apply force to ith point. If the distance
                 * is zero, do not move the points */
                double d, pdist;
                POINT in;
                int status;

                d = dig_distance2_point_to_line(
                    parray[i].x, parray[i].y, parray[i].z, parray[j].x,
                    parray[j].y, parray[j].z, parray[j - 1].x, parray[j - 1].y,
                    parray[j - 1].z, with_z, &in.x, &in.y, &in.z, &pdist,
                    &status);

                POINT dir;

                if (d == 0.0 || d > threshold2)
                    continue;
                d = sqrt(d);
                point_subtract(parray[i], in, &dir);
                point_scalar(dir, 1.0 / d, &dir);
                point_scalar(dir, 1.0 - d / threshold, &dir);
                fx.a[point_index[i]][0] += dir.x;
                fy.a[point_index[i]][0] += dir.y;
            }
        }

        /* calculate new displacement */
        matrix_mult_scalar(delta, &fx);
        matrix_mult_scalar(delta, &fy);
        matrix_mult_scalar(gama, &dx);
        matrix_mult_scalar(gama, &dy);

        matrix_add(&dx, &fx, &fx);
        matrix_add(&dy, &fy, &fy);

        matrix_mult(&kinv, &fx, &dx);
        matrix_mult(&kinv, &fy, &dy);

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
        for (i = 0; i < index; i++) {
            if (point_index[i] == -1)
                continue;
            parray[i].x +=
                dx.a[point_index[i]][0] - dx_old.a[point_index[i]][0];
            parray[i].y +=
                dy.a[point_index[i]][0] - dy_old.a[point_index[i]][0];
        }
    }
    index = 0;
    for (i = 1; i <= n_lines; i++) {
        type = Vect_read_line(In, Points, Cats, i);

        if (type != GV_LINE ||
            (layer > 0 && !Vect_cats_in_constraint(Cats, layer, cat_list))) {
            Vect_write_line(Out, type, Points, Cats);
            continue;
        }
        for (j = 0; j < Points->n_points; j++) {
            Points->x[j] = parray[index].x;
            Points->y[j] = parray[index].y;
            index++;
        }
        Vect_write_line(Out, type, Points, Cats);
    }

    G_free(parray);
    G_free(pset);
    G_free(point_index);
    G_free(first);
    G_free(line_index);
    G_free(need);
    G_free(sel);
    G_free(tmp_index);
    matrix_free(&k);
    matrix_free(&kinv);
    matrix_free(&dx);
    matrix_free(&dy);
    matrix_free(&fx);
    matrix_free(&fy);
    matrix_free(&dx_old);
    matrix_free(&dy_old);
    Vect_destroy_cats_struct(Cats);
    Vect_destroy_line_struct(Points);

    return 0;
}
