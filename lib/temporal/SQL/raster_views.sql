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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
            FROM raster_base A1, raster_absolute_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
=======
            FROM raster_base A1, raster_absolute_time A2, 
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
            FROM raster_base A1, raster_absolute_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_absolute_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            FROM raster_base A1, raster_absolute_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
            FROM raster_base A1, raster_relative_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
=======
            FROM raster_base A1, raster_relative_time A2, 
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
            FROM raster_base A1, raster_relative_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2,
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
            FROM raster_base A1, raster_relative_time A2, 
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
            FROM raster_base A1, raster_relative_time A2,
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
            raster_spatial_extent A3, raster_metadata A4,
            raster_stds_register A5
            WHERE A1.id = A2.id AND A1.id = A3.id AND
            A1.id = A4.id AND A1.id = A5.id;
