/*
 * pie.h
 *
 */

/* not available in SysV
 * #include "strings.h"
 */
#include <grass/gis.h>
#include "options.h"
#include "dhist.h"

/*******************************************************************
 *
 *
 *  <cell-file name> in mapset <mapset name>     <---- the title
 *
 *                    ......
 *                 ............
 *               .................
 *             .....................
 *           ........................
 *           ........................
 *           ...........*............            <----- the pie
 *           ........................
 *           ........................
 *             ....................
 *               ................
 *                 ............
 *                   .......
 *
 *   [][][][][][][][][][][][][][][][][][][][]    <---- the category
 *   ---+----+----+----+----+----+----+----+-        number legend
 *      n1   n2   n3   n4                  nn
 *
 *   Category values in <tic-mark number units>  <--- legend label
 *
 *
 *******************************************************************
 */

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
float rem(long int, long int); /* remainder function */
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
float rem(long int, long int); /* remainder function */
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
=======
float rem(long int, long int); /* remainder function */
=======
>>>>>>> osgeo-main
float rem(); /* remainder function */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
float rem(); /* remainder function */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
float rem(long int, long int); /* remainder function */
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
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
float rem(); /* remainder function */
=======
float rem(long int, long int); /* remainder function */
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
float rem(long int, long int); /* remainder function */
=======
float rem(); /* remainder function */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
float rem(); /* remainder function */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
float rem(long int, long int); /* remainder function */
=======
float rem(); /* remainder function */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
float rem(); /* remainder function */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
float rem(long int, long int); /* remainder function */
=======
float rem(); /* remainder function */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
float rem(); /* remainder function */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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

/* normalized coordinates & dimensions of pie-chart components */

/* origin */
#define ORIGIN_X    0.5
#define ORIGIN_Y    0.59

#define BAR_X1      0.13
#define BAR_X2      0.87
#define BAR_Y1      0.17
#define BAR_Y2      0.23

/* radius of pie */
#define RADIUS      0.25

/* height of legend "color-bar" */
#define BAR_HEIGHT  BAR_Y2 - BAR_Y1

/* minimum distance between numbered tic-marks on legend */
#define XTIC_DIST   40

/* sizes of legend tic-marks */
#define BIG_TIC     0.025
#define SMALL_TIC   0.015

/* y-coordinate of legend label */
#define LABEL       0.03

/* y-coordinate of legend tic-mark numbers */
#define XNUMS_Y     0.09

/* text width and height */
#define TEXT_HEIGHT 0.05
#define TEXT_WIDTH  TEXT_HEIGHT * 0.5

extern struct units tics[];
