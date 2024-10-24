/**
 * \file daemon.c
 *
 * \brief Implementation of the server for parallel
 * computing of r.li raster analysis
 *
 * \author Claudio Porta & Lucio Davide Spano
 *
 * This program is free software under the GPL (>=v2)
 * Read the COPYING file that comes with GRASS for details.
 *
 * \version 1.0
 *
 * \include
 *
 */
#include <stdlib.h>
#include <stddef.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <dirent.h>
#include <errno.h>
#include <math.h>

#ifdef __MINGW32__
#include <process.h>
#else
#include <sys/wait.h>
#endif

#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>
#include "daemon.h"

int calculateIndex(char *file, rli_func *f, char **parameters, char *raster,
                   char *output)
{

    char pathSetup[GPATH_MAX], out[GPATH_MAX], parsed;
    char *random_access_name;
    struct History history;
    struct g_area *g;
    int res;
    int doneDir, mv_fd, random_access;

    /* int mv_rows, mv_cols; */
    struct list *l;
    msg m, doneJob;

    g = (struct g_area *)G_malloc(sizeof(struct g_area));
    g->maskname = NULL;
    l = (struct list *)G_malloc(sizeof(struct list));
    l->head = NULL;
    l->tail = NULL;
    l->size = 0;

    worker_init(raster, f, parameters);

    /*#########################################################
       -----------------create area queue----------------------
       ######################################################### */

    /* strip off leading path if present */
    char rlipath[GPATH_MAX];
    char testpath[GPATH_MAX];

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
    /* conf files go into ~/.grass8/r.li/ */
    sprintf(rlipath, "%s%c%s%c", G_config_path(), HOST_DIRSEP, "r.li",
            HOST_DIRSEP);
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
    /* conf files go into ~/.grass8/r.li/ */
    sprintf(rlipath, "%s%c%s%c", G_config_path(), HOST_DIRSEP, "r.li",
            HOST_DIRSEP);
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
	/* conf files go into ~/.grass8/r.li/ */
    sprintf(rlipath, "%s%c%s%c", G_config_path(), HOST_DIRSEP, "r.li", HOST_DIRSEP);
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    /* conf files go into ~/.grass8/r.li/ */
    sprintf(rlipath, "%s%c%s%c", G_config_path(), HOST_DIRSEP, "r.li",
            HOST_DIRSEP);
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
    /* conf files go into ~/.grass8/r.li/ */
    sprintf(rlipath, "%s%c%s%c", G_config_path(), HOST_DIRSEP, "r.li",
            HOST_DIRSEP);
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
	/* conf files go into ~/.grass8/r.li/ */
    sprintf(rlipath, "%s%c%s%c", G_config_path(), HOST_DIRSEP, "r.li", HOST_DIRSEP);
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
	/* conf files go into ~/.grass8/r.li/ */
    sprintf(rlipath, "%s%c%s%c", G_config_path(), HOST_DIRSEP, "r.li", HOST_DIRSEP);
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
	/* conf files go into ~/.grass8/r.li/ */
    sprintf(rlipath, "%s%c%s%c", G_config_path(), HOST_DIRSEP, "r.li", HOST_DIRSEP);
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
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

    sprintf(testpath, "%s%c%s%c", G_config_path(), HOST_DIRSEP, "r.li",
            HOST_DIRSEP);
    if (strncmp(file, testpath, strlen(testpath)) == 0)
        file += strlen(testpath);

    /* TODO: check if this path is portable */
    /* TODO: use G_rc_path() */
    sprintf(pathSetup, "%s%s", rlipath, file);
    G_debug(1, "r.li.daemon pathSetup: [%s]", pathSetup);
    parsed = parseSetup(pathSetup, l, g, raster);

    /*########################################################
       -----------------open output file ---------------------
       ####################################################### */

    if (parsed == MVWIN) {
        /* struct Cell_head cellhd_r, cellhd_new;
           char *mapset; */
        /*creating new raster file */
        mv_fd = Rast_open_new(output, DCELL_TYPE);

        random_access_name = G_tempfile();
        random_access = open(random_access_name, O_RDWR | O_CREAT, 0755);
        if (random_access == -1)
            G_fatal_error(_("Cannot create random access file"));
    }
    else {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
>>>>>>> osgeo-main
	/* text file output */
	/* check if ~/.grass8/ exists */
<<<<<<< HEAD
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
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
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
	/* text file output */
	/* check if ~/.grass8/ exists */
<<<<<<< HEAD
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
        /* text file output */
        /* check if ~/.grass8/ exists */
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
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
	/* text file output */
	/* check if ~/.grass8/ exists */
<<<<<<< HEAD
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        /* text file output */
        /* check if ~/.grass8/ exists */
=======
	/* text file output */
	/* check if ~/.grass8/ exists */
<<<<<<< HEAD
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
        sprintf(out, "%s", G_config_path());
        doneDir = G_mkdir(out);
        if (doneDir == -1 && errno != EEXIST)
            G_fatal_error(_("Cannot create %s directory"), out);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
        /* check if ~/.grass8/r.li/ exists */
        sprintf(out, "%s", rlipath);
        doneDir = G_mkdir(out);
        if (doneDir == -1 && errno != EEXIST)
            G_fatal_error(_("Cannot create %s directory"), out);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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

        /* check if ~/.grass7/r.li/output exists */
        if (snprintf(out, GPATH_MAX, "%s%s", rlipath, "output") >= GPATH_MAX)
            G_fatal_error(_("Filepath '%s%s' exceeds max length"), rlipath,
                          "output");
        doneDir = G_mkdir(out);
        if (doneDir == -1 && errno != EEXIST)
            G_fatal_error(_("Cannot create %s directory"), out);
        if (snprintf(out, GPATH_MAX, "%s%s%c%s", rlipath, "output", HOST_DIRSEP,
                     output) >= GPATH_MAX)
            G_fatal_error(_("Filepath '%s%s%c%s' exceeds max length"), rlipath,
                          "output", HOST_DIRSEP, output);
        if ((res = open(out, O_WRONLY | O_CREAT | O_TRUNC, 0644)) == -1)
            G_fatal_error(_("Cannot create %s output"), out);
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
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> osgeo-main
	/* check if ~/.grass8/r.li/ exists */
	sprintf(out, "%s", rlipath);
	doneDir = G_mkdir(out);
	if (doneDir == -1 && errno != EEXIST)
	    G_fatal_error(_("Cannot create %s directory"), out);

	/* check if ~/.grass8/r.li/output exists */
	sprintf(out, "%s%s", rlipath, "output");
	doneDir = G_mkdir(out);
	if (doneDir == -1 && errno != EEXIST)
	    G_fatal_error(_("Cannot create %s directory"), out);
	sprintf(out, "%s%s%c%s", rlipath, "output", HOST_DIRSEP, output);
	res = open(out, O_WRONLY | O_CREAT | O_TRUNC, 0644);
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
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
        /* check if ~/.grass7/r.li/output exists */
        if (snprintf(out, GPATH_MAX, "%s%s", rlipath, "output") >= GPATH_MAX)
            G_fatal_error(_("Filepath '%s%s' exceeds max length"), rlipath,
                          "output");
        doneDir = G_mkdir(out);
        if (doneDir == -1 && errno != EEXIST)
            G_fatal_error(_("Cannot create %s directory"), out);
        if (snprintf(out, GPATH_MAX, "%s%s%c%s", rlipath, "output", HOST_DIRSEP,
                     output) >= GPATH_MAX)
            G_fatal_error(_("Filepath '%s%s%c%s' exceeds max length"), rlipath,
                          "output", HOST_DIRSEP, output);
        if ((res = open(out, O_WRONLY | O_CREAT | O_TRUNC, 0644)) == -1)
            G_fatal_error(_("Cannot create %s output"), out);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
    }

    /*#######################################################
       ------------------analysis loop----------------------
       ####################################################### */

    /*body */
    while (next_Area(parsed, l, g, &m) != 0) {
        worker_process(&doneJob, &m);

        /*perc++; */
        /*G_percent (perc, WORKERS, 1); */
        if (doneJob.type == DONE) {
            /* double result;

               result = doneJob.f.f_d.res; */
            /* output */
            if (parsed != MVWIN) {
                /* text file output */
                print_Output(res, doneJob);
            }
            else {
                /* raster output */
                raster_Output(random_access, doneJob.f.f_d.aid, g,
                              doneJob.f.f_d.res);
            }
        }
        else {
            if (parsed != MVWIN) {
                /* text file output */
                error_Output(res, doneJob);
            }
            else {
                /* printf("todo"); fflush(stdout); */
                /* TODO write to raster NULL ??? */
            }
        }
    }

    worker_end();

    /*################################################
       --------------delete tmp files------------------
       ################################################ */

    if (parsed == MVWIN) {
        write_raster(mv_fd, random_access, g);
        close(random_access);
        unlink(random_access_name);
        Rast_close(mv_fd);
        Rast_short_history(output, "raster", &history);
        Rast_command_history(&history);
        Rast_write_history(output, &history);
        G_done_msg(_("Raster map <%s> created."), output);
    }
    else {
        /* text file output */
        G_done_msg("Result written to text file <%s>", out);
    }

    /* This is only return in this function, so the documented 1 is
       actually never returned. */
    return 0;
}

int parseSetup(char *path, struct list *l, struct g_area *g, char *raster)
{
    struct stat s;
    struct Cell_head cellhd;
    char *buf;
    const char *token;
    int setup;
    int letti;
    double rel_x, rel_y, rel_rl, rel_cl;

    /* double sf_n, sf_s, sf_e, sf_w; */
    int sf_x, sf_y, sf_rl, sf_cl;
    int sa_x, sa_y, sa_rl, sa_cl;
    int size;

    if (stat(path, &s) != 0)
        G_fatal_error(_("Cannot find configuration file <%s>"), path);

    size = s.st_size * sizeof(char);
    buf = G_malloc(size);

    setup = open(path, O_RDONLY, 0755);
    if (setup == -1)
        G_fatal_error(_("Cannot read setup file"));

    letti = read(setup, buf, s.st_size);
    if (letti < s.st_size)
        G_fatal_error(_("Cannot read setup file"));

    token = strtok(buf, " ");
    if (strcmp("SAMPLINGFRAME", token) != 0)
        G_fatal_error(_("Unable to parse configuration file (sampling frame)"));

    rel_x = atof(strtok(NULL, "|"));
    rel_y = atof(strtok(NULL, "|"));
    rel_rl = atof(strtok(NULL, "|"));
    rel_cl = atof(strtok(NULL, "\n"));

    /* use current region ! */
    Rast_get_window(&cellhd);

    /* calculate absolute sampling frame definition */
    sf_x = (int)rint(cellhd.cols * rel_x);
    sf_y = (int)rint(cellhd.rows * rel_y);
    sf_rl = (int)rint(cellhd.rows * rel_rl);
    sf_cl = (int)rint(cellhd.cols * rel_cl);

    /* sanity check */
    if (sf_x < 0)
        sf_x = 0;
    if (sf_y < 0)
        sf_y = 0;
    if (sf_x > cellhd.cols)
        sf_x = cellhd.cols;
    if (sf_y > cellhd.rows)
        sf_y = cellhd.rows;
    if (sf_rl > cellhd.rows - sf_y)
        sf_rl = cellhd.rows - sf_y;
    if (sf_cl > cellhd.cols - sf_x)
        sf_cl = cellhd.cols - sf_x;

    /* calculate sample frame boundaries */
    /* sf_n = cellhd.north - (cellhd.ns_res * sf_y);
       sf_s = sf_n - (cellhd.ns_res * sf_rl);
       sf_w = cellhd.west + (cellhd.ew_res * sf_x);
       sf_e = sf_w + (cellhd.ew_res * sf_cl); */

    /* parse configuration file */
    token = strtok(NULL, " ");

    if (strcmp("SAMPLEAREA", token) == 0) {
        double rel_sa_x, rel_sa_y, rel_sa_rl, rel_sa_cl;
        int aid = 1, toReturn;

        do {
            rel_sa_x = atof(strtok(NULL, "|"));
            rel_sa_y = atof(strtok(NULL, "|"));
            rel_sa_rl = atof(strtok(NULL, "|"));
            rel_sa_cl = atof(strtok(NULL, "\n"));

            if (rel_sa_x == -1.0 && rel_sa_y == -1.0) {
                /* runtime disposition */

                sa_rl = (int)rint(cellhd.rows * rel_sa_rl);
                sa_cl = (int)rint(cellhd.cols * rel_sa_cl);

                /* sanity check */
                if (sa_rl > cellhd.rows - sf_y)
                    sa_rl = cellhd.rows - sf_y;
                if (sa_cl > cellhd.cols - sf_x)
                    sa_cl = cellhd.cols - sf_x;

                /* total sample area */
                g->rows = sf_rl;
                g->cols = sf_cl;
                g->x = sf_x;
                g->y = sf_y;
                /* current sample area (subset of total sample area) */
                g->rl = sa_rl;
                g->cl = sa_cl;
                g->sf_x = sf_x;
                g->sf_y = sf_y;

                g->count = 1;
                g->maskname = NULL;

                return disposeAreas(l, g, strtok(NULL, "\n"));
            }
            else {
                msg m;

                toReturn = NORMAL;
                /*read file and create list */
                m.type = AREA;
                /* current sample area (subset of total sample area) */
                sa_x = (int)rint(cellhd.cols * rel_sa_x);
                sa_y = (int)rint(cellhd.rows * rel_sa_y);
                sa_rl = (int)rint(cellhd.rows * rel_sa_rl);
                sa_cl = (int)rint(cellhd.cols * rel_sa_cl);

                /* sanity check */
                if (sa_x < 0)
                    sa_x = 0;
                if (sa_y < 0)
                    sa_y = 0;
                if (sa_x > cellhd.cols)
                    sa_x = cellhd.cols;
                if (sa_y > cellhd.rows)
                    sa_y = cellhd.rows;
                if (sa_rl > cellhd.rows - sa_y)
                    sa_rl = cellhd.rows - sa_y;
                if (sa_cl > cellhd.cols - sa_x)
                    sa_cl = cellhd.cols - sa_x;

                m.f.f_a.x = sa_x;
                m.f.f_a.y = sa_y;
                m.f.f_a.rl = sa_rl;
                m.f.f_a.cl = sa_cl;
                m.f.f_a.aid = aid;
                aid++;
                insertNode(l, m);
            }

        } while ((token = strtok(NULL, " ")) != NULL &&
                 strcmp(token, "SAMPLEAREA") == 0);

        close(setup);
        return toReturn;
    }
    else if (strcmp("MASKEDSAMPLEAREA", token) == 0) {
        double rel_sa_x, rel_sa_y, rel_sa_rl, rel_sa_cl;
        int aid = 1;
        char maskname[GNAME_MAX] = {'\0'};

        do {
            rel_sa_x = atof(strtok(NULL, "|"));
            rel_sa_y = atof(strtok(NULL, "|"));
            rel_sa_rl = atof(strtok(NULL, "|"));
            rel_sa_cl = atof(strtok(NULL, "|"));
            strcpy(maskname, strtok(NULL, "\n"));

            if (rel_sa_x == -1 && rel_sa_y == -1) {
                /* runtime disposition */

                sa_rl = (int)rint(cellhd.rows * rel_sa_rl);
                sa_cl = (int)rint(cellhd.cols * rel_sa_cl);

                /* sanity check */
                if (sa_rl > cellhd.rows - sf_y)
                    sa_rl = cellhd.rows - sf_y;
                if (sa_cl > cellhd.cols - sf_x)
                    sa_cl = cellhd.cols - sf_x;

                /* total sample area */
                g->rows = sf_rl;
                g->cols = sf_cl;
                g->x = sf_x;
                g->y = sf_y;
                /* current sample area (subset of total sample area) */
                g->rl = sa_rl;
                g->cl = sa_cl;
                g->count = 1;
                g->maskname = maskname;
                return disposeAreas(l, g, strtok(NULL, "\n"));
            }
            else {
                /*read file and create list */
                msg m;

                m.type = MASKEDAREA;
                /* current sample area (subset of total sample area) */
                sa_x = (int)rint(cellhd.cols * rel_sa_x);
                sa_y = (int)rint(cellhd.rows * rel_sa_y);
                sa_rl = (int)rint(cellhd.rows * rel_sa_rl);
                sa_cl = (int)rint(cellhd.cols * rel_sa_cl);

                /* sanity check */
                if (sa_x < 0)
                    sa_x = 0;
                if (sa_y < 0)
                    sa_y = 0;
                if (sa_x > cellhd.cols)
                    sa_x = cellhd.cols;
                if (sa_y > cellhd.rows)
                    sa_y = cellhd.rows;
                if (sa_rl > cellhd.rows - sa_y)
                    sa_rl = cellhd.rows - sa_y;
                if (sa_cl > cellhd.cols - sa_x)
                    sa_cl = cellhd.cols - sa_x;

                m.f.f_ma.x = sa_x;
                m.f.f_ma.y = sa_y;
                m.f.f_ma.rl = sa_rl;
                m.f.f_ma.cl = sa_cl;
                m.f.f_ma.aid = aid;
                strcpy(m.f.f_ma.mask, maskname);
                aid++;
                insertNode(l, m);
            }
        }

        while ((token = strtok(NULL, " ")) != NULL &&
               strcmp(token, "MASKEDSAMPLEAREA") == 0);

        close(setup);
        return NORMAL;
    }
    else if (strcmp("MASKEDOVERLAYAREA", token) == 0) {
        double sa_n, sa_s, sa_w, sa_e;
        int aid = 1;
        char maskname[GNAME_MAX] = {'\0'};
        msg m;

        /* Get the window setting. g.region raster=<input raster> */
        /*   ? same as cellhd above ? */
        /* no. the current window might be different */

        do {
            strcpy(maskname, strtok(NULL, "|"));
            sa_n = atof(strtok(NULL, "|"));
            sa_s = atof(strtok(NULL, "|"));
            sa_e = atof(strtok(NULL, "|"));
            sa_w = atof(strtok(NULL, "\n"));

            m.type = MASKEDAREA;

            /* Each input overlay area from input vector are converted to
               raster via v.to.rast. See r.li.setup/sample_area_vector.sh.
               This is used only for reading the region (NS, EW). */

            /* current sample area (subset of total sample area) */

            /* Get start x and y position of masked overlay raster with
               respect to current region.
               sa_n, sa_w are read from configuration file. */
            sa_x = (int)rint((sa_w - cellhd.west) / cellhd.ew_res);
            sa_y = (int)rint((cellhd.north - sa_n) / cellhd.ns_res);

            /* Get row count and column count of overlay raster */
            sa_rl = (int)rint((sa_n - sa_s) / cellhd.ns_res);
            sa_cl = (int)rint((sa_e - sa_w) / cellhd.ew_res);

            /* sanity check */
            if (sa_x < 0)
                sa_x = 0;
            if (sa_y < 0)
                sa_y = 0;
            if (sa_x > cellhd.cols)
                sa_x = cellhd.cols;
            if (sa_y > cellhd.rows)
                sa_y = cellhd.rows;
            if (sa_rl > cellhd.rows - sa_y)
                sa_rl = cellhd.rows - sa_y;
            if (sa_cl > cellhd.cols - sa_x)
                sa_cl = cellhd.cols - sa_x;

            m.f.f_ma.x = sa_x;
            m.f.f_ma.y = sa_y;
            m.f.f_ma.rl = sa_rl;
            m.f.f_ma.cl = sa_cl;
            m.f.f_ma.aid = aid;
            strcpy(m.f.f_ma.mask, maskname);
            aid++;
            insertNode(l, m);
        }

        while ((token = strtok(NULL, " ")) != NULL &&
               (strcmp(token, "MASKEDOVERLAYAREA") == 0));

        if (strcmp(token, "RASTERMAP") != 0)
            G_fatal_error(_("Irregular MASKEDOVERLAY areas definition"));

        token = strtok(NULL, "\n");
        if (strcmp(token, raster) != 0)
            G_fatal_error(_("The configuration file can only be used "
                            "with the <%s> raster map"),
                          token);
        close(setup);
        return NORMAL;
    }
    else
        G_fatal_error(_("Unable to parse configuration file (sample area)"));

    close(setup);
    return ERROR;
}

int disposeAreas(struct list *l, struct g_area *g, char *def)
{
    char *token;

    token = strtok(def, " \n");
    if (strcmp(token, "MOVINGWINDOW") == 0) {
        g->count = 0;
        g->dist = 0;
        g->add_row = 1;
        g->add_col = 1;
        if (g->rl != 1)
            g->rows = g->rows - g->rl + 1;
        else
            g->rows = g->rows;
        if (g->cl != 1)
            g->cols = g->cols - g->cl + 1;
        return MVWIN;
    }
    else if (strcmp(token, "RANDOMNONOVERLAPPING") == 0) {
        int units, sf_rl, sf_cl, sa_rl, sa_cl, max_units, i;
        int *assigned;

        sscanf(strtok(NULL, "\n"), "%i", &units);
        sf_rl = g->rows;
        sf_cl = g->cols;
        sa_rl = g->rl;
        sa_cl = g->cl;
        max_units = (int)rint((sf_rl / sa_rl) * (sf_cl / sa_cl));
        if (units > max_units)
            G_fatal_error(_("Too many units to place"));
        assigned = G_malloc(units * sizeof(int));
        i = 0;
        G_srand48(0);
        while (i < units) {
            int j, position, found = FALSE;

            position = G_lrand48() % max_units;
            for (j = 0; j < i; j++) {
                if (assigned[j] == position)
                    found = TRUE;
            }
            if (!found) {
                msg m;

                assigned[i] = position;
                i++;
                if (g->maskname == NULL) {
                    int n_col = rint(sf_cl / sa_cl);

                    m.type = AREA;
                    m.f.f_a.aid = i;
                    m.f.f_a.x = g->sf_x + (position % n_col) * sa_cl;
                    m.f.f_a.y = g->sf_y + (position / n_col) * sa_rl;
                    m.f.f_a.rl = sa_rl;
                    m.f.f_a.cl = sa_cl;
                    insertNode(l, m);
                }
                else {
                    int n_col = sf_cl / sa_cl;

                    m.type = MASKEDAREA;
                    m.f.f_ma.aid = i;
                    m.f.f_a.x = g->sf_x + (position % n_col) * sa_cl;
                    m.f.f_a.y = g->sf_y + (position / n_col) * sa_rl;
                    m.f.f_ma.rl = sa_rl;
                    m.f.f_ma.cl = sa_cl;
                    strcpy(m.f.f_ma.mask, g->maskname);
                    insertNode(l, m);
                }
            }
        }
        return NORMAL;
    }
    else if (strcmp(token, "SYSTEMATICCONTIGUOUS") == 0) {
        g->dist = 0;
        g->add_row = g->rl;
        g->add_col = g->cl;
        return GEN;
    }
    else if (strcmp(token, "SYSTEMATICNONCONTIGUOUS") == 0) {
        int dist;

        dist = atoi(strtok(NULL, "\n"));
        g->dist = dist;
        g->add_row = g->rl + dist;
        g->add_col = g->cl + dist;
        g->x = g->sf_x + dist;
        g->y = g->sf_y + dist;
        return GEN;
    }
    else if (strcmp(token, "STRATIFIEDRANDOM") == 0) {
        int r_strat, c_strat, r_strat_len, c_strat_len, loop, i;

        r_strat = atoi(strtok(NULL, "|"));
        c_strat = atoi(strtok(NULL, "\n"));
        r_strat_len = (int)rint(g->rows / r_strat);
        c_strat_len = (int)rint(g->cols / c_strat);
        if (r_strat_len < g->rl || c_strat_len < g->cl)
            G_fatal_error(
                _("Too many stratified random sample for raster map"));
        loop = r_strat * c_strat;
        G_srand48(0);
        for (i = 0; i < loop; i++) {
            msg m;

            if (g->maskname == NULL) {
                m.type = AREA;
                m.f.f_a.aid = i;
                m.f.f_a.x = (int)g->sf_x + ((i % c_strat) * c_strat_len) +
                            (G_lrand48() % (c_strat_len - g->cl));
                m.f.f_a.y = (int)g->sf_y + (rint(i / c_strat) * r_strat_len) +
                            (G_lrand48() % (r_strat_len - g->rl));
                m.f.f_a.rl = g->rl;
                m.f.f_a.cl = g->cl;
                insertNode(l, m);
            }
            else {
                m.type = MASKEDAREA;
                m.f.f_ma.aid = i;
                m.f.f_ma.x = (int)g->sf_x + ((i % c_strat) * c_strat_len) +
                             (G_lrand48() % (c_strat_len - g->cl));
                m.f.f_ma.y = (int)g->sf_y + (rint(i / c_strat) * r_strat_len) +
                             (G_lrand48() % (r_strat_len - g->rl));
                m.f.f_ma.rl = g->rl;
                m.f.f_ma.cl = g->cl;
                strcpy(m.f.f_ma.mask, g->maskname);
                insertNode(l, m);
            }
        }
        return NORMAL;
    }
    else {
        G_fatal_error(_("Illegal areas disposition"));
        return NORMAL;
    }
    return ERROR;
}

int next_Area(int parsed, struct list *l, struct g_area *g, msg *m)
{
    if (parsed == NORMAL) {
        if (l->size == 0)
            return 0;
        else {
            msg tmp;

            memcpy(&tmp, l->head->m, sizeof(msg));
            *m = tmp;
            removeNode(l);
            return 1;
        }
    }
    else {
        return next(g, m);
    }
}

int print_Output(int out, msg m)
{
    if (m.type != DONE)
        return 0;
    else {
        char s[100];
        int len;

        if (Rast_is_d_null_value(&m.f.f_d.res))
            sprintf(s, "RESULT %i|NULL\n", m.f.f_d.aid);
        else
            sprintf(s, "RESULT %i|%.15g\n", m.f.f_d.aid, m.f.f_d.res);
        len = strlen(s);

        if (write(out, s, len) == len)
            return 1;
        else
            return 0;
    }
}

int error_Output(int out, msg m)
{
    if (m.type != ERROR)
        return 0;
    else {
        char s[100];

        sprintf(s, "ERROR %i", m.f.f_d.aid);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
>>>>>>> osgeo-main
        if (write(out, s, strlen(s)) == strlen(s))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(out, s, strlen(s)) == strlen(s))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (write(out, s, strlen(s)) == strlen(s))
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
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
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
        if (write(out, s, strlen(s)) == strlen(s))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(out, s, strlen(s)) == strlen(s))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
        if (write(out, s, strlen(s)) == strlen(s))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(out, s, strlen(s)) == strlen(s))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (write(out, s, strlen(s)) == (ssize_t)strlen(s))
=======
        if (write(out, s, strlen(s)) == strlen(s))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(out, s, strlen(s)) == strlen(s))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
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
            return 1;
        else
            return 0;
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
int raster_Output(int fd, int aid, struct g_area *g UNUSED, double res)
=======
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
int raster_Output(int fd, int aid, struct g_area *g UNUSED, double res)
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int raster_Output(int fd, int aid, struct g_area *g UNUSED, double res)
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
int raster_Output(int fd, int aid, struct g_area *g UNUSED, double res)
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
int raster_Output(int fd, int aid, struct g_area *g, double res)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
{
    double toPut = res;
    off_t offset = (off_t)aid * sizeof(double);

    if (lseek(fd, offset, SEEK_SET) != offset) {
        G_message(_("Cannot make lseek"));
        return -1;
    }

    if (write(fd, &toPut, sizeof(double)) == 0)
        return 1;
    else
        return 0;
}

int write_raster(int mv_fd, int random_access, struct g_area *g)
{
    int i = 0, j = 0, letti = 0;
    double *file_buf;
    DCELL *cell_buf;
    int cols, rows, center;

    cols = g->cols;
    rows = g->rows;
    center = g->sf_x + ((int)g->cl / 2);

    file_buf = G_malloc(cols * sizeof(double));
    lseek(random_access, 0, SEEK_SET);

    cell_buf = Rast_allocate_d_buf();
    Rast_set_d_null_value(cell_buf, Rast_window_cols() + 1);

    for (i = 0; i < g->sf_y + ((int)g->rl / 2); i++) {
        Rast_put_row(mv_fd, cell_buf, DCELL_TYPE);
    }

    for (i = 0; i < rows; i++) {
        letti = read(random_access, file_buf, (cols * sizeof(double)));

        if (letti == -1)
            G_message("%s", strerror(errno));

        for (j = 0; j < cols; j++) {
            cell_buf[j + center] = file_buf[j];
        }

        Rast_put_row(mv_fd, cell_buf, DCELL_TYPE);
    }

    Rast_set_d_null_value(cell_buf, Rast_window_cols() + 1);

    for (i = 0; i < Rast_window_rows() - g->sf_y - ((int)g->rl / 2) - g->rows;
         i++) {
        Rast_put_row(mv_fd, cell_buf, DCELL_TYPE);
    }

    G_free(file_buf);
    G_free(cell_buf);

    return 1;
}
