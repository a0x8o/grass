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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_dir_object()
   \sa G_make_mapset_object_group_tmp()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
   \sa G_make_mapset_object_group()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
   \sa G_make_mapset_object_group()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
<<<<<<< HEAD
>>>>>>> main
=======
int make_mapset_element_impl(const char *p_path, const char *p_element, bool race_ok)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
            if (*element == 0)
                return 1;
        }
        *p++ = *element++;
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
=======
>>>>>>> main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
int make_mapset_element_no_fail_on_race(const char *p_path,
                                        const char *p_element)
=======
int make_mapset_element_no_fail_on_race(const char *p_path, const char *p_element)
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======

>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
=======
>>>>>>> main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======
    return G_make_mapset_dir_object(dir, name);
>>>>>>> 27faeed049 (r.in.pdal: use fabs for double values (#1752))
>>>>>>> f9d61299d7 (r.in.pdal: use fabs for double values (#1752))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    return G_make_mapset_dir_object(dir, name);
=======
    G_make_mapset_dir_object(dir, name);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
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
