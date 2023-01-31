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
=======
<<<<<<< HEAD
>>>>>>> main
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
