/******************************************************************************
 *
 * MODULE:       v.db.select
 *
 * AUTHOR(S):    Radim Blazek
 *               OGR support by Martin Landa <landa.martin gmail.com>
 *               -e, -j, and -f flags by Huidae Cho <grass4u gmail.com>
 *               group option by Luca Delucchi <lucadeluge gmail.com>
 *               CSV and format option by Vaclav Petras <wenzeslaus gmail com>
 *
 * PURPOSE:      Print vector attributes
 *
 * COPYRIGHT:    (C) 2005-2021 by the GRASS Development Team
 *
 *               This program is free software under the GNU General
 *               Public License (>=v2). Read the file COPYING that
 *               comes with GRASS for details.
 *
 *****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#include <grass/glocale.h>
#include <grass/gis.h>
#include <grass/vector.h>
#include <grass/dbmi.h>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
=======
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
>>>>>>> main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
enum OutputFormat {
    PLAIN,
    JSON,
    CSV,
    VERTICAL
};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
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
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
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
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
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
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
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
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
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
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
enum OutputFormat { PLAIN, JSON, CSV, VERTICAL };
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))

void fatal_error_option_value_excludes_flag(struct Option *option,
                                            struct Flag *excluded,
                                            const char *because)
{
    if (!excluded->answer)
        return;
    G_fatal_error(_("The flag -%c is not allowed with %s=%s. %s"),
                  excluded->key, option->key, option->answer, because);
}

void fatal_error_option_value_excludes_option(struct Option *option,
                                              struct Option *excluded,
                                              const char *because)
{
    if (!excluded->answer)
        return;
    G_fatal_error(_("The option %s is not allowed with %s=%s. %s"),
                  excluded->key, option->key, option->answer, because);
}

int main(int argc, char **argv)
{
    struct GModule *module;
    struct {
        struct Option *map;
        struct Option *field;
        struct Option *format;
        struct Option *fsep;
        struct Option *vsep;
        struct Option *nullval;
        struct Option *cols;
        struct Option *where;
        struct Option *file;
        struct Option *group;
    } options;
    struct {
        struct Flag *region;
        struct Flag *colnames;
        struct Flag *vertical;
        struct Flag *escape;
        struct Flag *features;
    } flags;
    dbDriver *driver;
    dbString sql, value_string;
    dbCursor cursor;
    dbTable *table;
    dbColumn *column;
    dbValue *value;
    struct field_info *Fi;
    int ncols, col, more;
    bool first_rec;
    struct Map_info Map;
    char query[DB_SQL_MAX];
    struct ilist *list_lines;
    char *fsep, *vsep;
    struct bound_box *min_box, *line_box;
    int i, line, area, cat, field_number;
    bool init_box;
    enum OutputFormat format;
    bool vsep_needs_newline;

    module = G_define_module();
    G_add_keyword(_("vector"));
    G_add_keyword(_("attribute table"));
    G_add_keyword(_("database"));
    G_add_keyword(_("SQL"));
    G_add_keyword(_("export"));
    module->description = _("Prints vector map attributes.");

    options.map = G_define_standard_option(G_OPT_V_MAP);
    options.map->guisection = _("Main");

    options.field = G_define_standard_option(G_OPT_V_FIELD);
    options.field->guisection = _("Selection");

    options.cols = G_define_standard_option(G_OPT_DB_COLUMNS);
    options.cols->guisection = _("Selection");

    options.where = G_define_standard_option(G_OPT_DB_WHERE);
    options.where->guisection = _("Selection");

    options.group = G_define_option();
    options.group->key = "group";
    options.group->required = NO;
    options.group->description =
        _("GROUP BY conditions of SQL statement without 'group by' keyword");
    options.group->guisection = _("Selection");

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
    options.format = G_define_standard_option(G_OPT_F_FORMAT);
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
    options.format = G_define_standard_option(G_OPT_F_FORMAT);
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
    options.format = G_define_option();
    options.format->key = "format";
    options.format->type = TYPE_STRING;
    options.format->required = YES;
    options.format->label = _("Output format");
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
    options.format->options = "plain,csv,json,vertical";
    options.format->descriptions =
        "plain;Configurable plain text output;"
        "csv;CSV (Comma Separated Values);"
        "json;JSON (JavaScript Object Notation);"
        "vertical;Plain text vertical output (instead of horizontal)";
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
    options.format->answer = "plain";
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
    options.format->answer = "plain";
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
=======
    options.format->answer = "plain";
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
    options.format->guisection = _("Format");

    options.fsep = G_define_standard_option(G_OPT_F_SEP);
    options.fsep->answer = NULL;
    options.fsep->guisection = _("Format");

    options.vsep = G_define_standard_option(G_OPT_F_SEP);
    options.vsep->key = "vertical_separator";
    options.vsep->label = _("Output vertical record separator");
    options.vsep->answer = NULL;
    options.vsep->guisection = _("Format");

    options.nullval = G_define_standard_option(G_OPT_M_NULL_VALUE);
    options.nullval->guisection = _("Format");

    options.file = G_define_standard_option(G_OPT_F_OUTPUT);
    options.file->key = "file";
    options.file->required = NO;
    options.file->guisection = _("Main");
    options.file->description =
        _("Name for output file (if omitted or \"-\" output to stdout)");

    flags.region = G_define_flag();
    flags.region->key = 'r';
    flags.region->description = _("Print minimal region extent of selected "
                                  "vector features instead of attributes");
    flags.region->guisection = _("Region");

    flags.colnames = G_define_flag();
    flags.colnames->key = 'c';
    flags.colnames->description = _("Do not include column names in output");
    flags.colnames->guisection = _("Format");

    flags.escape = G_define_flag();
    flags.escape->key = 'e';
    flags.escape->description = _("Escape newline and backslash characters");
    flags.escape->guisection = _("Format");

    flags.features = G_define_flag();
    flags.features->key = 'f';
    flags.features->description =
        _("Exclude attributes not linked to features");
    flags.features->guisection = _("Selection");

    G_gisinit(argv[0]);

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    /* set input vector map name and mapset */
    if (options.file->answer && strcmp(options.file->answer, "-") != 0) {
        if (NULL == freopen(options.file->answer, "w", stdout))
            G_fatal_error(_("Unable to open file <%s> for writing"),
                          options.file->answer);
    }

    if (strcmp(options.format->answer, "csv") == 0)
        format = CSV;
    else if (strcmp(options.format->answer, "json") == 0)
        format = JSON;
    else if (strcmp(options.format->answer, "vertical") == 0)
        format = VERTICAL;
    else
        format = PLAIN;
    if (format == JSON) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
        fatal_error_option_value_excludes_flag(
            options.format, flags.escape, _("Escaping is based on the format"));
        fatal_error_option_value_excludes_flag(
            options.format, flags.colnames,
            _("Column names are always included"));
        fatal_error_option_value_excludes_option(
            options.format, options.fsep, _("Separator is part of the format"));
        fatal_error_option_value_excludes_option(
            options.format, options.nullval,
            _("Null value is part of the format"));
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
    }
    if (format != VERTICAL) {
        fatal_error_option_value_excludes_option(
            options.format, options.vsep,
            _("Only vertical output can use vertical separator"));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> main
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
        fatal_error_option_value_excludes_flag(options.format, flags.escape,
                                               _("Escaping is based on the format"));
        fatal_error_option_value_excludes_flag(options.format, flags.colnames,
                                               _("Column names are always included"));
        fatal_error_option_value_excludes_option(options.format, options.fsep,
                                                 _("Separator is part of the format"));
        fatal_error_option_value_excludes_option(options.format, options.nullval,
                                                 _("Null value is part of the format"));
    }
    if (format != VERTICAL) {
        fatal_error_option_value_excludes_option(options.format, options.vsep,
                                                 _("Only vertical output can use vertical separator"));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
    }
    if (format != VERTICAL) {
        fatal_error_option_value_excludes_option(
            options.format, options.vsep,
            _("Only vertical output can use vertical separator"));
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
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
    }
    if (format != VERTICAL) {
        fatal_error_option_value_excludes_option(
            options.format, options.vsep,
            _("Only vertical output can use vertical separator"));
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
    }
    if (format != VERTICAL) {
        fatal_error_option_value_excludes_option(
            options.format, options.vsep,
            _("Only vertical output can use vertical separator"));
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
    }
    if (format != VERTICAL) {
        fatal_error_option_value_excludes_option(
            options.format, options.vsep,
            _("Only vertical output can use vertical separator"));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> osgeo-main
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
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
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
    }

    min_box = line_box = NULL;
    list_lines = NULL;

    if (flags.region->answer) {
        min_box = (struct bound_box *)G_malloc(sizeof(struct bound_box));
        G_zero((void *)min_box, sizeof(struct bound_box));

        line_box = (struct bound_box *)G_malloc(sizeof(struct bound_box));
    }

    if (flags.region->answer || flags.features->answer)
        list_lines = Vect_new_list();

    /* the field separator */
    if (options.fsep->answer) {
        fsep = G_option_to_separator(options.fsep);
    }
    else {
        /* A different separator is needed to for each format and output. */
        if (format == CSV) {
            fsep = G_store(",");
        }
        else if (format == PLAIN || format == VERTICAL) {
            if (flags.region->answer)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
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
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
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
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
                fsep = G_store("=");
            else
                fsep = G_store("|");
        }
        else
            fsep = NULL; /* Something like a separator is part of the format. */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
=======
                fsep = G_store("=");
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
            else
                fsep = G_store("|");
        }
        else
<<<<<<< HEAD
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
            fsep = NULL; /* Something like a separator is part of the format. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
               fsep = G_store("=");
            else
               fsep = G_store("|");
        }
        else
            fsep = NULL;  /* Something like a separator is part of the format. */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
    }
    if (options.vsep->answer)
        vsep = G_option_to_separator(options.vsep);
    else
        vsep = NULL;
    vsep_needs_newline = true;
    if (vsep && !strcmp(vsep, "\n"))
        vsep_needs_newline = false;

    db_init_string(&sql);
    db_init_string(&value_string);

    /* open input vector */
    if (flags.region->answer || flags.features->answer) {
        if (2 > Vect_open_old2(&Map, options.map->answer, "",
                               options.field->answer)) {
            Vect_close(&Map);
            G_fatal_error(_("Unable to open vector map <%s> at topology level. "
                            "Flag '%c' requires topology level."),
                          options.map->answer, flags.region->key);
        }
        field_number = Vect_get_field_number(&Map, options.field->answer);
    }
    else {
        if (Vect_open_old_head2(&Map, options.map->answer, "",
                                options.field->answer) < 0)
            G_fatal_error(_("Unable to open vector map <%s>"),
                          options.map->answer);
        /* field_number won't be used, but is initialized to suppress compiler
         * warnings. */
        field_number = -1;
    }

    if ((Fi = Vect_get_field2(&Map, options.field->answer)) == NULL)
        G_fatal_error(_("Database connection not defined for layer <%s>"),
                      options.field->answer);

    driver = db_start_driver_open_database(Fi->driver, Fi->database);

    if (!driver)
        G_fatal_error(_("Unable to open database <%s> by driver <%s>"),
                      Fi->database, Fi->driver);
    db_set_error_handler_driver(driver);

    if (options.cols->answer)
        sprintf(query, "SELECT %s FROM ", options.cols->answer);
    else
        sprintf(query, "SELECT * FROM ");

    db_set_string(&sql, query);
    db_append_string(&sql, Fi->table);

    if (options.where->answer) {
        char *buf = NULL;

        buf = G_malloc((strlen(options.where->answer) + 8));
        sprintf(buf, " WHERE %s", options.where->answer);
        db_append_string(&sql, buf);
        G_free(buf);
    }

    if (options.group->answer) {
        char *buf = NULL;

        buf = G_malloc((strlen(options.group->answer) + 8));
        sprintf(buf, " GROUP BY %s", options.group->answer);
        db_append_string(&sql, buf);
        G_free(buf);
    }

    if (db_open_select_cursor(driver, &sql, &cursor, DB_SEQUENTIAL) != DB_OK)
        G_fatal_error(_("Unable to open select cursor"));

    table = db_get_cursor_table(&cursor);
    ncols = db_get_table_number_of_columns(table);

    /* column names if horizontal output (ignore for -r, -c, JSON, vertical) */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
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
<<<<<<< HEAD
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> osgeo-main
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
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
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
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
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
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
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
=======
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
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> osgeo-main
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> osgeo-main
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
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
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
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
=======
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> osgeo-main
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
    if (!flags.region->answer && !flags.colnames->answer && format != JSON &&
        format != VERTICAL) {
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
    if (!flags.region->answer && !flags.colnames->answer &&
        format != JSON && format != VERTICAL) {
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
        for (col = 0; col < ncols; col++) {
            column = db_get_table_column(table, col);
            if (col)
                fprintf(stdout, "%s", fsep);
            fprintf(stdout, "%s", db_get_column_name(column));
        }
        fprintf(stdout, "\n");
    }

    init_box = true;
    first_rec = true;

    if (format == JSON) {
        if (flags.region->answer)
            fprintf(stdout, "{\"extent\":\n");
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        else
            fprintf(stdout, "{\"records\":[\n");
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
        else
            fprintf(stdout, "{\"records\":[\n");
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
        else
            fprintf(stdout, "{\"records\":[\n");
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
        else {
            fprintf(stdout, "{\"info\":\n{\"columns\":[\n");
            for (col = 0; col < ncols; col++) {
                column = db_get_table_column(table, col);
                if (col)
                    fprintf(stdout, "},\n");
                fprintf(stdout, "{\"name\":\"%s\",",
                        db_get_column_name(column));
                int sql_type = db_get_column_sqltype(column);
                fprintf(stdout, "\"sql_type\":\"%s\",",
                        db_sqltype_name(sql_type));

                int c_type = db_sqltype_to_Ctype(sql_type);
                fprintf(stdout, "\"is_number\":");
                /* Same rules as for quoting, i.e., number only as
                 * JSON or Python would see it and not numeric which may
                 * include, e.g., date. */
                if (c_type == DB_C_TYPE_INT || c_type == DB_C_TYPE_DOUBLE)
                    fprintf(stdout, "true");
                else
                    fprintf(stdout, "false");
            }

            fprintf(stdout, "}\n]},\n");
            fprintf(stdout, "\"records\":[\n");
        }
=======
        else
            fprintf(stdout, "{\"records\":[\n");
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
        else
            fprintf(stdout, "{\"records\":[\n");
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
        else
            fprintf(stdout, "{\"records\":[\n");
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
        else
            fprintf(stdout, "{\"records\":[\n");
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
        else
            fprintf(stdout, "{\"records\":[\n");
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
    }

    /* fetch the data */
    while (1) {
        if (db_fetch(&cursor, DB_NEXT, &more) != DB_OK)
            G_fatal_error(_("Unable to fetch data from table <%s>"), Fi->table);

        if (!more)
            break;

        if (first_rec)
            first_rec = false;
        else if (!flags.region->answer && format == JSON)
            fprintf(stdout, ",\n");

        cat = -1;
        for (col = 0; col < ncols; col++) {
            column = db_get_table_column(table, col);
            value = db_get_column_value(column);

            if (cat < 0 && strcmp(Fi->key, db_get_column_name(column)) == 0) {
                cat = db_get_value_int(value);
                if (flags.region->answer)
                    break;
            }

            if (flags.region->answer)
                continue;

            if (flags.features->answer) {
                Vect_cidx_find_all(&Map, field_number, ~GV_AREA, cat,
                                   list_lines);
                /* if no features are found for this category, don't print
                 * anything. */
                if (list_lines->n_values == 0)
                    break;
            }

            db_convert_column_value_to_string(column, &value_string);

            if (!flags.colnames->answer && format == VERTICAL)
                fprintf(stdout, "%s%s", db_get_column_name(column), fsep);

            if (col && format != JSON && format != VERTICAL)
                fprintf(stdout, "%s", fsep);

            if (format == JSON) {
                if (!col)
                    fprintf(stdout, "{");
                fprintf(stdout, "\"%s\":", db_get_column_name(column));
            }

            if (db_test_value_isnull(value)) {
                if (format == JSON)
                    fprintf(stdout, "null");
                else if (options.nullval->answer)
                    fprintf(stdout, "%s", options.nullval->answer);
            }
            else {
                char *str = db_get_string(&value_string);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                /* Escaped charcters in different formats
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
                /* Escaped charcters in different formats
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
<<<<<<< HEAD
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
                /* Escaped charcters in different formats
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
                /* Escaped characters in different formats
=======
                /* Escaped charcters in different formats
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> osgeo-main
=======
=======
                /* Escaped charcters in different formats
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Escaped charcters in different formats
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
                 * JSON (mandatory): \" \\ \r \n \t \f \b
                 * CSV (usually none, here optional): \\ \r \n \t \f \b
                 * Plain, vertical (optional): v7: \\ \r \n, v8 also: \t \f \b
                 */
                if (flags.escape->answer || format == JSON) {
                    if (strchr(str, '\\'))
                        str = G_str_replace(str, "\\", "\\\\");
                    if (strchr(str, '\r'))
                        str = G_str_replace(str, "\r", "\\r");
                    if (strchr(str, '\n'))
                        str = G_str_replace(str, "\n", "\\n");
                    if (strchr(str, '\t'))
                        str = G_str_replace(str, "\t", "\\t");
                    if (format == JSON && strchr(str, '"'))
                        str = G_str_replace(str, "\"", "\\\"");
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
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
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
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
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
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
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3dbf181f4a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3a39def153 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a1668d1b51 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 222e9db261 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ddd3218bfa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0f3e7ebb9c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fe9d137f79 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e528a47086 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c428eb98e4 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8ce884c47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 68958c7a1d (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 45f66daea7 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5b0d02a49f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> db749a0f62 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3141a6d48c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7f8e88ce75 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6f0f0fccf8 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 271754f563 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 42b1ba8521 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 67828de44a (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f1ad29e40c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c3d683896b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 39e3ee1d76 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 082b691b21 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 965183f78e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 3b180b69dc (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 0443c5dcb3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e5197de8d9 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e19e0046cb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e3be277cdf (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 75d9311c15 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 742b9484af (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 809d5f89eb (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> bc5eada47f (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c06825b488 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 988f80e605 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 05a8ed60c3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9bac2dde2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 7b90f7974c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 11b0593037 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 64d806ca5d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 85cc1167d0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5392ccd487 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> aa8b33015c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f8d608e69c (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46a71dc1f2 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5faac46788 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 35e6a92378 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> c6c8508517 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5019051b97 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 36c7b9e5de (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d673014324 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 99a8c96662 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 71a9287dd3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f9ae3b2f80 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8762e8a9d6 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e8af397a46 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 8c4bd4121e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cfcd5b1277 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 119d2c3497 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eeba252ad6 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b9a5537334 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 66396a47ed (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc1d729f83 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 58bb426d95 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> fc13117aec (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 21cd7af3aa (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 51073398a5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 611837a6a7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> ea42b10fac (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 82d549ef1b (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5696c23d46 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 19134012b7 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> b0ec89ca25 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 82c27043ba (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 1d791bc156 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6b1ac5a234 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> e98321d514 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> f2c67646fd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 290b426053 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> dee46b522d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> add85036f3 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 46043e6899 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d00e4a3f7c (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 29d48abc97 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 5a9d1aa9f5 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 866f2dbd13 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 9e96540c0b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 729c1b17f8 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d7b5d9cf78 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 77081d5e9a (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 12a24d0ffd (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 4178ebd75e (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 6510fbe5c0 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> eea17500b3 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> a41c6b59f1 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
=======
                    if (strchr(str, '\f')) /* form feed, somewhat unlikely */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b')) /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
<<<<<<< HEAD
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59b367cd2d (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> cb1a2a4144 (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 59f0722420 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 04cd7ecc3b (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
                /* Common CSV does not escape, but doubles quotes (and we quote
                 * all text fields which takes care of a separator character in
                 * text). */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
                    if (strchr(str, '\f'))  /* form feed, somewhat unlikely */
                        str = G_str_replace(str, "\f", "\\f");
                    if (strchr(str, '\b'))  /* backspace, quite unlikely */
                        str = G_str_replace(str, "\b", "\\b");
                }
                /* Common CSV does not escape, but doubles quotes (and we quote all
                 * text fields which takes care of a separator character in text). */
<<<<<<< HEAD
>>>>>>> fbc5f37844 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> d658b14f51 (WMS: replace broken URLs with alternative WMS (#1635))
<<<<<<< HEAD
>>>>>>> 332e06673e (WMS: replace broken URLs with alternative WMS (#1635))
=======
=======
=======
>>>>>>> 4d944b87c5 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 451daadac7 (WMS: replace broken URLs with alternative WMS (#1635))
>>>>>>> 455422fde6 (WMS: replace broken URLs with alternative WMS (#1635))
                if (format == CSV && strchr(str, '"')) {
                    str = G_str_replace(str, "\"", "\"\"");
                }

                if (format == JSON || format == CSV) {
                    int type =
                        db_sqltype_to_Ctype(db_get_column_sqltype(column));

                    /* Don't quote numbers, quote text and datetime. */
                    if (type == DB_C_TYPE_INT || type == DB_C_TYPE_DOUBLE)
                        fprintf(stdout, "%s", str);
                    else
                        fprintf(stdout, "\"%s\"", str);
                }
                else
                    fprintf(stdout, "%s", str);
            }

            if (format == VERTICAL)
                fprintf(stdout, "\n");
            else if (format == JSON) {
                if (col < ncols - 1)
                    fprintf(stdout, ",");
                else
                    fprintf(stdout, "}");
            }
        }

        if (flags.features->answer && col < ncols)
            continue;

        if (flags.region->answer) {
            /* get minimal region extent */
            Vect_cidx_find_all(&Map, field_number, ~GV_AREA, cat, list_lines);
            for (i = 0; i < list_lines->n_values; i++) {
                line = list_lines->value[i];
                if (Vect_get_line_type(&Map, line) == GV_CENTROID) {
                    area = Vect_get_centroid_area(&Map, line);
                    if (area > 0 && !Vect_get_area_box(&Map, area, line_box))
                        G_fatal_error(
                            _("Unable to get bounding box of area %d"), area);
                }
                else if (!Vect_get_line_box(&Map, line, line_box))
                    G_fatal_error(_("Unable to get bounding box of line %d"),
                                  line);
                if (init_box) {
                    Vect_box_copy(min_box, line_box);
                    init_box = false;
                }
                else
                    Vect_box_extend(min_box, line_box);
            }
        }
        else {
            /* End of record in attribute printing */
            if (format != JSON && format != VERTICAL)
                fprintf(stdout, "\n");
            else if (vsep) {
                if (vsep_needs_newline)
                    fprintf(stdout, "%s\n", vsep);
                else
                    fprintf(stdout, "%s", vsep);
            }
        }
    }

    if (!flags.region->answer && format == JSON)
        fprintf(stdout, "\n]}\n");

    if (flags.region->answer) {
        if (format == CSV) {
            fprintf(stdout, "n%ss%sw%se", fsep, fsep, fsep);
            if (Vect_is_3d(&Map)) {
                fprintf(stdout, "%st%sb", fsep, fsep);
            }
            fprintf(stdout, "\n");
            fprintf(stdout, "%f%s%f%s%f%s%f", min_box->N, fsep, min_box->S,
                    fsep, min_box->W, fsep, min_box->E);
            if (Vect_is_3d(&Map)) {
                fprintf(stdout, "%s%f%s%f", fsep, min_box->T, fsep, min_box->B);
            }
            fprintf(stdout, "\n");
        }
        else if (format == JSON) {
            fprintf(stdout, "{");
            fprintf(stdout, "\"n\":%f,", min_box->N);
            fprintf(stdout, "\"s\":%f,", min_box->S);
            fprintf(stdout, "\"w\":%f,", min_box->W);
            fprintf(stdout, "\"e\":%f", min_box->E);
            if (Vect_is_3d(&Map)) {
                fprintf(stdout, ",\"t\":%f,", min_box->T);
                fprintf(stdout, "\"b\":%f", min_box->B);
            }
            fprintf(stdout, "\n}}\n");
        }
        else {
            fprintf(stdout, "n%s%f\n", fsep, min_box->N);
            fprintf(stdout, "s%s%f\n", fsep, min_box->S);
            fprintf(stdout, "w%s%f\n", fsep, min_box->W);
            fprintf(stdout, "e%s%f\n", fsep, min_box->E);
            if (Vect_is_3d(&Map)) {
                fprintf(stdout, "t%s%f\n", fsep, min_box->T);
                fprintf(stdout, "b%s%f\n", fsep, min_box->B);
            }
        }
        fflush(stdout);

        G_free((void *)min_box);
        G_free((void *)line_box);

        Vect_destroy_list(list_lines);
    }

    db_close_cursor(&cursor);
    db_close_database_shutdown_driver(driver);
    Vect_close(&Map);

    exit(EXIT_SUCCESS);
}
