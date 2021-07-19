/*!
   \file lib/gis/mapset_msc.c

   \brief GIS library - Mapset user permission routines.

   (C) 1999-2014 The GRASS development team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.
 */

#include <grass/config.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <grass/gis.h>
#include <grass/glocale.h>

static int make_mapset_element(const char *, const char *);
static int make_mapset_element_no_fail_on_race(const char *, const char *);
static int make_mapset_element_impl(const char *, const char *, bool);

/*!
   \brief Create element in the current mapset.

   Make the specified element in the current mapset will check for the
   existence of the element and do nothing if it is found so this
   routine can be called even if the element already exists.

   Calls G_fatal_error() on failure.

   \deprecated
   This function is deprecated due to confusion in element terminology.
   Use G_make_mapset_object_group() or G_make_mapset_dir_object() instead.

   \param p_element element to be created in mapset

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_element(const char *p_element)
{
    char path[GPATH_MAX];

    G_file_name(path, NULL, NULL, G_mapset());
    return make_mapset_element(path, p_element);
}

/*!
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
   \brief Create directory for group of elements of a given type.

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for group of elements of a given type.
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for group of elements of a given type.
=======
<<<<<<< HEAD
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
=======
    \brief Create directory for group of elements of a given type.
<<<<<<< HEAD
<<<<<<< HEAD
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
=======
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
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
<<<<<<< HEAD
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for group of elements of a given type.
=======
   \brief Create directory for group of elements of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   If creation fails, but the directory exists after the failure,
   the function reports success. Therefore, two processes creating
   a directory in this way can work in parallel.

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `cell`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for group of elements of a given type.

    Creates the specified element directory in the current mapset.
    It will check for the existence of the element and do nothing
    if it is found so this routine can be called even if the element
    already exists to ensure that it exists.

    If creation fails, but the directory exists after the failure,
    the function reports success. Therefore, two processes creating
    a directory in this way can work in parallel.

    Calls G_fatal_error() on failure.

    \param type object type (e.g., `cell`)

    \return 0 no element defined
    \return 1 on success

    \sa G_make_mapset_dir_object()
    \sa G_make_mapset_object_group_tmp()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
 */
int G_make_mapset_object_group(const char *type)
{
    char path[GPATH_MAX];

    G_file_name(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
   \brief Create directory for an object of a given type.

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

   \sa G_make_mapset_object_group()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
   \sa G_make_mapset_object_group()
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
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for an object of a given type.
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_object_group()
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
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for an object of a given type.
=======
<<<<<<< HEAD
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
=======
    \brief Create directory for an object of a given type.
<<<<<<< HEAD
<<<<<<< HEAD
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_object_group()
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
=======
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_object_group()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_object_group()
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
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
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
<<<<<<< HEAD
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
   \sa G_make_mapset_object_group()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_object_group()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
   \sa G_make_mapset_object_group()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for an object of a given type.
=======
   \brief Create directory for an object of a given type.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   Creates the specified element directory in the current mapset.
   It will check for the existence of the element and do nothing
   if it is found so this routine can be called even if the element
   already exists to ensure that it exists.

   Any failure to create it, including the case when it exists
   (i.e., was created by another process after the existence test)
   is considered a failure because two processes should not attempt
   to create two objects of the same name (and type).

   This function is for objects which are directories
   (the function does not create files).

   Calls G_fatal_error() on failure.

   \param type object type (e.g., `vector`)
   \param name object name (e.g., `bridges`)

   \return 0 no element defined
   \return 1 on success

<<<<<<< HEAD
    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
   \sa G_make_mapset_object_group()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    \brief Create directory for an object of a given type.

    Creates the specified element directory in the current mapset.
    It will check for the existence of the element and do nothing
    if it is found so this routine can be called even if the element
    already exists to ensure that it exists.

    Any failure to create it, including the case when it exists
    (i.e., was created by another process after the existence test)
    is considered a failure because two processes should not attempt
    to create two objects of the same name (and type).

    This function is for objects which are directories
    (the function does not create files).

    Calls G_fatal_error() on failure.

    \param type object type (e.g., `vector`)
    \param name object name (e.g., `bridges`)

    \return 0 no element defined
    \return 1 on success

    \sa G_make_mapset_object_group()
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
 */
int G_make_mapset_dir_object(const char *type, const char *name)
{
    char path[GPATH_MAX];

    G_make_mapset_object_group(type);
    G_file_name(path, type, NULL, G_mapset());
    return make_mapset_element(path, name);
}

/*!
   \brief Create element in the temporary directory.

   See G_file_name_tmp() for details.

   \param p_element element to be created in mapset (e.g., `elevation`)

   \note
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_element_tmp(const char *p_element)
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element(path, p_element);
}

/*!
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_tmp() for details.

   \param type object type (e.g., `cell`)

   \note
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.

   \param type object type (e.g., `cell`)

   \note
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
    \brief Create directory for type of objects in the temporary directory.

    See G_file_name_tmp() for details.

    \param type object type (e.g., `cell`)

    \note
    Use G_make_mapset_object_group_tmp() for creating common, shared
    directories which are for multiple concrete elements (objects).

    \return 0 no element defined
    \return 1 on success
 */
int G_make_mapset_object_group_tmp(const char *type)
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.

   \param type object type (e.g., `cell`)

   \note
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.

   \param type object type (e.g., `cell`)

   \note
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.

   \param type object type (e.g., `cell`)

   \note
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.

   \param type object type (e.g., `cell`)

   \note
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
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
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
    \brief Create directory for type of objects in the temporary directory.
=======
   \brief Create directory for type of objects in the temporary directory.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

   See G_file_name_tmp() for details.
=======
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> main
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \param type object type (e.g., `cell`)

   \note
<<<<<<< HEAD
   Use G_make_mapset_object_group_tmp() for creating common, shared
   directories which are for multiple concrete elements (objects).
=======
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

   \return 0 no element defined
   \return 1 on success
 */
<<<<<<< HEAD
int G_make_mapset_object_group_tmp(const char *type)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.

   \param type object type (e.g., `cell`)

   \note
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
{
    char path[GPATH_MAX];

    G_file_name_tmp(path, NULL, NULL, G_mapset());
    return make_mapset_element_no_fail_on_race(path, type);
}

/*!
   \brief Create directory for type of objects in the temporary directory.

   See G_file_name_basedir() for details.

   \param type object type (e.g., `cell`)

   \note
   Use G_make_mapset_object_group_basedir() for creating common, shared
   directories for temporary data.

   \return 0 no element defined
   \return 1 on success
 */
int G_make_mapset_object_group_basedir(const char *type, const char *basedir)
{
    char path[GPATH_MAX];

    G_file_name_basedir(path, NULL, NULL, G_mapset(), basedir);
    return make_mapset_element_no_fail_on_race(path, type);
}

int make_mapset_element_impl(const char *p_path, const char *p_element,
                             bool race_ok)
{
    char path[GPATH_MAX] = {'\0'};
    char *p;
    const char *element;

    element = p_element;
    if (*element == 0)
        return 0;

    strncpy(path, p_path, GPATH_MAX - 1);
    p = path;
    while (*p)
        p++;
    /* add trailing slash if missing */
    --p;
    if (*p++ != '/') {
        *p++ = '/';
        *p = 0;
    }

    /* now append element, one directory at a time, to path */
    while (1) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
        if (*element == '/' || *element == 0) {
            *p = 0;
            char *msg = NULL;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
	if (*element == '/' || *element == 0) {
	    *p = 0;
            char *msg = NULL;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
        if (*element == '/' || *element == 0) {
            *p = 0;
            char *msg = NULL;

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
        if (*element == '/' || *element == 0) {
            *p = 0;
            char *msg = NULL;

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
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        if (*element == '/' || *element == 0) {
            *p = 0;
            char *msg = NULL;

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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
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
        if (*element == '/' || *element == 0) {
            *p = 0;
            char *msg = NULL;

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
        if (*element == '/' || *element == 0) {
            *p = 0;
            char *msg = NULL;

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
	if (*element == '/' || *element == 0) {
	    *p = 0;
            char *msg = NULL;
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (*element == '/' || *element == 0) {
            *p = 0;
            char *msg = NULL;

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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
	if (*element == '/' || *element == 0) {
	    *p = 0;
            char *msg = NULL;
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
        if (*element == '/' || *element == 0) {
            *p = 0;
            char *msg = NULL;

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
            if (access(path, 0) != 0) {
                /* Assuming that directory does not exist. */
                if (G_mkdir(path) != 0) {
                    msg = G_store(strerror(errno));
                }
            }
            if (access(path, 0) != 0 || (msg && !race_ok)) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
                /* Directory is not accessible even after attempt to create it.
                 */
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
            if (*element == 0)
                return 1;
        }
        *p++ = *element++;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
<<<<<<< HEAD
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
=======
                /* Directory is not accessible even after attempt to create it.
                 */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(
                        _("Unable to make mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(
                        _("Unable to access mapset element %s (%s): %s"),
                        p_element, path, strerror(errno));
                }
            }
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                /* Directory is not accessible even after attempt to create it. */
                if (msg) {
                    /* Error already happened when mkdir. */
                    G_fatal_error(_("Unable to make mapset element %s (%s): %s"),
                                  p_element, path, strerror(errno));
                }
                else {
                    /* Access error is not related to mkdir. */
                    G_fatal_error(_("Unable to access mapset element %s (%s): %s"),
                                  p_element, path, strerror(errno));
                }
            }
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
	    if (*element == 0)
		return 1;
	}
	*p++ = *element++;
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
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
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
            if (*element == 0)
                return 1;
        }
        *p++ = *element++;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
    }
}

int make_mapset_element(const char *p_path, const char *p_element)
{
    return make_mapset_element_impl(p_path, p_element, false);
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> osgeo-main
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
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
=======
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
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
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
{
    return make_mapset_element_impl(p_path, p_element, true);
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
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
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
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
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
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
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
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
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> osgeo-main
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> osgeo-main
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
/*!
   \brief Create misc element in the current mapset.

   \param dir directory path (e.g., `cell_misc`)
   \param name element to be created in mapset (e.g., `elevation`)

   \return 0 no element defined
   \return 1 on success
 */
int G__make_mapset_element_misc(const char *dir, const char *name)
{
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> aaa2e34005 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 1ffad0fc5b (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 9cd1b6d9c9 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 0cbfb74ba9 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> b2ab840ea4 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> e5fc818f7d (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 4590042bfb (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 78a52d42bb (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 30416b6363 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> acd1b6e775 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d96f5cdda9 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2e4d8e4117 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 9bd9a00f13 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 61fdece06c (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 9602ecba41 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d95d1dcca3 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 70379b8c0d (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6a4b50f6be (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 85474cf068 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a8f346dc65 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 653527d137 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 17573ca63a (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d15443b874 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a69b865d0d (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a5c9c945b5 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> f63c120be9 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 7c48d4bab5 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a187971a2b (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 460bcc93b2 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2d43486e7b (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 961d2e8d91 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776bc11225 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 3a69cb5ad8 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1ffad0fc5b (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 6bb042a534 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9cd1b6d9c9 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 0cdf004d95 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 30c0a64bd6 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 4e28c55b49 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 174a0a2c6b (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 53e0308ffd (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
    return G_make_mapset_dir_object(dir, name);
>>>>>>> a5c9c945b5 (r.in.pdal: use fabs for double values (#1752))
=======
<<<<<<< HEAD
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
>>>>>>> 2d43486e7b (r.in.pdal: use fabs for double values (#1752))
=======
<<<<<<< HEAD
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
>>>>>>> 7c48d4bab5 (r.in.pdal: use fabs for double values (#1752))
=======
<<<<<<< HEAD
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0cdf004d95 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 0cbfb74ba9 (r.in.pdal: use fabs for double values (#1752))
=======
=======
=======
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 30c0a64bd6 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> b2ab840ea4 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 4e28c55b49 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> e5fc818f7d (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a777ae5960 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 3a69cb5ad8 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> d15443b874 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
    return G_make_mapset_dir_object(dir, name);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    return G_make_mapset_dir_object(dir, name);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> f63c120be9 (r.in.pdal: use fabs for double values (#1752))
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
>>>>>>> osgeo-main
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d15443b874 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
=======
    return G_make_mapset_dir_object(dir, name);
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
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> e4543c8b72 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 53e0308ffd (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
=======
>>>>>>> 938317f5e5 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 961d2e8d91 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 666607eccb (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6bb042a534 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> a69b865d0d (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 460bcc93b2 (r.in.pdal: use fabs for double values (#1752))
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 666607eccb (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> a69b865d0d (r.in.pdal: use fabs for double values (#1752))
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 174a0a2c6b (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 53e0308ffd (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 30416b6363 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 30416b6363 (r.in.pdal: use fabs for double values (#1752))
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> e4543c8b72 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 53e0308ffd (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> abb139f9fc (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> acd1b6e775 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 43a14bf1d8 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> d96f5cdda9 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 0f7db87b86 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 2e4d8e4117 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 3270e6468a (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 9bd9a00f13 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 616b6d254e (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 61fdece06c (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> d282634b4c (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 9602ecba41 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> b20e7d7e8b (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> d95d1dcca3 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> e49d57326e (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 70379b8c0d (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> e1389b69ec (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 6a4b50f6be (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> 8fadce25e0 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 85474cf068 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> a21c434467 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> a8f346dc65 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> acd1b6e775 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d96f5cdda9 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 2e4d8e4117 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 9bd9a00f13 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 61fdece06c (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 9602ecba41 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> d95d1dcca3 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 70379b8c0d (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6a4b50f6be (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 85474cf068 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a8f346dc65 (r.in.pdal: use fabs for double values (#1752))
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 938317f5e5 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> b0ee055743 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> aaa2e34005 (r.in.pdal: use fabs for double values (#1752))
=======
=======
    return G_make_mapset_dir_object(dir, name);
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
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4b5e4db7d3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 961d2e8d91 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 776bc11225 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0545137c75 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 3a69cb5ad8 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1ffad0fc5b (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bbe0f8458b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
>>>>>>> a69b865d0d (r.in.pdal: use fabs for double values (#1752))
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 6bb042a534 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9cd1b6d9c9 (r.in.pdal: use fabs for double values (#1752))
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
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> e4543c8b72 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
=======
>>>>>>> 53e0308ffd (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 938317f5e5 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a187971a2b (r.in.pdal: use fabs for double values (#1752))
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a187971a2b (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> 460bcc93b2 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 485ab4c120 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 0cdf004d95 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 0cbfb74ba9 (r.in.pdal: use fabs for double values (#1752))
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
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b5bd69d54d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b2ab840ea4 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 09e2da0f21 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
<<<<<<< HEAD
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 4e28c55b49 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> e5fc818f7d (r.in.pdal: use fabs for double values (#1752))
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
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 4070153b86 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> e4543c8b72 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 30c0a64bd6 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 4590042bfb (r.in.pdal: use fabs for double values (#1752))
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
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 686d2e0404 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 53e0308ffd (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 174a0a2c6b (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 78a52d42bb (r.in.pdal: use fabs for double values (#1752))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> e85854f15b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 53e0308ffd (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 30416b6363 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 92f4985d14 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> abb139f9fc (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> acd1b6e775 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fae0ef2321 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 95a484914d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 43a14bf1d8 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> d96f5cdda9 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e621aac8f3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> fe292bf504 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
<<<<<<< HEAD
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 0f7db87b86 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 2e4d8e4117 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b95b0d8ab2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5a342a7bc7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 3270e6468a (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 9bd9a00f13 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 05ebc5df37 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ff23ff042d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 616b6d254e (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 61fdece06c (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3bb9edaff3 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> b34f2b11df (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> d282634b4c (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 9602ecba41 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9ae19d54c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> f8c17e2c16 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> b20e7d7e8b (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> d95d1dcca3 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 00836f7c93 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 5c566ffedc (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> e49d57326e (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 70379b8c0d (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d167c94555 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> a67b145d8f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> e1389b69ec (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 6a4b50f6be (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 40f7652106 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 97f957a0b7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> eab8a2b63d (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 938317f5e5 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 653527d137 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 17573ca63a (r.in.pdal: use fabs for double values (#1752))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 198d7a13b2 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ed582d44e5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 8fadce25e0 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 85474cf068 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab6c96ff3e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8f2d4463c9 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> a21c434467 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> a8f346dc65 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> a777ae5960 (r.in.pdal: use fabs for double values (#1752))
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2e3eee6b66 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> aeb2dc26c5 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 961d2e8d91 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 666607eccb (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b67019a4e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 8ace21395b (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 3a69cb5ad8 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> d15443b874 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 856b44c452 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 5016a6692a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> a69b865d0d (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> a5c9c945b5 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 671e6a355e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 018aecd8a6 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 0cdf004d95 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> a5c9c945b5 (r.in.pdal: use fabs for double values (#1752))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 0a74870c80 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> f63c120be9 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63c02ea43e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 0f48660671 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
<<<<<<< HEAD
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 4e28c55b49 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 7c48d4bab5 (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 7f57c23d18 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> ebeb54c4e0 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> e4543c8b72 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 30c0a64bd6 (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> a187971a2b (r.in.pdal: use fabs for double values (#1752))
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
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> d703f39c74 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 72e8ce6804 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 53e0308ffd (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 174a0a2c6b (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 460bcc93b2 (r.in.pdal: use fabs for double values (#1752))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
>>>>>>> 6837a8cea1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> 53e0308ffd (r.in.pdal: use fabs for double values (#1752))
<<<<<<< HEAD
>>>>>>> 2d43486e7b (r.in.pdal: use fabs for double values (#1752))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e4a11f0d3a (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> 9982dfa0b8 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
}

static int check_owner(const struct stat *info)
{
#if defined(__MINGW32__) || defined(SKIP_MAPSET_OWN_CHK)
    return 1;
#else
    const char *check = getenv("GRASS_SKIP_MAPSET_OWNER_CHECK");

    if (check && *check)
        return 1;
    if (info->st_uid != getuid())
        return 0;
    if (info->st_uid != geteuid())
        return 0;
    return 1;
#endif
}

/*!
   \brief Check for user mapset permission

   \param mapset mapset name

   \return 1 mapset exists, and user has permission
   \return 0 mapset exists, BUT user denied permission
   \return -1 mapset does not exist
 */
int G_mapset_permissions(const char *mapset)
{
    char path[GPATH_MAX];
    struct stat info;

    G_file_name(path, "", "", mapset);

    if (G_stat(path, &info) != 0)
        return -1;
    if (!S_ISDIR(info.st_mode))
        return -1;

    if (!check_owner(&info))
        return 0;

    return 1;
}

/*!
   \brief Check for user mapset permission

   \param gisdbase full path to GISDBASE
   \param location location name
   \param mapset mapset name

   \return 1 mapset exists, and user has permission
   \return 0 mapset exists, BUT user denied permission
   \return -1 mapset does not exist
 */
int G_mapset_permissions2(const char *gisdbase, const char *location,
                          const char *mapset)
{
    char path[GPATH_MAX];
    struct stat info;

    sprintf(path, "%s/%s/%s", gisdbase, location, mapset);

    if (G_stat(path, &info) != 0)
        return -1;
    if (!S_ISDIR(info.st_mode))
        return -1;

    if (!check_owner(&info))
        return 0;

    return 1;
}
