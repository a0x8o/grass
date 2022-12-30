/*!
   \file lib/gis/file_name.c

   \brief GIS library - Determine GRASS data base file name

   (C) 2001-2015 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Original author CERL
 */

#include <string.h>
#include <stdlib.h>
#include <grass/gis.h>

#include "gis_local_proto.h"

static char *file_name(char *, const char *, const char *, const char *,
                       const char *, const char *);
static void append_char(char *, char);

/*!
   \brief Builds full path names to GIS data files

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 6aa010c28c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> e4f78d0976 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 74c93c5cf9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
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
<<<<<<< HEAD
>>>>>>> 6115a08197 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 07d94d7b38 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 9472540a75 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> ce63d8d35a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> d04dea00b0 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> d629338063 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 33d0aafa36 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> f14457be8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 953825a892 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 037caabfd6 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 943d9f04d9 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
>>>>>>> fae8071192 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
=======
<<<<<<< HEAD
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 953825a892 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 943d9f04d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 33d0aafa36 (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6dd43833fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 86cf92e040 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6aa010c28c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
<<<<<<< HEAD
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> e4f78d0976 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 74c93c5cf9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 6115a08197 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
<<<<<<< HEAD
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 07d94d7b38 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 9472540a75 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> ce63d8d35a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> d04dea00b0 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> d629338063 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 33d0aafa36 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> f14457be8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 953825a892 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 037caabfd6 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 943d9f04d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6dd43833fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> ccdaf75290 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> fae8071192 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
<<<<<<< HEAD
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  If <i>name</i> is of the form "nnn@ppp" then path is set as if name
  had been "nnn" and mapset had been "ppp" (mapset parameter itself is
  ignored in this case).
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

<<<<<<< HEAD
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
  \param[out] path allocated buffer to hold resultant full path to file
  \param element database element (eg, "cell", "cellhd", "vector", etc)
  \param name name of file to build path to (fully qualified names allowed)
  \param mapset mapset name
>>>>>>> 6dd43833fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6aa010c28c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 33d0aafa36 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953825a892 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 943d9f04d9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> fae8071192 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
   If <i>name</i> is of the form "nnn@ppp" then path is set as if name
   had been "nnn" and mapset had been "ppp" (mapset parameter itself is
   ignored in this case).
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6aa010c28c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4f78d0976 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 74c93c5cf9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6115a08197 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 07d94d7b38 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9472540a75 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ce63d8d35a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d04dea00b0 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d629338063 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 33d0aafa36 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f14457be8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 953825a892 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 037caabfd6 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 943d9f04d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> fae8071192 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))

   Paths to files are currently in form:
   /path/to/location/mapset/element/name

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name(path, "fcell", "my_raster", "my_mapset");
   // path now is "/full/path/to/my_mapset/fcell/my_raster"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name(path, "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/elem/name
   @endcode

   \param[out] path allocated buffer to hold resultant full path to file
   \param element database element (eg, "cell", "cellhd", "vector", etc)
   \param name name of file to build path to (fully qualified names allowed)
   \param mapset mapset name

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
   \param[out] path allocated buffer to hold resultant full path to file
   \param element database element (eg, "cell", "cellhd", "vector", etc)
   \param name name of file to build path to (fully qualified names allowed)
   \param mapset mapset name

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
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
   \param[out] path allocated buffer to hold resultant full path to file
   \param element database element (eg, "cell", "cellhd", "vector", etc)
   \param name name of file to build path to (fully qualified names allowed)
   \param mapset mapset name

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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
   \param[out] path allocated buffer to hold resultant full path to file
   \param element database element (eg, "cell", "cellhd", "vector", etc)
   \param name name of file to build path to (fully qualified names allowed)
   \param mapset mapset name

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
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
   \param[out] path allocated buffer to hold resultant full path to file
   \param element database element (eg, "cell", "cellhd", "vector", etc)
   \param name name of file to build path to (fully qualified names allowed)
   \param mapset mapset name

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
   \return pointer to <i>path</i> buffer
 */
char *G_file_name(char *path, const char *element, const char *name,
                  const char *mapset)
{
    return file_name(path, NULL, element, name, mapset, NULL);
}

/*!
   \brief Builds full path names to GIS misc data files

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 86cf92e040 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 6aa010c28c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4f78d0976 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 74c93c5cf9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6115a08197 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 07d94d7b38 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9472540a75 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ce63d8d35a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d04dea00b0 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d629338063 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
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
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
>>>>>>> osgeo-main
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6dd43833fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 86cf92e040 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6aa010c28c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ccdaf75290 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
>>>>>>> fae8071192 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> e4f78d0976 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 74c93c5cf9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 6115a08197 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 07d94d7b38 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 9472540a75 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> ce63d8d35a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> d04dea00b0 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> d629338063 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 33d0aafa36 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> f14457be8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 953825a892 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 037caabfd6 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 943d9f04d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6dd43833fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> ccdaf75290 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> fae8071192 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
=======
  Paths to misc files are currently in form:
  /path/to/location/mapset/dir/name/element
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

<<<<<<< HEAD
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
  \param[out] path allocated buffer to hold resultant full path to file
  \param dir misc directory (e.g., "cell_misc", "group")
  \param element database element (in this case – file to build path to e.g., "history", "REF")
  \param name name of object (raster, group; fully qualified names allowed e.g., "my_raster@PERMANENT")
  \param mapset mapset name
>>>>>>> 6dd43833fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6aa010c28c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 33d0aafa36 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 953825a892 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 943d9f04d9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> fae8071192 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
   Paths to misc files are currently in form:
   /path/to/location/mapset/dir/name/element
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6aa010c28c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8614616900 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ea5d53b6b9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 37d32904d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a8d52f876 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2f50bc0852 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b15c601d56 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6b422433a6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 02f7a8e9af (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b68dfa8313 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4f78d0976 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f56d06b627 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 74c93c5cf9 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 53ec9c1d9c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6115a08197 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> f24e9a2df1 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 07d94d7b38 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 967c826c3c (Improve G_open|find _misc function documentation (#1760))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9472540a75 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 042c2ebe6c (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ce63d8d35a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 236bd3862e (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d04dea00b0 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 1fa70da29d (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d629338063 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> aeb0ef40a8 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b7542e1a5a (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> b0b2482a64 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 33d0aafa36 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f14457be8f (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 953825a892 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 037caabfd6 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 943d9f04d9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fe6c05cdfc (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> fae8071192 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 913353db8f (Improve G_open|find _misc function documentation (#1760))
>>>>>>> d093457878 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8fbe1fc408 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 1f6e800d59 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a12132efd9 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> b2183bf70a (Improve G_open|find _misc function documentation (#1760))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8882b01eef (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 83b8fc7df9 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c5cda9f071 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> b340b436b9 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5ee893ff88 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 50cae84486 (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 611b91cfb6 (Improve G_open|find _misc function documentation (#1760))
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
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> d5a2b4a9fd (Improve G_open|find _misc function documentation (#1760))
<<<<<<< HEAD
>>>>>>> 6acc4586c3 (Improve G_open|find _misc function documentation (#1760))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5b1a121e4b (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 54418965c6 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5331444a64 (Improve G_open|find _misc function documentation (#1760))
>>>>>>> 4a0c628589 (Improve G_open|find _misc function documentation (#1760))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))

   path input buffer memory must be allocated by caller.

   C:
   @code{.c}
   char path[GPATH_MAX];
   G_file_name_misc(path, "cell_misc", "history", "my_raster", "my_mapset");
   // path now contains "/full/path/to/my_mapset/cell_misc/my_raster/history"
   @endcode
   Python:
   @code{.py}
   import ctypes
   from grass.pygrass.utils import decode
   from grass.lib.gis import G_file_name_misc, GPATH_MAX

   path = ctypes.create_string_buffer(GPATH_MAX)
   path_str = decode(G_file_name_misc(path, "dir", "elem", "name", "mapset"))
   print(path_str)
   >>> /full/path/to/mapset/dir/name/elem
   @endcode

   \param[out] path allocated buffer to hold resultant full path to file
   \param dir misc directory (e.g., "cell_misc", "group")
   \param element database element (in this case – file to build path to e.g.,
   "history", "REF") \param name name of object (raster, group; fully qualified
   names allowed e.g., "my_raster@PERMANENT") \param mapset mapset name

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
   \param[out] path allocated buffer to hold resultant full path to file
   \param dir misc directory (e.g., "cell_misc", "group")
   \param element database element (in this case – file to build path to e.g.,
   "history", "REF") \param name name of object (raster, group; fully qualified
   names allowed e.g., "my_raster@PERMANENT") \param mapset mapset name

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
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
   \param[out] path allocated buffer to hold resultant full path to file
   \param dir misc directory (e.g., "cell_misc", "group")
   \param element database element (in this case – file to build path to e.g.,
   "history", "REF") \param name name of object (raster, group; fully qualified
   names allowed e.g., "my_raster@PERMANENT") \param mapset mapset name

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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
   \param[out] path allocated buffer to hold resultant full path to file
   \param dir misc directory (e.g., "cell_misc", "group")
   \param element database element (in this case – file to build path to e.g.,
   "history", "REF") \param name name of object (raster, group; fully qualified
   names allowed e.g., "my_raster@PERMANENT") \param mapset mapset name

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
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
   \param[out] path allocated buffer to hold resultant full path to file
   \param dir misc directory (e.g., "cell_misc", "group")
   \param element database element (in this case – file to build path to e.g.,
   "history", "REF") \param name name of object (raster, group; fully qualified
   names allowed e.g., "my_raster@PERMANENT") \param mapset mapset name

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
   \return pointer to <i>path</i> buffer
 */
char *G_file_name_misc(char *path, const char *dir, const char *element,
                       const char *name, const char *mapset)
{
    return file_name(path, dir, element, name, mapset, NULL);
}

/*!
   \brief Builds full path names to GIS data files in temporary directory (for
   internal use only)

   By default temporary directory is located
   $LOCATION/$MAPSET/.tmp/$HOSTNAME. If GRASS_VECTOR_TMPDIR_MAPSET is
   set to "0", the temporary directory is located in TMPDIR
   (environmental variable defined by the user or GRASS initialization
   script if not given). Note that GRASS_VECTOR_TMPDIR_MAPSET variable
   is currently used only by vector library.

   \param[out] path buffer to hold resultant full path to file
   \param element database element (eg, "cell", "cellhd", "vector", etc)
   \param name name of file to build path to (fully qualified names allowed)
   \param mapset mapset name

   \return pointer to <i>path</i> buffer
 */
char *G_file_name_tmp(char *path, const char *element, const char *name,
                      const char *mapset)
{
    const char *env, *tmp_path;

    tmp_path = NULL;
    env = getenv("GRASS_VECTOR_TMPDIR_MAPSET");
    if (env && strcmp(env, "0") == 0) {
        tmp_path = getenv("TMPDIR");
    }

    return file_name(path, NULL, element, name, mapset, tmp_path);
}

/*!
   \brief Builds full path names to GIS data files in temporary directory (for
   internal use only)

   By default the GRASS temporary directory is located at
   $LOCATION/$MAPSET/.tmp/$HOSTNAME/. If basedir is provided, the
   temporary directory is located at <basedir>/.tmp/$HOSTNAME/.

   \param[out] path buffer to hold resultant full path to file
   \param element database element (eg, "cell", "cellhd", "vector", etc)
   \param name name of file to build path to (fully qualified names allowed)
   \param mapset mapset name

   \return pointer to <i>path</i> buffer
 */
char *G_file_name_basedir(char *path, const char *element, const char *name,
                          const char *mapset, const char *basedir)
{
    return file_name(path, NULL, element, name, mapset, basedir);
}

char *file_name(char *path, const char *dir, const char *element,
                const char *name, const char *mapset, const char *base)
{
    const char *pname = name;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    char xname[GNAME_MAX] = {'\0'};
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
    char xname[GNAME_MAX] = {'\0'};
>>>>>>> cbab883699 (lib/gis: Fix out of scope memory access error in file_name function call (#4650))
=======
    char xname[GNAME_MAX] = {'\0'};
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    if (base && *base) {
        sprintf(path, "%s", base);
    }
    else {
        char xmapset[GMAPSET_MAX] = {'\0'};
        char *location = G__location_path();

        /*
         * if a name is given, build a file name
         * must split the name into name, mapset if it is
         * in the name@mapset format
         */
        if (name && *name && G_name_is_fully_qualified(name, xname, xmapset)) {
            pname = xname;
            sprintf(path, "%s%c%s", location, HOST_DIRSEP, xmapset);
        }
        else if (mapset && *mapset)
            sprintf(path, "%s%c%s", location, HOST_DIRSEP, mapset);
        else
            sprintf(path, "%s%c%s", location, HOST_DIRSEP, G_mapset());
        G_free(location);
    }

    if (dir && *dir) { /* misc element */
        append_char(path, HOST_DIRSEP);
        strcat(path, dir);

        if (pname && *pname) {
            append_char(path, HOST_DIRSEP);
            strcat(path, pname);
        }

        if (element && *element) {
            append_char(path, HOST_DIRSEP);
            strcat(path, element);
        }
    }
    else {
        if (element && *element) {
            append_char(path, HOST_DIRSEP);
            strcat(path, element);
        }

        if (pname && *pname) {
            append_char(path, HOST_DIRSEP);
            strcat(path, pname);
        }
    }

    G_debug(2, "G_file_name(): path = %s", path);

    return path;
}

void append_char(char *s, char c)
{
    int len = strlen(s);

    s[len] = c;
    s[len + 1] = '\0';
}
