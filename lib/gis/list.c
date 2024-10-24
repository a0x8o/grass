/*!
   \file lib/gis/list.c

   \brief List elements

   \author Unknown (probably CERL)

   (C) 2000, 2010 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.
 */

#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <sys/types.h>
#include <dirent.h>

#include <grass/gis.h>
#include <grass/glocale.h>

static int list_element(FILE *, const char *, const char *, const char *,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                        int (*)(const char *, const char *, char *));
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        int (*)(const char *, const char *, char *));
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
=======
                        int (*)(const char *, const char *, char *));
=======
>>>>>>> osgeo-main
                        int (*)(const char *, const char *, const char *));
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                        int (*)(const char *, const char *, const char *));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                        int (*)(const char *, const char *, char *));
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
                        int (*)(const char *, const char *, const char *));
=======
                        int (*)(const char *, const char *, char *));
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
                        int (*)(const char *, const char *, char *));
=======
                        int (*)(const char *, const char *, const char *));
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                        int (*)(const char *, const char *, const char *));
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
                        int (*)(const char *, const char *, char *));
=======
                        int (*)(const char *, const char *, const char *));
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                        int (*)(const char *, const char *, const char *));
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
                        int (*)(const char *, const char *, char *));
=======
                        int (*)(const char *, const char *, const char *));
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                        int (*)(const char *, const char *, const char *));
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

/*!
   \brief General purpose list function

   Will list files from all mapsets in the mapset list for a specified
   database element.

   Note: output is to stdout piped thru the more utility

   \code
   lister (char *name char *mapset, char* buf)
   \endcode

   Given file <em>name</em>, and <em>mapset</em>, lister() should
   copy a string into 'buf' when called with name == "", should set
   buf to general title for mapset list.

   \param element    database element (eg, "cell", "cellhd", etc.)
   \param desc       description for element (if NULL, element is used)
   \param mapset     mapset to be listed "" to list all mapsets in mapset search
   list
   "." will list current mapset
   \param lister     if given will call this routine to get a list title.
   NULL if no titles desired.
 */
void G_list_element(const char *element, const char *desc, const char *mapset,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                    int (*lister)(const char *, const char *, char *))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    int (*lister)(const char *, const char *, char *))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                    int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
                    int (*lister)(const char *, const char *, const char *))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                    int (*lister)(const char *, const char *, const char *))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    int (*lister)(const char *, const char *, char *))
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
                    int (*lister)(const char *, const char *, const char *))
=======
                    int (*lister)(const char *, const char *, char *))
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
                    int (*lister)(const char *, const char *, char *))
=======
                    int (*lister)(const char *, const char *, const char *))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    int (*lister)(const char *, const char *, const char *))
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
                    int (*lister)(const char *, const char *, char *))
=======
                    int (*lister)(const char *, const char *, const char *))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    int (*lister)(const char *, const char *, const char *))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
                    int (*lister)(const char *, const char *, char *))
=======
                    int (*lister)(const char *, const char *, const char *))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    int (*lister)(const char *, const char *, const char *))
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
{
    struct Popen pager;
    int n;
    FILE *more;
    int count;

    count = 0;
    if (desc == 0 || *desc == 0)
        desc = element;

    /*
     * G_popen() the more command to page the output
     */
    more = G_open_pager(&pager);
    fprintf(more, "----------------------------------------------\n");

    /*
     * if no specific mapset is requested, list the mapsets
     * from the mapset search list
     * otherwise just list the specified mapset
     */
    if (mapset == 0 || *mapset == 0)
        for (n = 0; (mapset = G_get_mapset_name(n)); n++)
            count += list_element(more, element, desc, mapset, lister);
    else
        count += list_element(more, element, desc, mapset, lister);

    if (count == 0) {
        if (mapset == 0 || *mapset == 0)
            fprintf(more, _("no %s files available in current mapset\n"), desc);
        else
            fprintf(more, _("no %s files available in mapset <%s>\n"), desc,
                    mapset);

        fprintf(more, "----------------------------------------------\n");
    }
    /*
     * close the more
     */
    G_close_pager(&pager);
}

static int list_element(FILE *out, const char *element, const char *desc,
                        const char *mapset,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                        int (*lister)(const char *, const char *, char *))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        int (*lister)(const char *, const char *, char *))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
=======
                        int (*lister)(const char *, const char *, char *))
=======
>>>>>>> osgeo-main
                        int (*lister)(const char *, const char *, const char *))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                        int (*lister)(const char *, const char *, const char *))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                        int (*lister)(const char *, const char *, char *))
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
                        int (*lister)(const char *, const char *, const char *))
=======
                        int (*lister)(const char *, const char *, char *))
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
                        int (*lister)(const char *, const char *, char *))
=======
                        int (*lister)(const char *, const char *, const char *))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                        int (*lister)(const char *, const char *, const char *))
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
                        int (*lister)(const char *, const char *, char *))
=======
                        int (*lister)(const char *, const char *, const char *))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                        int (*lister)(const char *, const char *, const char *))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
                        int (*lister)(const char *, const char *, char *))
=======
                        int (*lister)(const char *, const char *, const char *))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                        int (*lister)(const char *, const char *, const char *))
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
{
    char path[GPATH_MAX];
    int count = 0;
    char **list;
    int i;

    /*
     * convert . to current mapset
     */
    if (strcmp(mapset, ".") == 0)
        mapset = G_mapset();

    /*
     * get the full name of the GIS directory within the mapset
     * and list its contents (if it exists)
     *
     * if lister() routine is given, the ls command must give 1 name
     */
    G_file_name(path, element, "", mapset);
    if (access(path, 0) != 0) {
        fprintf(out, "\n");
        return count;
    }

    /*
     * if a title so that we can call lister() with the names
     * otherwise the ls must be forced into columnar form.
     */

    list = G_ls2(path, &count);

    if (count > 0) {
        fprintf(out, _("%s files available in mapset <%s>:\n"), desc, mapset);
        if (lister) {
            char title[400];
            char name[GNAME_MAX];

            *name = *title = 0;
            lister(name, mapset, title);
            if (*title)
                fprintf(out, "\n%-18s %-.60s\n", name, title);
        }
    }

    if (lister) {
        for (i = 0; i < count; i++) {
            char title[400];

            lister(list[i], mapset, title);
            fprintf(out, "%-18s %-.60s\n", list[i], title);
        }
    }
    else
        G_ls_format(list, count, 0, out);

    fprintf(out, "\n");

    for (i = 0; i < count; i++)
        G_free((char *)list[i]);
    if (list)
        G_free(list);

    return count;
}

/*!
   \brief List specified type of elements. Application must release
   the allocated memory.

   \param element element type (G_ELEMENT_RASTER, G_ELEMENT_VECTOR,
   G_ELEMENT_REGION ) \param gisbase path to GISBASE \param location location
   name \param mapset mapset name

   \return zero terminated array of element names
 */
char **G_list(int element, const char *gisbase, const char *location,
              const char *mapset)
{
    char *el;
    char *buf;
    DIR *dirp;
    struct dirent *dp;
    int count;
    char **list;

    switch (element) {
    case G_ELEMENT_RASTER:
        el = "cell";
        break;

    case G_ELEMENT_GROUP:
        el = "group";
        break;

    case G_ELEMENT_VECTOR:
        el = "vector";
        break;

    case G_ELEMENT_REGION:
        el = "windows";
        break;

    default:
        G_fatal_error(_("G_list: Unknown element type"));
    }

    buf = (char *)G_malloc(strlen(gisbase) + strlen(location) + strlen(mapset) +
                           strlen(el) + 4);

    sprintf(buf, "%s/%s/%s/%s", gisbase, location, mapset, el);

    dirp = opendir(buf);
    G_free(buf);

    if (dirp == NULL) { /* this can happen if element does not exist */
        list = (char **)G_calloc(1, sizeof(char *));
        return list;
    }

    count = 0;
    while ((dp = readdir(dirp)) != NULL) {
        if (dp->d_name[0] == '.')
            continue;
        count++;
    }
    rewinddir(dirp);

    list = (char **)G_calloc(count + 1, sizeof(char *));

    count = 0;
    while ((dp = readdir(dirp)) != NULL) {
        if (dp->d_name[0] == '.')
            continue;

        list[count] = (char *)G_malloc(strlen(dp->d_name) + 1);
        strcpy(list[count], dp->d_name);
        count++;
    }
    closedir(dirp);

    return list;
}

/*!
   \brief Free list

   \param list char* array to be freed

   \return
 */
void G_free_list(char **list)
{
    int i = 0;

    if (!list)
        return;

    while (list[i]) {
        G_free(list[i]);
        i++;
    }
    G_free(list);
}
