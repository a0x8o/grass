/*!
 * \file lib/gis/tempfile.c
 *
 * \brief GIS Library - Temporary file functions.
 *
 * (C) 2001-2015 by the GRASS Development Team
 *
 * This program is free software under the GNU General Public License
 * (>=v2). Read the file COPYING that comes with GRASS for details.
 *
 * \author Original author CERL
 */

#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <stdlib.h>

#include <grass/gis.h>

#include "gis_local_proto.h"

static struct Counter unique;
static int initialized;

/*!
   \brief Initialize environment for creating tempfiles.
 */
void G_init_tempfile(void)
{
    if (G_is_initialized(&initialized))
        return;

    G_init_counter(&unique, 0);

    G_initialize_done(&initialized);
}

/*!
 * \brief Returns a temporary file name.
 *
 * This routine returns a pointer to a string containing a unique
 * temporary file name that can be used as a temporary file within the
 * module. Successive calls to G_tempfile() will generate new
 * names. Only the file name is generated. The file itself is not
 * created. To create the file, the module must use standard UNIX
 * functions which create and open files, e.g., <i>creat()</i> or
 * <i>fopen()</i>.
 *
 * Successive calls will generate different names the names are of the
 * form pid.n where pid is the programs process id number and n is a
 * unique identifier.
 *
 * <b>Note:</b> It is recommended to <i>unlink()</i> (remove) the
 * temp file on exit/error. Only if GRASS is left with 'exit', the GIS
 * mapset management will clean up the temp directory (ETC/clean_temp).
 *
 * \return pointer to a character string containing the name. The name
 * is copied to allocated memory and may be released by the unix free()
 * routine.
 */
char *G_tempfile(void)
{
    return G_tempfile_pid(getpid());
}

/*!
 * \brief Returns a temporary file name.
 *
 * Similar to G_tempfile(), but the temporary file name will include
 * a provided base directory instead of the path to the current mapset.
 *
 * \return pointer to a character string containing the name. The name
 * is copied to allocated memory and may be released by the unix free()
 * routine.
 */
char *G_tempfile_basedir(const char *basedir)
{
    return G_tempfile_pid_basedir(getpid(), basedir);
}

/*!
 * \brief Create tempfile from process id.
 *
 * See G_tempfile().
 *
 * \param pid
 * \return pointer to string path
 */
char *G_tempfile_pid(int pid)
{
    char path[GPATH_MAX];
    char name[GNAME_MAX];
    char element[100];

    if (pid <= 0)
        pid = getpid();
    G_temp_element(element);
    G_init_tempfile();
    do {
        int uniq = G_counter_next(&unique);

        sprintf(name, "%d.%d", pid, uniq);
        G_file_name(path, element, name, G_mapset());
    } while (access(path, F_OK) == 0);

    G_debug(2, "G_tempfile_pid(): %s", path);

    return G_store(path);
}

/*!
 * \brief Create tempfile from process id in given base directory.
 *
 * See G_tempfile_basedir().
 *
 * \param pid
 * \return pointer to string path
 */
char *G_tempfile_pid_basedir(int pid, const char *basedir)
{
    char path[GPATH_MAX];
    char name[GNAME_MAX];
    char element[100];

    if (pid <= 0)
        pid = getpid();
    G__temp_element_basedir(element, basedir);
    G_init_tempfile();
    do {
        int uniq = G_counter_next(&unique);

        sprintf(name, "%d.%d", pid, uniq);
        G_file_name_basedir(path, element, name, G_mapset(), basedir);
    } while (access(path, F_OK) == 0);

    G_debug(2, "G_tempfile_pid(): %s", path);

    return G_store(path);
}

/*!
 * \brief Populates element with a path string.
 *
 * \param[out] element element name
 */
void G_temp_element(char *element)
{
    G__temp_element(element, FALSE);
}

/*!
 * \brief Populates element with a path string (internal use only!)
 *
 * \param[out] element element name
 * \param tmp TRUE to use G_make_mapset_element_tmp() instead of
 * G_make_mapset_element()
 */
void G__temp_element(char *element, int tmp)
{
    const char *machine;

    strcpy(element, ".tmp");
    machine = G__machine_name();
    if (machine != NULL && *machine != 0) {
        strcat(element, "/");
        strcat(element, machine);
    }

    if (!tmp)
        G_make_mapset_object_group(element);
    else
        G_make_mapset_object_group_tmp(element);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
=======
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD

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
    
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
    
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8e24da816f (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======

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
    
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> e17ab3c1a1 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD

=======
    
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
>>>>>>> f6958f78a7 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
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
    G_debug(2, "G__temp_element(): %s (tmp=%d)", element, tmp);
}

/*!
 * \brief Populates element with a path string (internal use only!)
 *
 * \param[out] element element name
 * \param tmp TRUE to use G_make_mapset_element_tmp() instead of
 * G_make_mapset_element()
 */
void G__temp_element_basedir(char *element, const char *basedir)
{
    const char *machine;

    strcpy(element, ".tmp");
    machine = G__machine_name();
    if (machine != NULL && *machine != 0) {
        strcat(element, "/");
        strcat(element, machine);
    }

    if (basedir && *basedir)
        G_make_mapset_object_group_basedir(element, basedir);
    else
        G_make_mapset_object_group(element);

    G_debug(2, "G__temp_element_basedir(): %s", element);
}
