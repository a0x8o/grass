/****************************************************************
 *
 * MODULE:       v.in.ogr
 *
 * AUTHOR(S):    Radim Blazek
 *
 * PURPOSE:      Import OGR vectors
 *
 * COPYRIGHT:    (C) 2001 by the GRASS Development Team
 *
 *               This program is free software under the
 *               GNU General Public License (>=v2).
 *               Read the file COPYING that comes with GRASS
 *               for details.
 *
 **************************************************************/

#include <stdlib.h>
#include <string.h>
#include <grass/gis.h>
#include <grass/dbmi.h>
#include <grass/vector.h>
#include <grass/glocale.h>
#include "ogr_api.h"
#include "global.h"

int split_line(struct Map_info *Map, int otype, struct line_pnts *Points,
               struct line_cats *Cats);

/* Add categories to centroids inside polygon */
int centroid(OGRGeometryH hGeomAny, CENTR *Centr, struct spatial_index *Sindex,
             int field, int cat, double min_area, int type)
{
    int i, valid_isles, j, np, nr, ret;
    static int first = 1;
    static struct line_pnts *Points;
    struct line_pnts **IPoints;
    static struct line_cats *BCats, *Cats;
    OGRGeometryH hGeom;
    OGRwkbGeometryType eType;
    OGRGeometryH hRing;
    double size;
    static struct ilist *List;
    struct bound_box box;

    G_debug(3, "centroid() cat = %d", cat);

    if (first) {
        Points = Vect_new_line_struct();
        BCats = Vect_new_cats_struct();
        Cats = Vect_new_cats_struct();
        List = Vect_new_list();
        first = 0;
    }
    else {
        Vect_reset_line(Points);
        Vect_reset_cats(Cats);
        Vect_reset_cats(BCats);
        Vect_cat_set(Cats, field, cat);
    }

    hGeom = hGeomAny;

    if (OGR_G_HasCurveGeometry(hGeom, 0)) {
        G_debug(2, "Approximating curves in a '%s'",
                OGR_G_GetGeometryName(hGeom));

        /* The ownership of the returned geometry belongs to the caller. */
        hGeom = OGR_G_GetLinearGeometry(hGeom, 0, NULL);
    }

    eType = wkbFlatten(OGR_G_GetGeometryType(hGeom));

    if (eType == wkbPolygon) {
        nr = OGR_G_GetGeometryCount(hGeom);

        G_debug(3, "polygon: %d rings", nr);

        /* SFS: 1 exterior boundary and 0 or more interior boundaries.
         *  So I hope that exterior is the first one, even if it is not
         * explicitly told  */

        /* Area */
        hRing = OGR_G_GetGeometryRef(hGeom, 0);
        if (hRing == NULL) {
            G_warning(_("Skipping empty geometry feature %d"), cat);
            return 0;
        }
        np = OGR_G_GetPointCount(hRing);
        Vect_reset_line(Points);
        for (j = 0; j < np; j++) {
            Vect_append_point(Points, OGR_G_GetX(hRing, j),
                              OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
        }

        /* Degenerate is ignored */
        if (Points->n_points < 4)
            return 0;

        /* Small areas ignored because boundaries are not imported */
        size = G_area_of_polygon(Points->x, Points->y, Points->n_points);
        if (size < min_area)
            return 0;

        /* Isles */
        IPoints = (struct line_pnts **)G_malloc((nr - 1) *
                                                sizeof(struct line_pnts *));
        valid_isles = 0;
        for (i = 1; i < nr; i++) {

            hRing = OGR_G_GetGeometryRef(hGeom, i);
            if ((np = OGR_G_GetPointCount(hRing)) > 0) {
                IPoints[valid_isles] = Vect_new_line_struct();
                for (j = 0; j < np; j++) {
                    Vect_append_point(
                        IPoints[valid_isles], OGR_G_GetX(hRing, j),
                        OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
                }
                size = G_area_of_polygon(IPoints[valid_isles]->x,
                                         IPoints[valid_isles]->y,
                                         IPoints[valid_isles]->n_points);
                if (size < min_area)
                    Vect_destroy_line_struct(IPoints[valid_isles]);
                else
                    valid_isles++;
            }
        }

        /* Find centroids */
        if (Points->n_points >= 4) {
            int centr, in;
            double x, y;

            Vect_line_box(Points, &box);
            /* centroid's z is set to zero */
            box.T = box.B = 0;
            Vect_spatial_index_select(Sindex, &box, List);

            for (i = 0; i < List->n_values; i++) {
                centr = List->value[i];
                x = Centr[centr].x;
                y = Centr[centr].y;
                ret = Vect_point_in_poly(x, y, Points);
                if (ret == 0)
                    continue; /* outside */

                in = 1;
                for (j = 0; j < valid_isles; j++) {
                    ret = Vect_point_in_poly(x, y, IPoints[j]);
                    if (ret > 0) { /* centroid in inner ring */
                        in = 0;
                        break; /* inside isle */
                    }
                }
                if (!in)
                    continue;

                G_debug(3, "Centroid %d : layer %d cat %d", centr, field, cat);
                Vect_cat_set(Centr[centr].cats, field, cat);
            }
        }

        for (i = 0; i < valid_isles; i++) {
            Vect_destroy_line_struct(IPoints[i]);
        }
        G_free(IPoints);
    }

    /* I did not test this because I did not have files of these types */
    else if (eType == wkbGeometryCollection || eType == wkbMultiPolygon) {
        G_debug(3, "GeometryCollection or MultiPolygon/LineString/Point");
        nr = OGR_G_GetGeometryCount(hGeom);
        for (i = 0; i < nr; i++) {
            hRing = OGR_G_GetGeometryRef(hGeom, i);

            ret = centroid(hRing, Centr, Sindex, field, cat, min_area, type);
        }
    }

    /* destroy non-curve version of a curve geometry */
    if (hGeom != hGeomAny)
        OGR_G_DestroyGeometry(hGeom);

    return 0;
}

/* count polygons and isles */
int poly_count(OGRGeometryH hGeomAny, int line2boundary)
{
    int i, nr, ret;
    OGRGeometryH hGeom;
    OGRwkbGeometryType eType;
    OGRGeometryH hRing;

    hGeom = hGeomAny;

    if (OGR_G_HasCurveGeometry(hGeom, 0)) {
        G_debug(2, "Approximating curves in a '%s'",
                OGR_G_GetGeometryName(hGeom));

        /* The ownership of the returned geometry belongs to the caller. */
        hGeom = OGR_G_GetLinearGeometry(hGeom, 0, NULL);
    }

    eType = wkbFlatten(OGR_G_GetGeometryType(hGeom));

    if (eType == wkbPolygon) {
        G_debug(5, "Polygon");
        nr = OGR_G_GetGeometryCount(hGeom);
        n_polygon_boundaries += nr;
    }
    else if (eType == wkbGeometryCollection || eType == wkbMultiPolygon) {
        G_debug(5, "GeometryCollection or MultiPolygon");
        nr = OGR_G_GetGeometryCount(hGeom);
        for (i = 0; i < nr; i++) {
            hRing = OGR_G_GetGeometryRef(hGeom, i);

            ret = poly_count(hRing, line2boundary);
            if (ret == -1) {
                G_warning(_("Unable to read part of geometry"));
            }
        }
    }

    if (!line2boundary) {
        /* destroy non-curve version of a curve geometry */
        if (hGeom != hGeomAny)
            OGR_G_DestroyGeometry(hGeom);

        return 0;
    }

    if (eType == wkbLineString) {
        G_debug(5, "Polygon");
        n_polygon_boundaries++;
    }
    else if (eType == wkbGeometryCollection || eType == wkbMultiLineString) {
        G_debug(5, "GeometryCollection or MultiPolygon");
        nr = OGR_G_GetGeometryCount(hGeom);
        for (i = 0; i < nr; i++) {
            hRing = OGR_G_GetGeometryRef(hGeom, i);

            ret = poly_count(hRing, line2boundary);
            if (ret == -1) {
                G_warning(_("Unable to read part of geometry"));
            }
        }
    }

    G_debug(1, "poly_count(): n_poly_boundaries=%d", n_polygon_boundaries);

    /* destroy non-curve version of a curve geometry */
    if (hGeom != hGeomAny)
        OGR_G_DestroyGeometry(hGeom);

    return 0;
}

/* Write geometry to output map */
int geom(OGRGeometryH hGeomAny, struct Map_info *Map, int field, int cat,
         double min_area, int type, int mk_centr)
{
    int i, valid_isles, j, np, nr, ret, otype;
    static int first = 1;
    static struct line_pnts *Points;
    struct line_pnts **IPoints;
    static struct line_cats *BCats, *Cats;
    OGRGeometryH hGeom;
    OGRwkbGeometryType eType;
    OGRGeometryH hRing;
    double x, y;
    double size;
    int lastidx;

    G_debug(3, "geom() cat = %d", cat);

    if (first) {
        Points = Vect_new_line_struct();
        BCats = Vect_new_cats_struct();
        Cats = Vect_new_cats_struct();
        first = 0;
    }
    Vect_reset_line(Points);
    Vect_reset_cats(Cats);
    Vect_reset_cats(BCats);
    Vect_cat_set(Cats, field, cat);

    hGeom = hGeomAny;

    if (OGR_G_HasCurveGeometry(hGeom, 0)) {
        G_debug(2, "Approximating curves in a '%s'",
                OGR_G_GetGeometryName(hGeom));

        /* The ownership of the returned geometry belongs to the caller. */
        hGeom = OGR_G_GetLinearGeometry(hGeom, 0, NULL);
    }

    eType = wkbFlatten(OGR_G_GetGeometryType(hGeom));

    if (eType == wkbPoint) {
        if ((np = OGR_G_GetPointCount(hGeom)) == 0) {
            G_warning(_("Skipping empty geometry feature %d"), cat);
            return 0;
        }

        Vect_append_point(Points, OGR_G_GetX(hGeom, 0), OGR_G_GetY(hGeom, 0),
                          OGR_G_GetZ(hGeom, 0));
        if (type & GV_CENTROID)
            otype = GV_CENTROID;
        else
            otype = GV_POINT;
        Vect_write_line(Map, otype, Points, Cats);
    }
    else if (eType == wkbLineString) {
        if ((np = OGR_G_GetPointCount(hGeom)) == 0) {
            G_warning(_("Skipping empty geometry feature %d"), cat);
            return 0;
        }

        for (i = 0; i < np; i++) {
            Vect_append_point(Points, OGR_G_GetX(hGeom, i),
                              OGR_G_GetY(hGeom, i), OGR_G_GetZ(hGeom, i));
        }
        Vect_line_prune(Points);
        if (type & GV_BOUNDARY)
            otype = GV_BOUNDARY;
        else
            otype = GV_LINE;

        if (split_distance > 0 && otype == GV_BOUNDARY)
            split_line(Map, otype, Points, Cats);
        else
            Vect_write_line(Map, otype, Points, Cats);
    }

    else if (eType == wkbPolygon) {
        G_debug(4, "\tPolygon");

        /* SFS: 1 exterior boundary and 0 or more interior boundaries.
         *  So I hope that exterior is the first one, even if it is not
         * explicitly told  */

        /* Area */
        hRing = OGR_G_GetGeometryRef(hGeom, 0);
        if (hRing == NULL || (np = OGR_G_GetPointCount(hRing)) == 0) {
            G_warning(_("Skipping empty geometry feature %d"), cat);
            return 0;
        }

        nr = OGR_G_GetGeometryCount(hGeom);

        Vect_reset_line(Points);
        for (j = 0; j < np; j++) {
            Vect_append_point(Points, OGR_G_GetX(hRing, j),
                              OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
        }
        Vect_line_prune(Points);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        /* Degenerate is not ignored because it may be useful to see where it
         * is, but may be eliminated by min_area option */
        if (Points->n_points < 4)
            G_warning(_("Feature (cat %d): degenerated polygon (%d vertices)"),
                      cat, Points->n_points);

        size = G_area_of_polygon(Points->x, Points->y, Points->n_points);
        if (size < min_area) {
            G_debug(2, "\tArea size %.1e, area not imported", size);
            return 0;
        }

        n_polygons++;

        if (type & GV_LINE)
            otype = GV_LINE;
        else
            otype = GV_BOUNDARY;

        if (split_distance > 0 && otype == GV_BOUNDARY)
            split_line(Map, otype, Points, BCats);
        else
            Vect_write_line(Map, otype, Points, BCats);

        /* Isles */
        IPoints = (struct line_pnts **)G_malloc((nr - 1) *
                                                sizeof(struct line_pnts *));
        valid_isles = 0;
        for (i = 1; i < nr; i++) {
            G_debug(3, "\tInner ring %d", i);

            hRing = OGR_G_GetGeometryRef(hGeom, i);

            if ((np = OGR_G_GetPointCount(hRing)) == 0) {
                G_warning(_("Skipping empty geometry feature %d"), cat);
            }
            else {
                IPoints[valid_isles] = Vect_new_line_struct();

                for (j = 0; j < np; j++) {
                    Vect_append_point(
                        IPoints[valid_isles], OGR_G_GetX(hRing, j),
                        OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
                }
                Vect_line_prune(IPoints[valid_isles]);

                if (IPoints[valid_isles]->n_points < 4)
                    G_warning(_("Degenerate island (%d vertices)"),
                              IPoints[i - 1]->n_points);

                size = G_area_of_polygon(IPoints[valid_isles]->x,
                                         IPoints[valid_isles]->y,
                                         IPoints[valid_isles]->n_points);
                if (size < min_area) {
                    G_debug(2, "\tIsland size %.1e, island not imported", size);
                }
                else {
                    if (type & GV_LINE)
                        otype = GV_LINE;
                    else
                        otype = GV_BOUNDARY;
                    if (split_distance > 0 && otype == GV_BOUNDARY)
                        split_line(Map, otype, IPoints[valid_isles], BCats);
                    else
                        Vect_write_line(Map, otype, IPoints[valid_isles],
                                        BCats);
                }
                valid_isles++;
            }
        } /* inner rings done */

        /* Centroid */
        /* Vect_get_point_in_poly_isl() would fail for degenerate polygon */
        if (mk_centr) {
            if (Points->n_points >= 4) {
                ret = Vect_get_point_in_poly_isl(
                    Points, (const struct line_pnts **)IPoints, valid_isles, &x,
                    &y);
                if (ret == -1) {
                    G_warning(_("Unable calculate centroid"));
                }
                else {
                    Vect_reset_line(Points);
                    Vect_append_point(Points, x, y, 0.0);
                    if (type & GV_POINT)
                        otype = GV_POINT;
                    else
                        otype = GV_CENTROID;
                    Vect_write_line(Map, otype, Points, Cats);
                }
            }
            else if (Points->n_points > 0) {
                if (Points->n_points >= 2) {
                    /* center of 1. segment ( 2. point is not best for 3
                     * vertices as 3. may be the same as 1.) */
                    x = (Points->x[0] + Points->x[1]) / 2;
                    y = (Points->y[0] + Points->y[1]) / 2;
                }
                else { /* one point */
                    x = Points->x[0];
                    y = Points->y[0];
                }
                Vect_reset_line(Points);
                Vect_append_point(Points, x, y, 0.0);
                if (type & GV_POINT)
                    otype = GV_POINT;
                else
                    otype = GV_CENTROID;
                Vect_write_line(Map, otype, Points, Cats);
            }
            else { /* 0 points */
                G_warning(_("No centroid written for polygon with 0 vertices"));
            }
        }

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
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
        /* Degenerate is not ignored because it may be useful to see where it
         * is, but may be eliminated by min_area option */
        if (Points->n_points < 4)
            G_warning(_("Feature (cat %d): degenerated polygon (%d vertices)"),
                      cat, Points->n_points);

        size = G_area_of_polygon(Points->x, Points->y, Points->n_points);
        if (size < min_area) {
            G_debug(2, "\tArea size %.1e, area not imported", size);
            return 0;
        }

        n_polygons++;

        if (type & GV_LINE)
            otype = GV_LINE;
        else
            otype = GV_BOUNDARY;

        if (split_distance > 0 && otype == GV_BOUNDARY)
            split_line(Map, otype, Points, BCats);
        else
            Vect_write_line(Map, otype, Points, BCats);

        /* Isles */
        IPoints = (struct line_pnts **)G_malloc((nr - 1) *
                                                sizeof(struct line_pnts *));
        valid_isles = 0;
        for (i = 1; i < nr; i++) {
            G_debug(3, "\tInner ring %d", i);

            hRing = OGR_G_GetGeometryRef(hGeom, i);

            if ((np = OGR_G_GetPointCount(hRing)) == 0) {
                G_warning(_("Skipping empty geometry feature %d"), cat);
            }
            else {
                IPoints[valid_isles] = Vect_new_line_struct();

                for (j = 0; j < np; j++) {
                    Vect_append_point(
                        IPoints[valid_isles], OGR_G_GetX(hRing, j),
                        OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
                }
                Vect_line_prune(IPoints[valid_isles]);

                if (IPoints[valid_isles]->n_points < 4)
                    G_warning(_("Degenerate island (%d vertices)"),
                              IPoints[i - 1]->n_points);

                size = G_area_of_polygon(IPoints[valid_isles]->x,
                                         IPoints[valid_isles]->y,
                                         IPoints[valid_isles]->n_points);
                if (size < min_area) {
                    G_debug(2, "\tIsland size %.1e, island not imported", size);
                }
                else {
                    if (type & GV_LINE)
                        otype = GV_LINE;
                    else
                        otype = GV_BOUNDARY;
                    if (split_distance > 0 && otype == GV_BOUNDARY)
                        split_line(Map, otype, IPoints[valid_isles], BCats);
                    else
                        Vect_write_line(Map, otype, IPoints[valid_isles],
                                        BCats);
                }
                valid_isles++;
            }
        } /* inner rings done */

        /* Centroid */
        /* Vect_get_point_in_poly_isl() would fail for degenerate polygon */
        if (mk_centr) {
            if (Points->n_points >= 4) {
                ret = Vect_get_point_in_poly_isl(
                    Points, (const struct line_pnts **)IPoints, valid_isles, &x,
                    &y);
                if (ret == -1) {
                    G_warning(_("Unable calculate centroid"));
                }
                else {
                    Vect_reset_line(Points);
                    Vect_append_point(Points, x, y, 0.0);
                    if (type & GV_POINT)
                        otype = GV_POINT;
                    else
                        otype = GV_CENTROID;
                    Vect_write_line(Map, otype, Points, Cats);
                }
            }
            else if (Points->n_points > 0) {
                if (Points->n_points >= 2) {
                    /* center of 1. segment ( 2. point is not best for 3
                     * vertices as 3. may be the same as 1.) */
                    x = (Points->x[0] + Points->x[1]) / 2;
                    y = (Points->y[0] + Points->y[1]) / 2;
                }
                else { /* one point */
                    x = Points->x[0];
                    y = Points->y[0];
                }
                Vect_reset_line(Points);
                Vect_append_point(Points, x, y, 0.0);
                if (type & GV_POINT)
                    otype = GV_POINT;
                else
                    otype = GV_CENTROID;
                Vect_write_line(Map, otype, Points, Cats);
            }
            else { /* 0 points */
                G_warning(_("No centroid written for polygon with 0 vertices"));
            }
        }

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
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
        /* Degenerate is not ignored because it may be useful to see where it
         * is, but may be eliminated by min_area option */
        if (Points->n_points < 4)
            G_warning(_("Feature (cat %d): degenerated polygon (%d vertices)"),
                      cat, Points->n_points);

        size = G_area_of_polygon(Points->x, Points->y, Points->n_points);
        if (size < min_area) {
            G_debug(2, "\tArea size %.1e, area not imported", size);
            return 0;
        }

        n_polygons++;

        if (type & GV_LINE)
            otype = GV_LINE;
        else
            otype = GV_BOUNDARY;

        if (split_distance > 0 && otype == GV_BOUNDARY)
            split_line(Map, otype, Points, BCats);
        else
            Vect_write_line(Map, otype, Points, BCats);

        /* Isles */
        IPoints = (struct line_pnts **)G_malloc((nr - 1) *
                                                sizeof(struct line_pnts *));
        valid_isles = 0;
        for (i = 1; i < nr; i++) {
            G_debug(3, "\tInner ring %d", i);

            hRing = OGR_G_GetGeometryRef(hGeom, i);

            if ((np = OGR_G_GetPointCount(hRing)) == 0) {
                G_warning(_("Skipping empty geometry feature %d"), cat);
            }
            else {
                IPoints[valid_isles] = Vect_new_line_struct();

                for (j = 0; j < np; j++) {
                    Vect_append_point(
                        IPoints[valid_isles], OGR_G_GetX(hRing, j),
                        OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
                }
                Vect_line_prune(IPoints[valid_isles]);

                if (IPoints[valid_isles]->n_points < 4)
                    G_warning(_("Degenerate island (%d vertices)"),
                              IPoints[i - 1]->n_points);

                size = G_area_of_polygon(IPoints[valid_isles]->x,
                                         IPoints[valid_isles]->y,
                                         IPoints[valid_isles]->n_points);
                if (size < min_area) {
                    G_debug(2, "\tIsland size %.1e, island not imported", size);
                }
                else {
                    if (type & GV_LINE)
                        otype = GV_LINE;
                    else
                        otype = GV_BOUNDARY;
                    if (split_distance > 0 && otype == GV_BOUNDARY)
                        split_line(Map, otype, IPoints[valid_isles], BCats);
                    else
                        Vect_write_line(Map, otype, IPoints[valid_isles],
                                        BCats);
                }
                valid_isles++;
            }
        } /* inner rings done */

        /* Centroid */
        /* Vect_get_point_in_poly_isl() would fail for degenerate polygon */
        if (mk_centr) {
            if (Points->n_points >= 4) {
                ret = Vect_get_point_in_poly_isl(
                    Points, (const struct line_pnts **)IPoints, valid_isles, &x,
                    &y);
                if (ret == -1) {
                    G_warning(_("Unable calculate centroid"));
                }
                else {
                    Vect_reset_line(Points);
                    Vect_append_point(Points, x, y, 0.0);
                    if (type & GV_POINT)
                        otype = GV_POINT;
                    else
                        otype = GV_CENTROID;
                    Vect_write_line(Map, otype, Points, Cats);
                }
            }
            else if (Points->n_points > 0) {
                if (Points->n_points >= 2) {
                    /* center of 1. segment ( 2. point is not best for 3
                     * vertices as 3. may be the same as 1.) */
                    x = (Points->x[0] + Points->x[1]) / 2;
                    y = (Points->y[0] + Points->y[1]) / 2;
                }
                else { /* one point */
                    x = Points->x[0];
                    y = Points->y[0];
                }
                Vect_reset_line(Points);
                Vect_append_point(Points, x, y, 0.0);
                if (type & GV_POINT)
                    otype = GV_POINT;
                else
                    otype = GV_CENTROID;
                Vect_write_line(Map, otype, Points, Cats);
            }
            else { /* 0 points */
                G_warning(_("No centroid written for polygon with 0 vertices"));
            }
        }

=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
        lastidx = Points->n_points - 1;
        if (Points->x[0] != Points->x[lastidx] ||
            Points->y[0] != Points->y[lastidx] ||
            Points->z[0] != Points->z[lastidx]) {
            if (mk_centr) {
                /* do not clean polygons */
                G_fatal_error(
                    _("Found unclosed outer polygon ring, can be "
                      "closed when cleaning polygons is not disabled"));
            }
            else {
                G_warning(_("Closing unclosed outer polygon ring"));
                Vect_append_point(Points, Points->x[0], Points->y[0],
                                  Points->z[0]);
            }
        }

        /* Degenerate is not ignored because it may be useful to see where it
         * is, but may be eliminated by min_area option */
        if (Points->n_points < 4)
            G_warning(_("Feature (cat %d): degenerated polygon (%d vertices)"),
                      cat, Points->n_points);

        size = G_area_of_polygon(Points->x, Points->y, Points->n_points);
        if (size < min_area) {
            G_debug(2, "\tArea size %.1e, area not imported", size);
            return 0;
        }

        n_polygons++;

        if (type & GV_LINE)
            otype = GV_LINE;
        else
            otype = GV_BOUNDARY;

        if (split_distance > 0 && otype == GV_BOUNDARY)
            split_line(Map, otype, Points, BCats);
        else
            Vect_write_line(Map, otype, Points, BCats);

        /* Isles */
        IPoints = (struct line_pnts **)G_malloc((nr - 1) *
                                                sizeof(struct line_pnts *));
        valid_isles = 0;
        for (i = 1; i < nr; i++) {
            G_debug(3, "\tInner ring %d", i);

            hRing = OGR_G_GetGeometryRef(hGeom, i);

            if ((np = OGR_G_GetPointCount(hRing)) == 0) {
                G_warning(_("Skipping empty geometry feature %d"), cat);
            }
            else {
                IPoints[valid_isles] = Vect_new_line_struct();

                for (j = 0; j < np; j++) {
                    Vect_append_point(
                        IPoints[valid_isles], OGR_G_GetX(hRing, j),
                        OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
                }
                Vect_line_prune(IPoints[valid_isles]);

                lastidx = IPoints[valid_isles]->n_points - 1;
                if (IPoints[valid_isles]->x[0] !=
                        IPoints[valid_isles]->x[lastidx] ||
                    IPoints[valid_isles]->y[0] !=
                        IPoints[valid_isles]->y[lastidx] ||
                    IPoints[valid_isles]->z[0] !=
                        IPoints[valid_isles]->z[lastidx]) {
                    if (mk_centr) {
                        /* do not clean polygons */
                        G_fatal_error(
                            _("Found unclosed inner polygon ring, can be "
                              "closed when cleaning polygons is not disabled"));
                    }
                    else {
                        G_warning(_("Closing unclosed inner polygon ring"));
                        Vect_append_point(IPoints[valid_isles],
                                          IPoints[valid_isles]->x[0],
                                          IPoints[valid_isles]->y[0],
                                          IPoints[valid_isles]->z[0]);
                    }
                }

                if (IPoints[valid_isles]->n_points < 4)
                    G_warning(_("Degenerate island (%d vertices)"),
                              IPoints[i - 1]->n_points);

                size = G_area_of_polygon(IPoints[valid_isles]->x,
                                         IPoints[valid_isles]->y,
                                         IPoints[valid_isles]->n_points);
                if (size < min_area) {
                    G_debug(2, "\tIsland size %.1e, island not imported", size);
                }
                else {
                    if (type & GV_LINE)
                        otype = GV_LINE;
                    else
                        otype = GV_BOUNDARY;
                    if (split_distance > 0 && otype == GV_BOUNDARY)
                        split_line(Map, otype, IPoints[valid_isles], BCats);
                    else
                        Vect_write_line(Map, otype, IPoints[valid_isles],
                                        BCats);
                }
                valid_isles++;
            }
        } /* inner rings done */

        /* Centroid */
        /* Vect_get_point_in_poly_isl() would fail for degenerate polygon */
        if (mk_centr) {
            if (Points->n_points >= 4) {
                ret = Vect_get_point_in_poly_isl(
                    Points, (const struct line_pnts **)IPoints, valid_isles, &x,
                    &y);
                if (ret == -1) {
                    G_warning(_("Unable calculate centroid"));
                }
                else {
                    Vect_reset_line(Points);
                    Vect_append_point(Points, x, y, 0.0);
                    if (type & GV_POINT)
                        otype = GV_POINT;
                    else
                        otype = GV_CENTROID;
                    Vect_write_line(Map, otype, Points, Cats);
                }
            }
            else if (Points->n_points > 0) {
                if (Points->n_points >= 2) {
                    /* center of 1. segment ( 2. point is not best for 3
                     * vertices as 3. may be the same as 1.) */
                    x = (Points->x[0] + Points->x[1]) / 2;
                    y = (Points->y[0] + Points->y[1]) / 2;
                }
                else { /* one point */
                    x = Points->x[0];
                    y = Points->y[0];
                }
                Vect_reset_line(Points);
                Vect_append_point(Points, x, y, 0.0);
                if (type & GV_POINT)
                    otype = GV_POINT;
                else
                    otype = GV_CENTROID;
                Vect_write_line(Map, otype, Points, Cats);
            }
            else { /* 0 points */
                G_warning(_("No centroid written for polygon with 0 vertices"));
            }
        }

=======
        /* Degenerate is not ignored because it may be useful to see where it
         * is, but may be eliminated by min_area option */
        if (Points->n_points < 4)
            G_warning(_("Feature (cat %d): degenerated polygon (%d vertices)"),
                      cat, Points->n_points);

        size = G_area_of_polygon(Points->x, Points->y, Points->n_points);
        if (size < min_area) {
            G_debug(2, "\tArea size %.1e, area not imported", size);
            return 0;
        }

        n_polygons++;

        if (type & GV_LINE)
            otype = GV_LINE;
        else
            otype = GV_BOUNDARY;

        if (split_distance > 0 && otype == GV_BOUNDARY)
            split_line(Map, otype, Points, BCats);
        else
            Vect_write_line(Map, otype, Points, BCats);

        /* Isles */
        IPoints = (struct line_pnts **)G_malloc((nr - 1) *
                                                sizeof(struct line_pnts *));
        valid_isles = 0;
        for (i = 1; i < nr; i++) {
            G_debug(3, "\tInner ring %d", i);

            hRing = OGR_G_GetGeometryRef(hGeom, i);

            if ((np = OGR_G_GetPointCount(hRing)) == 0) {
                G_warning(_("Skipping empty geometry feature %d"), cat);
            }
            else {
                IPoints[valid_isles] = Vect_new_line_struct();

                for (j = 0; j < np; j++) {
                    Vect_append_point(
                        IPoints[valid_isles], OGR_G_GetX(hRing, j),
                        OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
                }
                Vect_line_prune(IPoints[valid_isles]);

                if (IPoints[valid_isles]->n_points < 4)
                    G_warning(_("Degenerate island (%d vertices)"),
                              IPoints[i - 1]->n_points);

                size = G_area_of_polygon(IPoints[valid_isles]->x,
                                         IPoints[valid_isles]->y,
                                         IPoints[valid_isles]->n_points);
                if (size < min_area) {
                    G_debug(2, "\tIsland size %.1e, island not imported", size);
                }
                else {
                    if (type & GV_LINE)
                        otype = GV_LINE;
                    else
                        otype = GV_BOUNDARY;
                    if (split_distance > 0 && otype == GV_BOUNDARY)
                        split_line(Map, otype, IPoints[valid_isles], BCats);
                    else
                        Vect_write_line(Map, otype, IPoints[valid_isles],
                                        BCats);
                }
                valid_isles++;
            }
        } /* inner rings done */

        /* Centroid */
        /* Vect_get_point_in_poly_isl() would fail for degenerate polygon */
        if (mk_centr) {
            if (Points->n_points >= 4) {
                ret = Vect_get_point_in_poly_isl(
                    Points, (const struct line_pnts **)IPoints, valid_isles, &x,
                    &y);
                if (ret == -1) {
                    G_warning(_("Unable calculate centroid"));
                }
                else {
                    Vect_reset_line(Points);
                    Vect_append_point(Points, x, y, 0.0);
                    if (type & GV_POINT)
                        otype = GV_POINT;
                    else
                        otype = GV_CENTROID;
                    Vect_write_line(Map, otype, Points, Cats);
                }
            }
            else if (Points->n_points > 0) {
                if (Points->n_points >= 2) {
                    /* center of 1. segment ( 2. point is not best for 3
                     * vertices as 3. may be the same as 1.) */
                    x = (Points->x[0] + Points->x[1]) / 2;
                    y = (Points->y[0] + Points->y[1]) / 2;
                }
                else { /* one point */
                    x = Points->x[0];
                    y = Points->y[0];
                }
                Vect_reset_line(Points);
                Vect_append_point(Points, x, y, 0.0);
                if (type & GV_POINT)
                    otype = GV_POINT;
                else
                    otype = GV_CENTROID;
                Vect_write_line(Map, otype, Points, Cats);
            }
            else { /* 0 points */
                G_warning(_("No centroid written for polygon with 0 vertices"));
            }
        }

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
        /* Degenerate is not ignored because it may be useful to see where it
         * is, but may be eliminated by min_area option */
        if (Points->n_points < 4)
            G_warning(_("Feature (cat %d): degenerated polygon (%d vertices)"),
                      cat, Points->n_points);

        size = G_area_of_polygon(Points->x, Points->y, Points->n_points);
        if (size < min_area) {
            G_debug(2, "\tArea size %.1e, area not imported", size);
            return 0;
        }

        n_polygons++;

        if (type & GV_LINE)
            otype = GV_LINE;
        else
            otype = GV_BOUNDARY;

        if (split_distance > 0 && otype == GV_BOUNDARY)
            split_line(Map, otype, Points, BCats);
        else
            Vect_write_line(Map, otype, Points, BCats);

        /* Isles */
        IPoints = (struct line_pnts **)G_malloc((nr - 1) *
                                                sizeof(struct line_pnts *));
        valid_isles = 0;
        for (i = 1; i < nr; i++) {
            G_debug(3, "\tInner ring %d", i);

            hRing = OGR_G_GetGeometryRef(hGeom, i);

            if ((np = OGR_G_GetPointCount(hRing)) == 0) {
                G_warning(_("Skipping empty geometry feature %d"), cat);
            }
            else {
                IPoints[valid_isles] = Vect_new_line_struct();

                for (j = 0; j < np; j++) {
                    Vect_append_point(
                        IPoints[valid_isles], OGR_G_GetX(hRing, j),
                        OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
                }
                Vect_line_prune(IPoints[valid_isles]);

                if (IPoints[valid_isles]->n_points < 4)
                    G_warning(_("Degenerate island (%d vertices)"),
                              IPoints[i - 1]->n_points);

                size = G_area_of_polygon(IPoints[valid_isles]->x,
                                         IPoints[valid_isles]->y,
                                         IPoints[valid_isles]->n_points);
                if (size < min_area) {
                    G_debug(2, "\tIsland size %.1e, island not imported", size);
                }
                else {
                    if (type & GV_LINE)
                        otype = GV_LINE;
                    else
                        otype = GV_BOUNDARY;
                    if (split_distance > 0 && otype == GV_BOUNDARY)
                        split_line(Map, otype, IPoints[valid_isles], BCats);
                    else
                        Vect_write_line(Map, otype, IPoints[valid_isles],
                                        BCats);
                }
                valid_isles++;
            }
        } /* inner rings done */

        /* Centroid */
        /* Vect_get_point_in_poly_isl() would fail for degenerate polygon */
        if (mk_centr) {
            if (Points->n_points >= 4) {
                ret = Vect_get_point_in_poly_isl(
                    Points, (const struct line_pnts **)IPoints, valid_isles, &x,
                    &y);
                if (ret == -1) {
                    G_warning(_("Unable calculate centroid"));
                }
                else {
                    Vect_reset_line(Points);
                    Vect_append_point(Points, x, y, 0.0);
                    if (type & GV_POINT)
                        otype = GV_POINT;
                    else
                        otype = GV_CENTROID;
                    Vect_write_line(Map, otype, Points, Cats);
                }
            }
            else if (Points->n_points > 0) {
                if (Points->n_points >= 2) {
                    /* center of 1. segment ( 2. point is not best for 3
                     * vertices as 3. may be the same as 1.) */
                    x = (Points->x[0] + Points->x[1]) / 2;
                    y = (Points->y[0] + Points->y[1]) / 2;
                }
                else { /* one point */
                    x = Points->x[0];
                    y = Points->y[0];
                }
                Vect_reset_line(Points);
                Vect_append_point(Points, x, y, 0.0);
                if (type & GV_POINT)
                    otype = GV_POINT;
                else
                    otype = GV_CENTROID;
                Vect_write_line(Map, otype, Points, Cats);
            }
            else { /* 0 points */
                G_warning(_("No centroid written for polygon with 0 vertices"));
            }
        }

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
        /* Degenerate is not ignored because it may be useful to see where it
         * is, but may be eliminated by min_area option */
        if (Points->n_points < 4)
            G_warning(_("Feature (cat %d): degenerated polygon (%d vertices)"),
                      cat, Points->n_points);

        size = G_area_of_polygon(Points->x, Points->y, Points->n_points);
        if (size < min_area) {
            G_debug(2, "\tArea size %.1e, area not imported", size);
            return 0;
        }

        n_polygons++;

        if (type & GV_LINE)
            otype = GV_LINE;
        else
            otype = GV_BOUNDARY;

        if (split_distance > 0 && otype == GV_BOUNDARY)
            split_line(Map, otype, Points, BCats);
        else
            Vect_write_line(Map, otype, Points, BCats);

        /* Isles */
        IPoints = (struct line_pnts **)G_malloc((nr - 1) *
                                                sizeof(struct line_pnts *));
        valid_isles = 0;
        for (i = 1; i < nr; i++) {
            G_debug(3, "\tInner ring %d", i);

            hRing = OGR_G_GetGeometryRef(hGeom, i);

            if ((np = OGR_G_GetPointCount(hRing)) == 0) {
                G_warning(_("Skipping empty geometry feature %d"), cat);
            }
            else {
                IPoints[valid_isles] = Vect_new_line_struct();

                for (j = 0; j < np; j++) {
                    Vect_append_point(
                        IPoints[valid_isles], OGR_G_GetX(hRing, j),
                        OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
                }
                Vect_line_prune(IPoints[valid_isles]);

                if (IPoints[valid_isles]->n_points < 4)
                    G_warning(_("Degenerate island (%d vertices)"),
                              IPoints[i - 1]->n_points);

                size = G_area_of_polygon(IPoints[valid_isles]->x,
                                         IPoints[valid_isles]->y,
                                         IPoints[valid_isles]->n_points);
                if (size < min_area) {
                    G_debug(2, "\tIsland size %.1e, island not imported", size);
                }
                else {
                    if (type & GV_LINE)
                        otype = GV_LINE;
                    else
                        otype = GV_BOUNDARY;
                    if (split_distance > 0 && otype == GV_BOUNDARY)
                        split_line(Map, otype, IPoints[valid_isles], BCats);
                    else
                        Vect_write_line(Map, otype, IPoints[valid_isles],
                                        BCats);
                }
                valid_isles++;
            }
        } /* inner rings done */

        /* Centroid */
        /* Vect_get_point_in_poly_isl() would fail for degenerate polygon */
        if (mk_centr) {
            if (Points->n_points >= 4) {
                ret = Vect_get_point_in_poly_isl(
                    Points, (const struct line_pnts **)IPoints, valid_isles, &x,
                    &y);
                if (ret == -1) {
                    G_warning(_("Unable calculate centroid"));
                }
                else {
                    Vect_reset_line(Points);
                    Vect_append_point(Points, x, y, 0.0);
                    if (type & GV_POINT)
                        otype = GV_POINT;
                    else
                        otype = GV_CENTROID;
                    Vect_write_line(Map, otype, Points, Cats);
                }
            }
            else if (Points->n_points > 0) {
                if (Points->n_points >= 2) {
                    /* center of 1. segment ( 2. point is not best for 3
                     * vertices as 3. may be the same as 1.) */
                    x = (Points->x[0] + Points->x[1]) / 2;
                    y = (Points->y[0] + Points->y[1]) / 2;
                }
                else { /* one point */
                    x = Points->x[0];
                    y = Points->y[0];
                }
                Vect_reset_line(Points);
                Vect_append_point(Points, x, y, 0.0);
                if (type & GV_POINT)
                    otype = GV_POINT;
                else
                    otype = GV_CENTROID;
                Vect_write_line(Map, otype, Points, Cats);
            }
            else { /* 0 points */
                G_warning(_("No centroid written for polygon with 0 vertices"));
            }
        }

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
        /* Degenerate is not ignored because it may be useful to see where it
         * is, but may be eliminated by min_area option */
        if (Points->n_points < 4)
            G_warning(_("Feature (cat %d): degenerated polygon (%d vertices)"),
                      cat, Points->n_points);

        size = G_area_of_polygon(Points->x, Points->y, Points->n_points);
        if (size < min_area) {
            G_debug(2, "\tArea size %.1e, area not imported", size);
            return 0;
        }

        n_polygons++;

        if (type & GV_LINE)
            otype = GV_LINE;
        else
            otype = GV_BOUNDARY;

        if (split_distance > 0 && otype == GV_BOUNDARY)
            split_line(Map, otype, Points, BCats);
        else
            Vect_write_line(Map, otype, Points, BCats);

        /* Isles */
        IPoints = (struct line_pnts **)G_malloc((nr - 1) *
                                                sizeof(struct line_pnts *));
        valid_isles = 0;
        for (i = 1; i < nr; i++) {
            G_debug(3, "\tInner ring %d", i);

            hRing = OGR_G_GetGeometryRef(hGeom, i);

            if ((np = OGR_G_GetPointCount(hRing)) == 0) {
                G_warning(_("Skipping empty geometry feature %d"), cat);
            }
            else {
                IPoints[valid_isles] = Vect_new_line_struct();

                for (j = 0; j < np; j++) {
                    Vect_append_point(
                        IPoints[valid_isles], OGR_G_GetX(hRing, j),
                        OGR_G_GetY(hRing, j), OGR_G_GetZ(hRing, j));
                }
                Vect_line_prune(IPoints[valid_isles]);

                if (IPoints[valid_isles]->n_points < 4)
                    G_warning(_("Degenerate island (%d vertices)"),
                              IPoints[i - 1]->n_points);

                size = G_area_of_polygon(IPoints[valid_isles]->x,
                                         IPoints[valid_isles]->y,
                                         IPoints[valid_isles]->n_points);
                if (size < min_area) {
                    G_debug(2, "\tIsland size %.1e, island not imported", size);
                }
                else {
                    if (type & GV_LINE)
                        otype = GV_LINE;
                    else
                        otype = GV_BOUNDARY;
                    if (split_distance > 0 && otype == GV_BOUNDARY)
                        split_line(Map, otype, IPoints[valid_isles], BCats);
                    else
                        Vect_write_line(Map, otype, IPoints[valid_isles],
                                        BCats);
                }
                valid_isles++;
            }
        } /* inner rings done */

        /* Centroid */
        /* Vect_get_point_in_poly_isl() would fail for degenerate polygon */
        if (mk_centr) {
            if (Points->n_points >= 4) {
                ret = Vect_get_point_in_poly_isl(
                    Points, (const struct line_pnts **)IPoints, valid_isles, &x,
                    &y);
                if (ret == -1) {
                    G_warning(_("Unable calculate centroid"));
                }
                else {
                    Vect_reset_line(Points);
                    Vect_append_point(Points, x, y, 0.0);
                    if (type & GV_POINT)
                        otype = GV_POINT;
                    else
                        otype = GV_CENTROID;
                    Vect_write_line(Map, otype, Points, Cats);
                }
            }
            else if (Points->n_points > 0) {
                if (Points->n_points >= 2) {
                    /* center of 1. segment ( 2. point is not best for 3
                     * vertices as 3. may be the same as 1.) */
                    x = (Points->x[0] + Points->x[1]) / 2;
                    y = (Points->y[0] + Points->y[1]) / 2;
                }
                else { /* one point */
                    x = Points->x[0];
                    y = Points->y[0];
                }
                Vect_reset_line(Points);
                Vect_append_point(Points, x, y, 0.0);
                if (type & GV_POINT)
                    otype = GV_POINT;
                else
                    otype = GV_CENTROID;
                Vect_write_line(Map, otype, Points, Cats);
            }
            else { /* 0 points */
                G_warning(_("No centroid written for polygon with 0 vertices"));
            }
        }

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
        for (i = 0; i < valid_isles; i++) {
            Vect_destroy_line_struct(IPoints[i]);
        }
        G_free(IPoints);
    }

    /* I did not test this because I did not have files of these types */
    else if (eType == wkbGeometryCollection || eType == wkbMultiPolygon ||
             eType == wkbMultiLineString || eType == wkbMultiPoint) {
        G_debug(4, "\tGeometryCollection or MultiPolygon/LineString/Point");
        nr = OGR_G_GetGeometryCount(hGeom);
        for (i = 0; i < nr; i++) {
            hRing = OGR_G_GetGeometryRef(hGeom, i);

            ret = geom(hRing, Map, field, cat, min_area, type, mk_centr);
            if (ret == -1) {
                G_warning(_("Unable to write part of geometry"));
            }
        }
    }

    else {
        G_warning(_("Skipping unsupported geometry type '%s'"),
                  OGR_G_GetGeometryName(hGeom));
    }

    /* destroy non-curve version of a curve geometry */
    if (hGeom != hGeomAny)
        OGR_G_DestroyGeometry(hGeom);

    return 0;
}

int split_line(struct Map_info *Map, int otype, struct line_pnts *Points,
               struct line_cats *Cats)
{
    int i;
    double dist = 0., seg_dist, dx, dy;
    struct line_pnts *OutPoints;

    /* don't write zero length boundaries */
    Vect_line_prune(Points);
    if (Points->n_points < 2)
        return 0;

    /* can't split boundaries with only 2 vertices */
    if (Points->n_points == 2) {
        Vect_line_prune(Points);

        if (Points->n_points < 2)
            return 0;
        Vect_write_line(Map, otype, Points, Cats);
        return 0;
    }

    OutPoints = Vect_new_line_struct();
    Vect_append_point(OutPoints, Points->x[0], Points->y[0], Points->z[0]);
    Vect_append_point(OutPoints, Points->x[1], Points->y[1], Points->z[1]);
    dx = Points->x[1] - Points->x[0];
    dy = Points->y[1] - Points->y[0];
    dist = sqrt(dx * dx + dy * dy);

    /* trying to keep line length smaller than split_distance
     * alternative, less code: write line as soon as split_distance is exceeded
     */
    for (i = 2; i < Points->n_points; i++) {
        dx = Points->x[i] - Points->x[i - 1];
        dy = Points->y[i] - Points->y[i - 1];
        seg_dist = sqrt(dx * dx + dy * dy);
        dist += seg_dist;
        if (dist > split_distance) {
            Vect_write_line(Map, otype, OutPoints, Cats);
            Vect_reset_line(OutPoints);
            dist = seg_dist;
            Vect_append_point(OutPoints, Points->x[i - 1], Points->y[i - 1],
                              Points->z[i - 1]);
        }
        Vect_append_point(OutPoints, Points->x[i], Points->y[i], Points->z[i]);
    }
    Vect_line_prune(OutPoints);

    if (OutPoints->n_points > 1)
        Vect_write_line(Map, otype, OutPoints, Cats);

    Vect_destroy_line_struct(OutPoints);

    return 0;
}
