/***************************************************************************
 *
 * MODULE:     v.out.vtk
 * AUTHOR(S):  Soeren Gebbert
 *
 * PURPOSE:    v.out.vtk: writes ASCII VTK file
 *             this module is based on v.out.ascii
 * COPYRIGHT:  (C) 2000 by the GRASS Development Team
 *
 *             This program is free software under the GNU General Public
 *              License (>=v2). Read the file COPYING that comes with GRASS
 *              for details.
 *
 ****************************************************************************/

#ifndef __V_OUT_VTK_WRITE_VTK__
#define __V_OUT_VTK_WRITE_VTK__

/* the information for every vector type */
typedef struct {
    int numpoints; /* The number of points */
    int pointoffset;
    int numvertices; /* the number of vertices */
    int verticesoffset;
    int numlines; /* The number of lines */
    int lineoffset;
    int numpolygons; /* The number of polygons */
    int polygonoffset;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    int generatedata; /* If 0 the categorie data is not complete */
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
    int generatedata; /* If 0 the category data is not complete */
=======
    int generatedata; /* If 0 the categorie data is not complete */
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
    int generatedata; /* If 0 the categorie data is not complete */
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
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    int generatedata; /* If 0 the categorie data is not complete */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
} VTKTypeInfo;

/* essential vtk file information */
typedef struct {
    int maxnumpoints;        /* The max number of points */
    int maxnumvertices;      /* the max number of vertices */
    int maxnumlines;         /* The max number of lines */
    int maxnumlinepoints;    /* The max number of line points */
    int maxnumpolygons;      /* The max number of polygons */
    int maxnumpolygonpoints; /* The max number of polygon points */
    VTKTypeInfo **typeinfo;  /* The info struct for every vector type */
} VTKInfo;

/* Writes the point cooridanets for every vector type */
int write_vtk_points(FILE *ascii, struct Map_info *Map, VTKInfo *info,
                     int *type, int typenum, int dp, double scale);
/* Writes the polydata cells for every vector type */
int write_vtk_cells(FILE *ascii, struct Map_info *Map, VTKInfo *info, int *type,
                    int typenum);
/* Write the category (the first available) as cell or point data */
int write_vtk_cat_data(FILE *ascii, struct Map_info *Map, VTKInfo *info,
                       int layer, int *type, int typenum, int dp);
/* If a database connection is given, write the db data as cell or point data */
int write_vtk_db_data(FILE *ascii, struct Map_info *Map, VTKInfo *info,
                      int layer, int *type, int typenum, int dp);
#endif
