--#############################################################################
-- This SQL is to update a space-time raster dataset metadata
--
-- Author: Soeren Gebbert soerengebbert <at> googlemail <dot> com
-- UPDATE FROM syntax: Stefan Blumentrath stefan  <dot>  blumentrath <at> gmx <dot> de
--#############################################################################

-- SPACETIME_REGISTER_TABLE is a placeholder for specific stds map register table name (SQL compliant)
-- SPACETIME_ID is a placeholder for specific stds id: name@mapset
-- for TGIS < 3 the lines for semantic lables get replaced / commented out

<<<<<<< HEAD
UPDATE strds_metadata
   SET
       -- Update the min and max values
       number_of_semantic_labels = number_of_semantic_labels_new,
       -- Update the min and max values
       min_min = new_stats.min_min_new,
       min_max = new_stats.min_max_new,
       max_min = new_stats.max_min_new,
       max_max = new_stats.max_max_new,
       -- Update the resolution
       nsres_min = new_stats.nsres_min_new,
       nsres_max = new_stats.nsres_max_new,
       ewres_min = new_stats.ewres_min_new,
       ewres_max = new_stats.ewres_max_new
  FROM
       (SELECT
            count(distinct semantic_label) AS number_of_semantic_labels_new,
            min(min) AS min_min_new,
            max(min) AS min_max_new,
            min(max) AS max_min_new,
            max(max) AS max_max_new,
            min(nsres) AS nsres_min_new,
            max(nsres) AS nsres_max_new,
            min(ewres) AS ewres_min_new,
            max(ewres) AS ewres_max_new
        FROM
            SPACETIME_REGISTER_TABLE INNER JOIN
            raster_metadata ON
            SPACETIME_REGISTER_TABLE.id = raster_metadata.id
       ) AS new_stats
 WHERE strds_metadata.id = 'SPACETIME_ID';
=======
-- Update the min and max values
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
<<<<<<< HEAD
<<<<<<< HEAD
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
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
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
<<<<<<< HEAD
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET min_max =
       (SELECT max(min) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_min =
       (SELECT min(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET max_max =
       (SELECT max(max) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
-- Update the resolution
UPDATE strds_metadata SET nsres_min =
       (SELECT min(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET nsres_max =
       (SELECT max(nsres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
UPDATE strds_metadata SET ewres_min =
       (SELECT min(ewres) FROM raster_metadata WHERE raster_metadata.id IN
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
=======
<<<<<<< HEAD
UPDATE strds_metadata SET ewres_max = 
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    		(SELECT id FROM SPACETIME_REGISTER_TABLE)
       ) WHERE id = 'SPACETIME_ID';
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
