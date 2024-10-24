--#############################################################################
-- This SQL script generates two views to access all map specific tables.
--
-- Author: Soeren Gebbert soerengebbert <at> googlemail <dot> com
--#############################################################################


-- Create the views to access all cols for the absolute and relative time

CREATE VIEW raster_view_abs_time AS SELECT
            A1.id, A1.mapset,
            A1.name, A1.temporal_type,
            A1.creation_time,
            A1.creator,
            A2.start_time, A2.end_time,
            A3.north, A3.south, A3.east, A3.west, A3.bottom, A3.top, A3.proj,
            A4.datatype, A4.cols, A4.rows,
            A4.nsres, A4.ewres, A4.min, A4.max,
            A4.number_of_cells, A4.semantic_label, A5.registered_stds
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
            FROM raster_base A1, raster_absolute_time A2,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            FROM raster_base A1, raster_absolute_time A2,
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_absolute_time A2,
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
            FROM raster_base A1, raster_absolute_time A2, 
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
            FROM raster_base A1, raster_absolute_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
            raster_spatial_extent A3, raster_metadata A4,
            raster_stds_register A5
            WHERE A1.id = A2.id AND A1.id = A3.id AND
            A1.id = A4.id AND A1.id = A5.id;

CREATE VIEW raster_view_rel_time AS SELECT
            A1.id, A1.mapset,
            A1.name, A1.temporal_type,
            A1.creation_time,
            A1.creator,
            A2.start_time, A2.end_time, A2.unit,
            A3.north, A3.south, A3.east, A3.west, A3.bottom, A3.top, A3.proj,
            A4.datatype, A4.cols, A4.rows,
            A4.nsres, A4.ewres, A4.min, A4.max,
            A4.number_of_cells, A4.semantic_label, A5.registered_stds
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
            FROM raster_base A1, raster_relative_time A2,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            FROM raster_base A1, raster_relative_time A2,
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
            FROM raster_base A1, raster_relative_time A2,
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
            FROM raster_base A1, raster_relative_time A2, 
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
            FROM raster_base A1, raster_relative_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
            raster_spatial_extent A3, raster_metadata A4,
            raster_stds_register A5
            WHERE A1.id = A2.id AND A1.id = A3.id AND
            A1.id = A4.id AND A1.id = A5.id;
