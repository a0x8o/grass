/****************************************************************************
 *
 * MODULE:       r.to.rast3elev
 *
 * AUTHOR(S):    Original author
 *               Soeren Gebbert soerengebbert@gmx.de
 *                 07 08 2006 Berlin
 * PURPOSE:      Creates a 3D volume map based on 2D elevation and value raster
 *               maps
 *
 * COPYRIGHT:    (C) 2006 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/raster3d.h>
#include <grass/glocale.h>
#include <grass/config.h>

/*- params and global variables -----------------------------------------*/
typedef struct {
    struct Option *input, *elev, *output, *upper, *lower, *tilesize;
    struct Flag *fillup, *filllow, *mask;
} paramType;

/*Data to be used */
typedef struct {
    int mapnum; /*The umber of input maps */
    int count;  /*3d raster map access counter */
    void *map;  /*The 3d voxel output map */
    int input;  /*The current raster value map pointer */
    int elev;   /*The current raster elevation map pointer */
    int inputmaptype;
    int elevmaptype;
    double upper;    /*The upper value */
    double lower;    /*The lower value */
    int useUpperVal; /*0 = use upper value, 1 = use map value to fill upper
                        cells */
    int useLowerVal; /*0 = use lower value, 1 = use map value to fill lower
                        cells */
} Database;

paramType param; /*params */

/*- prototypes --------------------------------------------------------------*/
void fatal_error(Database db, char *errorMsg); /*Simple Error message */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7131152b5c (Fix missing function prototypes (#2727))
=======
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7da05b27a8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
>>>>>>> 4f0c0751b4 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca99b767dd (Fix missing function prototypes (#2727))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9f0d2f42c1 (Fix missing function prototypes (#2727))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 285ce8b9cb (Fix missing function prototypes (#2727))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 525d31acb7 (Fix missing function prototypes (#2727))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1f70c0e30 (Fix missing function prototypes (#2727))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6ae26438a1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4137a1b10b (Fix missing function prototypes (#2727))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d0c8a37cfc (Fix missing function prototypes (#2727))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2ff4a2b4d (Fix missing function prototypes (#2727))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3aaa8eeeda (Fix missing function prototypes (#2727))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d26853320 (Fix missing function prototypes (#2727))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
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
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
void set_params(void);                         /*Fill the paramType structure */
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
void set_params(void);                         /*Fill the paramType structure */
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
void set_params();                             /*Fill the paramType structure */
=======
void set_params(void);                         /*Fill the paramType structure */
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
void set_params(void);                         /*Fill the paramType structure */
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
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
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
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
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
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
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
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
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
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
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
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
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
void set_params(void);                         /*Fill the paramType structure */
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void set_params(void);                         /*Fill the paramType structure */
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
>>>>>>> osgeo-main
void set_params();                             /*Fill the paramType structure */
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
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
void set_params(void);                         /*Fill the paramType structure */
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
void set_params();                             /*Fill the paramType structure */
=======
void set_params(void);                         /*Fill the paramType structure */
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
void set_params(void);                         /*Fill the paramType structure */
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
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
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
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
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params(void);                         /*Fill the paramType structure */
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
void set_params();                             /*Fill the paramType structure */
=======
void set_params(void);                         /*Fill the paramType structure */
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
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
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
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
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
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void set_params(void);                         /*Fill the paramType structure */
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
=======
=======
void set_params(void);                         /*Fill the paramType structure */
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ca99b767dd (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
>>>>>>> 9f0d2f42c1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
>>>>>>> 285ce8b9cb (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
>>>>>>> 525d31acb7 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
>>>>>>> f1f70c0e30 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
>>>>>>> 6ae26438a1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
>>>>>>> 4137a1b10b (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
>>>>>>> d0c8a37cfc (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
>>>>>>> f2ff4a2b4d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
>>>>>>> 3aaa8eeeda (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
>>>>>>> 8d26853320 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4f0c0751b4 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 7131152b5c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
void set_params();                             /*Fill the paramType structure */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 7da05b27a8 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
void elev_raster_to_g3d(Database db,
                        RASTER3D_Region region); /*Write the raster */
int open_input_raster_map(const char *name);     /*opens the outputmap */
void close_input_raster_map(int fd);             /*close the map */
double get_raster_value_as_double(int maptype, void *ptr, double nullval);
void check_input_maps(Database *db); /*Check input maps */

/* ************************************************************************* */
/* Get the value of the current raster pointer as double ******************* */

/* ************************************************************************* */
double get_raster_value_as_double(int MapType, void *ptr, double nullval)
{
    if (Rast_is_null_value(ptr, MapType))
        return nullval;

    switch (MapType) {
    case CELL_TYPE:
        return *(CELL *)ptr;
    case FCELL_TYPE:
        return *(FCELL *)ptr;
    case DCELL_TYPE:
        return *(DCELL *)ptr;
    default:
        return nullval;
    }
}

/* ************************************************************************* */
/* Check the input maps **************************************************** */

/* ************************************************************************* */
void check_input_maps(Database *db)
{
    int i;
    int elevcount = 0, inputcount = 0;

    G_debug(2, "Checking input maps");

    /*Check elev maps */
    if (param.elev->answers != NULL)
        for (i = 0; param.elev->answers[i] != NULL; i++)
            elevcount++;

    /*Check input maps */
    if (param.input->answers != NULL)
        for (i = 0; param.input->answers[i] != NULL; i++)
            inputcount++;

    if (elevcount != inputcount)
        G_fatal_error(_("The number of input and elevation maps is not equal"));

    db->mapnum = inputcount;

    return;
}

/* ************************************************************************* */
/* Open the raster input map *********************************************** */

/* ************************************************************************* */
int open_input_raster_map(const char *name)
{
    G_debug(3, "Open Raster file %s", name);

    return Rast_open_old(name, "");
}

/* ************************************************************************* */
/* Close the raster input map ********************************************** */

/* ************************************************************************* */
void close_input_raster_map(int fd)
{
    Rast_close(fd);
}

/* ************************************************************************* */
/* Error handling ********************************************************** */

/* ************************************************************************* */
void fatal_error(Database db, char *errorMsg)
{
    /* Close files and exit */
    if (db.map != NULL) {
        /* should unopen map here! but this functionality is not jet implemented
         */
        if (!Rast3d_close(db.map))
            Rast3d_fatal_error(_("Could not close the map"));
    }

    if (db.input)
        close_input_raster_map(db.input);

    if (db.elev)
        close_input_raster_map(db.elev);

    Rast3d_fatal_error("%s", errorMsg);
    exit(EXIT_FAILURE);
}

/* ************************************************************************* */
/* Set up the arguments **************************************************** */

/* ************************************************************************* */
void set_params(void)
{

    param.input = G_define_standard_option(G_OPT_R_INPUTS);
    param.elev = G_define_standard_option(G_OPT_R_ELEVS);
    param.output = G_define_standard_option(G_OPT_R3_OUTPUT);

    param.upper = G_define_option();
    param.upper->key = "upper";
    param.upper->type = TYPE_DOUBLE;
    param.upper->required = NO;
    param.upper->description =
        _("The value to fill the upper cells, default is null");

    param.lower = G_define_option();
    param.lower->key = "lower";
    param.lower->type = TYPE_DOUBLE;
    param.lower->required = NO;
    param.lower->description =
        _("The value to fill the lower cells, default is null");

    param.tilesize = G_define_option();
    param.tilesize->description =
        _("The maximum tile size in kilo bytes. Default is 32KB.");
    param.tilesize->key = "tilesize";
    param.tilesize->answer = "32";
    param.tilesize->type = TYPE_INTEGER;
    param.tilesize->required = NO;
    param.tilesize->multiple = NO;

    param.fillup = G_define_flag();
    param.fillup->key = 'u';
    param.fillup->description =
        _("Use the input map values to fill the upper cells");

    param.filllow = G_define_flag();
    param.filllow->key = 'l';
    param.filllow->description =
        _("Use the input map values to fill the lower cells");

    param.mask = G_define_flag();
    param.mask->key = 'm';
    param.mask->description =
        _("Use 3D raster mask (if exists) with input map");

    return;
}

/* ************************************************************************* */
/* Write the raster maps into the RASTER3D map
 * *********************************** */

/* ************************************************************************* */
void elev_raster_to_g3d(Database db, RASTER3D_Region region)
{
    int x, y, z = 0;
    int rows, cols, depths;
    void *input_rast;
    void *input_ptr;
    void *elev_rast;
    void *elev_ptr;
    double inval, value, null;
    double height, top, bottom, tbres;

    rows = region.rows;
    cols = region.cols;
    depths = region.depths;
    top = region.top;
    bottom = region.bottom;

    /*Calculate the top-bottom resolution */
    tbres = (top - bottom) / depths;

    /*memory */
    input_rast = Rast_allocate_buf(db.inputmaptype);
    elev_rast = Rast_allocate_buf(db.elevmaptype);

    Rast3d_set_null_value(&null, 1, DCELL_TYPE);

    G_debug(3,
            "elev_raster_to_g3d: Writing 3D raster map with depths %i rows %i "
            "cols %i and count %i.",
            depths, rows, cols, db.count);

    /*The mainloop */
    for (y = 0; y < rows; y++) { /* From north to south */
        G_percent(y, rows - 1, 10);

        Rast_get_row(db.input, input_rast, y, db.inputmaptype);
        Rast_get_row(db.elev, elev_rast, y, db.elevmaptype);

        for (x = 0, input_ptr = input_rast, elev_ptr = elev_rast; x < cols; x++,
            input_ptr = G_incr_void_ptr(input_ptr,
                                        Rast_cell_size(db.inputmaptype)),
            elev_ptr = G_incr_void_ptr(elev_ptr,
                                       Rast_cell_size(db.elevmaptype))) {

            /*Get the elevation and the input map value */
            inval =
                get_raster_value_as_double(db.inputmaptype, input_ptr, null);
            height = get_raster_value_as_double(db.elevmaptype, elev_ptr, null);

            G_debug(
                4,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                "Caluclating position in 3d region -> height %g with value %g",
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
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
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
                "Caluclating position in 3d region -> height %g with value %g",
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
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
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
                "Caluclating position in 3d region -> height %g with value %g",
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
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
                "Calculating position in 3d region -> height %g with value %g",
=======
                "Caluclating position in 3d region -> height %g with value %g",
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
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
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
                "Caluclating position in 3d region -> height %g with value %g",
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
                height, inval);

            /* Calculate if the RASTER3D cell is lower or upper the elevation
             * map and set the value.*/
            if (db.count == 0) {
                /*Use this method if the 3d raster map was not touched before */
                for (z = 0; z < depths; z++) {

                    /*Upper cells */
                    if (height < (z * tbres + bottom)) {
                        if (db.useUpperVal == 1)
                            value = inval; /*Input map value */
                        else
                            value = db.upper;
                    }
                    /*lower cells */
                    if (height > ((z + 1) * tbres + bottom)) {
                        if (db.useLowerVal == 1)
                            value = inval; /*Input map value */
                        else
                            value = db.lower;
                    }
                    /*If exactly at the border, fill upper AND lower cell */
                    if (height >= (z * tbres + bottom) &&
                        height <= ((z + 1) * tbres + bottom))
                        value = inval;
                    /*If the elevation is null, set the RASTER3D value null */
                    if (Rast3d_is_null_value_num(&height, DCELL_TYPE))
                        value = null;

                    /*Write the value to the 3D map */
                    if (Rast3d_put_double(db.map, x, y, z, value) < 0)
                        fatal_error(db,
                                    _("Error writing 3D raster double data"));
                }
            }
            else {
                /*Use this method for every following 3d raster maps access */
                for (z = 0; z < depths; z++) {
                    /*Upper cells */
                    if (height < (z * tbres + bottom)) {
                        if (db.useUpperVal == 1)
                            value = inval; /*Input map value */
                        else if (db.useUpperVal == 2)
                            value = db.upper;
                        else
                            value = Rast3d_get_double(db.map, x, y, z);
                    }
                    /*lower cells */
                    if (height > ((z + 1) * tbres + bottom)) {
                        if (db.useLowerVal == 1)
                            value = inval; /*Input map value */
                        else if (db.useLowerVal == 2)
                            value = db.lower;
                        else
                            value = Rast3d_get_double(db.map, x, y, z);
                    }
                    /*If exactly at the border, fill upper AND lower cell */
                    if (height >= (z * tbres + bottom) &&
                        height <= ((z + 1) * tbres + bottom))
                        value = inval;
                    /*If the elevation is null, set the RASTER3D value null */
                    if (Rast3d_is_null_value_num(&height, DCELL_TYPE))
                        value = Rast3d_get_double(db.map, x, y, z);

                    /*Write the value to the 3D map */
                    if (Rast3d_put_double(db.map, x, y, z, value) < 0)
                        fatal_error(db,
                                    _("Error writing 3D raster double data"));
                }
            }
        }
    }

    if (input_rast)
        G_free(input_rast);
    if (elev_rast)
        G_free(elev_rast);

    return;
}

/* ************************************************************************* */
/* Main function, open the raster maps and create the RASTER3D raster maps
 * ****** */

/* ************************************************************************* */
int main(int argc, char *argv[])
{
    RASTER3D_Region region;
    struct Cell_head window2d;
    struct GModule *module;
    int cols, rows, i;
    char *name = NULL;
    int changemask = 0;
    double maxSize;
    Database db;

    /*Initiate the database structure */
    db.map = NULL;
    db.input = 0;
    db.elev = 0;
    db.useUpperVal = 0;
    db.useLowerVal = 0;

    /* Initialize GRASS */
    G_gisinit(argv[0]);

    module = G_define_module();
    G_add_keyword(_("raster"));
    G_add_keyword(_("conversion"));
    G_add_keyword(_("raster3d"));
    G_add_keyword(_("voxel"));
    module->description = _(
        "Creates a 3D volume map based on 2D elevation and value raster maps.");

    /* Get parameters from user */
    set_params();

    /* Have GRASS get inputs */
    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    /*Check if maps exist */
    check_input_maps(&db);

    /* Get the tile size */
    maxSize = atoi(param.tilesize->answer);

    /*Do not use values */
    db.useUpperVal = 0;
    db.useLowerVal = 0;

    /*Use the input map value to fill the upper cells */
    if (param.fillup->answer) {
        db.useUpperVal = 1;
    }

    /*Use the input map value to fill the lower cells */
    if (param.filllow->answer) {
        db.useLowerVal = 1;
    }

    /*Set the upper value */
    if (param.upper->answer) {
        if (sscanf(param.upper->answer, "%lf", &db.upper))
            db.useUpperVal = 2;
        else
            G_fatal_error(_("The upper value is not valid"));
    }
    else {
        Rast3d_set_null_value(&db.upper, 1, DCELL_TYPE);
    }

    /*Set the lower value */
    if (param.lower->answer) {
        if (sscanf(param.lower->answer, "%lf", &db.lower))
            db.useLowerVal = 2;
        else
            G_fatal_error(_("The lower value is not valid"));
    }
    else {
        Rast3d_set_null_value(&db.lower, 1, DCELL_TYPE);
    }

    /* Figure out the current g3d region */
    Rast3d_init_defaults();
    Rast3d_get_window(&region);

    /*Check if the g3d-region is equal to the 2d rows and cols */
    rows = Rast_window_rows();
    cols = Rast_window_cols();

    G_debug(2, "Checking 2d and 3d region");

    /*If not equal, set the 2D windows correct */
    if (rows != region.rows || cols != region.cols) {
        G_message(_("The 2D and 3D region settings are different. I will use "
                    "the 3D region settings to adjust the 2D region."));
        G_get_set_window(&window2d);
        window2d.ns_res = region.ns_res;
        window2d.ew_res = region.ew_res;
        window2d.rows = region.rows;
        window2d.cols = region.cols;
        Rast_set_window(&window2d);
    }

    G_debug(2, "Open 3d raster map %s", param.output->answer);

    /*open RASTER3D output map */
    db.map = NULL;
    db.map = Rast3d_open_new_opt_tile_size(param.output->answer,
                                           RASTER3D_USE_CACHE_XY, &region,
                                           DCELL_TYPE, maxSize);

    if (db.map == NULL)
        fatal_error(db, _("Error opening 3D raster map"));

    /*if requested set the Mask on */
    if (param.mask->answer) {
        if (Rast3d_mask_file_exists()) {
            changemask = 0;
            if (Rast3d_mask_is_off(db.map)) {
                Rast3d_mask_on(db.map);
                changemask = 1;
            }
        }
    }

    G_message(_("Creating 3D raster map"));

    /*For each elevation - input map couple */
    for (i = 0; i < db.mapnum; i++) {

        G_debug(2, "Open input raster map %s", param.input->answers[i]);

        db.count = i;
        /*Open input map */
        name = param.input->answers[i];
        db.input = open_input_raster_map(name);
        db.inputmaptype = Rast_map_type(name, "");

        G_debug(2, "Open elev raster map %s", param.elev->answers[i]);

        /*Open elev map */
        name = param.elev->answers[i];
        db.elev = open_input_raster_map(name);
        db.elevmaptype = Rast_map_type(name, "");

        /****************************************/
        /*Write the data into the RASTER3D Rastermap */
        elev_raster_to_g3d(db, region);

        /*****************************************/

        /* Close files */
        close_input_raster_map(db.input);
        close_input_raster_map(db.elev);
    }

    /*We set the Mask off, if it was off before */
    if (param.mask->answer) {
        if (Rast3d_mask_file_exists())
            if (Rast3d_mask_is_on(db.map) && changemask)
                Rast3d_mask_off(db.map);
    }

    G_debug(2, "Close 3d raster map");

    /* Flush all tile */
    if (!Rast3d_flush_all_tiles(db.map))
        Rast3d_fatal_error("Error flushing tiles with Rast3d_flush_all_tiles");
    if (!Rast3d_close(db.map))
        Rast3d_fatal_error(_("Error closing 3d raster map"));

    G_debug(2, "\nDone\n");

    return (EXIT_SUCCESS);
}
