/*!
   \file lib/imagery/sigsetfile.c

   \brief Imagery Library - Signature file functions (statistics for i.smap)

   (C) 2001-2011, 2013, 2021 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author USA CERL
 */

#include <string.h>

#include <grass/gis.h>
#include <grass/imagery.h>
#include <grass/glocale.h>

/*!
   \brief Create new sigset file

   \param name name of sigset file

   \return pointer to FILE
   \return NULL on error
 */
FILE *I_fopen_sigset_file_new(const char *name)
{
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
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
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
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
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
    char dir[GNAME_MAX];
    FILE *fd;

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;
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
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;
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
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

<<<<<<< HEAD
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new(element, name);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

<<<<<<< HEAD
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new(element, name);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

<<<<<<< HEAD
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new(element, name);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

<<<<<<< HEAD
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new(element, name);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

<<<<<<< HEAD
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new(element, name);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

<<<<<<< HEAD
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new(element, name);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

<<<<<<< HEAD
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new(element, name);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

<<<<<<< HEAD
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new(element, name);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))

=======
<<<<<<< HEAD
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;

=======
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;

>>>>>>> osgeo-main
=======
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;

>>>>>>> osgeo-main
    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

<<<<<<< HEAD
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new(element, name);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
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
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
    char element[GNAME_MAX];
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;

    /* create sig directory */
    I_make_signatures_dir(I_SIGFILE_TYPE_SIGSET);

    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_new_misc(dir, "sig", name);

>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
=======

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    return fd;
}

/*!
   \brief Open existing sigset signature file

   \param name name of signature file (may be fully qualified)

   \return pointer to FILE*
   \return NULL on error
 */
FILE *I_fopen_sigset_file_old(const char *name)
{
    char sig_name[GNAME_MAX], sig_mapset[GMAPSET_MAX];
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
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
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
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
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
    char dir[GNAME_MAX];
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    char dir[GNAME_MAX];
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
=======
    char dir[GNAME_MAX];
=======
>>>>>>> osgeo-main
    char element[GNAME_MAX];
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    char dir[GNAME_MAX];
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    char dir[GNAME_MAX];
=======
    char element[GNAME_MAX];
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
    char dir[GNAME_MAX];
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
    char dir[GNAME_MAX];
=======
    char element[GNAME_MAX];
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    char dir[GNAME_MAX];
=======
    char element[GNAME_MAX];
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
=======
    char dir[GNAME_MAX];
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
    char dir[GNAME_MAX];
=======
    char element[GNAME_MAX];
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
=======
    char dir[GNAME_MAX];
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
    char element[GNAME_MAX];
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    char dir[GNAME_MAX];
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
    char dir[GNAME_MAX];
=======
    char element[GNAME_MAX];
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
=======
    char dir[GNAME_MAX];
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
    FILE *fd;

    if (G_unqualified_name(name, NULL, sig_name, sig_mapset) == 0)
        strcpy(sig_mapset, G_mapset());

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
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
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
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
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> osgeo-main
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old(element, sig_name, sig_mapset);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
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
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old(element, sig_name, sig_mapset);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old(element, sig_name, sig_mapset);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old(element, sig_name, sig_mapset);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old(element, sig_name, sig_mapset);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
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
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
=======
    I__get_signatures_element(element, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old(element, sig_name, sig_mapset);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
=======
    I_get_signatures_dir(dir, I_SIGFILE_TYPE_SIGSET);
    fd = G_fopen_old_misc(dir, "sig", sig_name, sig_mapset);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))

    return fd;
}
