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
/****************************************************************************
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/****************************************************************************
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
/****************************************************************************
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
/****************************************************************************
=======
>>>>>>> osgeo-main
=======
/****************************************************************************
=======
>>>>>>> osgeo-main
=======
/****************************************************************************
=======
>>>>>>> osgeo-main

 /****************************************************************************
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
/****************************************************************************
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
/****************************************************************************
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
/****************************************************************************
=======

 /****************************************************************************
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
/****************************************************************************
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
 *
 * MODULE:    r.in.pdal
 *
 * AUTHOR(S): Vaclav Petras
 *
 * PURPOSE:   This file is a wrapper for a subset of Segment functions
 *
 * COPYRIGHT: (C) 2015 by Vaclav Petras and the GRASS Development Team
 *
 *            This program is free software under the GNU General Public
 *            License (>=v2). Read the file COPYING that comes with
 *            GRASS for details.
 *
 *****************************************************************************/

#ifndef GRASS_RAST_SEGMENT_H
#define GRASS_RAST_SEGMENT_H

#include <grass/raster.h>
#include <grass/segment.h>

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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
void rast_segment_open(SEGMENT *segment, const char *name,
                       RASTER_MAP_TYPE *map_type);
int rast_segment_get_value_xy(SEGMENT *base_segment,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void rast_segment_open(SEGMENT *segment, const char *name,
                       RASTER_MAP_TYPE *map_type);
int rast_segment_get_value_xy(SEGMENT *base_segment,
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
void rast_segment_open(SEGMENT * segment, const char *name,
                       RASTER_MAP_TYPE * map_type);
int rast_segment_get_value_xy(SEGMENT * base_segment,
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
void rast_segment_open(SEGMENT *segment, const char *name,
                       RASTER_MAP_TYPE *map_type);
int rast_segment_get_value_xy(SEGMENT *base_segment,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
void rast_segment_open(SEGMENT *segment, const char *name,
                       RASTER_MAP_TYPE *map_type);
int rast_segment_get_value_xy(SEGMENT *base_segment,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
                              struct Cell_head *input_region,
                              RASTER_MAP_TYPE rtype, double x, double y,
                              double *value);

#endif /* GRASS_RAST_SEGMENT_H */
