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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28e7b3b34d (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4eab8f90cb (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1e595a59e6 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cdd2375514 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1cabd030d3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b339c662ab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
>>>>>>> 6007b09add (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81fd408422 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7b9fb7e19e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
UPDATE strds_metadata SET ewres_max =
       (SELECT max(ewres) FROM raster_metadata WHERE raster_metadata.id IN
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
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
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
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
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
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
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
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
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
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
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
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
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
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
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
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
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
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
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
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
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
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
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
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
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
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
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
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
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
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
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
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
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
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
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
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
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
UPDATE strds_metadata SET min_min = 
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN 
=======
UPDATE strds_metadata SET min_min =
       (SELECT min(min) FROM raster_metadata WHERE raster_metadata.id IN
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
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
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
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
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
