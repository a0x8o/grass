#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <libgen.h>
#include <grass/gis.h>
#include <grass/spawn.h>
#include <grass/display.h>
#include <grass/glocale.h>

#include "proto.h"

static char *start(const char *, const char *, int, int, int);
static char *start_wx(const char *, const char *, int, int, int);
static void error_handler(void *);

/* start file-based monitor */
char *start(const char *name, const char *output, int width, int height,
            int update)
{
    char *output_path;
    const char *output_name;

    /* stop monitor on failure */
    G_add_error_handler(error_handler, (char *)name);

    /* full path for output file */
    output_path = (char *)G_malloc(GPATH_MAX);
    output_path[0] = '\0';

    if (!output) {
        char buff[512];

        sprintf(buff, "GRASS_RENDER_IMMEDIATE=%s", name);
        putenv(G_store(buff));
        sprintf(buff, "GRASS_RENDER_WIDTH=%d", width);
        putenv(G_store(buff));
        sprintf(buff, "GRASS_RENDER_HEIGHT=%d", height);
        putenv(G_store(buff));

        D_open_driver();

        output_name = D_get_file();
        if (!output_name)
            return NULL;
        if (!update && access(output_name, F_OK) == 0) {
            if (G_get_overwrite()) {
                G_warning(_("File <%s> already exists and will be overwritten"),
                          output_name);
                D_setup_unity(0);
                D_erase("white");
            }
            else
                G_fatal_error(_("option <%s>: <%s> exists. To overwrite, use "
                                "the --overwrite flag"),
                              "output", output_name);
        }
        D_close_driver(); /* must be called after check because this
                           * function produces default map file */
        putenv("GRASS_RENDER_IMMEDIATE=");
    }
    else {
        char *dir_name;

        output_name = output;
        /* check write permission */
        dir_name = G_store(output_name);
        if (access(dirname(dir_name), W_OK) != 0)
            G_fatal_error(_("Unable to start monitor, don't have "
                            "write permission for <%s>"),
                          output_name);
        G_free(dir_name);

        /* check if file exists */
        if (!update && access(output_name, F_OK) == 0) {
            if (G_get_overwrite()) {
                G_warning(_("File <%s> already exists and will be overwritten"),
                          output_name);
                if (0 != unlink(output_name))
                    G_fatal_error(_("Unable to delete <%s>"), output_name);
            }
        }
    }

    if (!strchr(output_name, HOST_DIRSEP)) { /* relative path */
        char *ptr;

        if (!getcwd(output_path, GPATH_MAX))
            G_fatal_error(_("Unable to get current working directory"));
        ptr = output_path + strlen(output_path) - 1;
        if (*(ptr++) != HOST_DIRSEP) {
            *(ptr++) = HOST_DIRSEP;
            *(ptr) = '\0';
        }
        strcat(output_path, output_name);
        G_message(_("Output file: %s"), output_path);
    }
    else {
        strcpy(output_path, output_name); /* already full path */
    }

    return output_path;
}

/* start wxGUI display monitor */
char *start_wx(const char *name, const char *element, int width, int height,
               int x_only)
{
    char progname[GPATH_MAX], mon_path[GPATH_MAX];
    char str_width[1024], str_height[1024], *str_x_only;
    char *mapfile;

    /* full path */
    mapfile = (char *)G_malloc(GPATH_MAX);
    mapfile[0] = '\0';

    sprintf(progname, "%s/gui/wxpython/mapdisp/main.py", G_gisbase());
    sprintf(str_width, "%d", width);
    sprintf(str_height, "%d", height);

    if (x_only)
        str_x_only = "1";
    else
        str_x_only = "0";

    G_file_name(mon_path, element, NULL, G_mapset());
    G_spawn_ex(getenv("GRASS_PYTHON"), progname, progname, name, mon_path,
               str_width, str_height, str_x_only, SF_BACKGROUND, NULL);

    G_file_name(mapfile, element, "map.ppm", G_mapset());

    return mapfile;
}

int start_mon(const char *name, const char *output, int select, int width,
              int height, const char *bgcolor, int truecolor, int x_only,
              int update)
{
    char *mon_path;
    char *out_file, *env_file, *cmd_file, *leg_file;
    char buf[1024];
    char file_path[GPATH_MAX], render_cmd_path[GPATH_MAX];
    int fd;

    if (check_mon(name)) {
        const char *curr_mon;

        curr_mon = G_getenv_nofatal("MONITOR");
        if (select && (!curr_mon || strcmp(curr_mon, name) != 0))
            G_setenv("MONITOR", name);

        G_fatal_error(_("Monitor <%s> already running"), name);
    }

    G_verbose_message(_("Starting monitor <%s>..."), name);

    /* create .tmp/HOSTNAME/u_name directory */
    mon_path = get_path(name, FALSE);
    G_make_mapset_element(mon_path);

    G_file_name(file_path, mon_path, "env", G_mapset());
    env_file = G_store(file_path);
    G_file_name(file_path, mon_path, "cmd", G_mapset());
    cmd_file = G_store(file_path);
    G_file_name(file_path, mon_path, "leg", G_mapset());
    leg_file = G_store(file_path);

    /* create py file (renderer) */
    sprintf(render_cmd_path, "%s/etc/d.mon/render_cmd.py", getenv("GISBASE"));
    G_file_name(file_path, mon_path, "render.py", G_mapset());
    G_debug(1, "Monitor name=%s, pyfile = %s", name, file_path);
    if (1 != G_copy_file(render_cmd_path, file_path))
        G_fatal_error(_("Unable to copy render command file"));

    /* start monitor */
    if (strncmp(name, "wx", 2) == 0)
        out_file = start_wx(name, mon_path, width, height, x_only);
    else
        out_file = start(name, output, width, height, update);

    /* create env file (environmental variables used for rendering) */
    G_debug(1, "Monitor name=%s, envfile=%s", name, env_file);
    fd = creat(env_file, 0666);
    if (fd < 0)
        G_fatal_error(_("Unable to create file <%s>"), env_file);

    if (G_strncasecmp(name, "wx", 2) == 0) {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=default\n"); /* TODO: read settings
                                                             from wxGUI */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> osgeo-main
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
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
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
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
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
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
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> osgeo-main
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
=======
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
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
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
<<<<<<< HEAD
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
<<<<<<< HEAD
=======
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
<<<<<<< HEAD
    if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
<<<<<<< HEAD
    if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
<<<<<<< HEAD
    if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
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
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    sprintf(buf, "GRASS_RENDER_FILE=%s\n", out_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_WIDTH=%d\n", width);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_RENDER_HEIGHT=%d\n", height);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
    sprintf(buf, "GRASS_LEGEND_FILE=%s\n", leg_file);
    if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))

    if (bgcolor) {
        if (strcmp(bgcolor, "none") == 0)
            sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        else
            sprintf(buf, "GRASS_RENDER_BACKGROUNDCOLOR=%s\n", bgcolor);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
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
<<<<<<< HEAD
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
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    if (truecolor) {
        sprintf(buf, "GRASS_RENDER_TRUECOLOR=TRUE\n");
<<<<<<< HEAD
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> osgeo-main
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    if (truecolor) {
        sprintf(buf, "GRASS_RENDER_TRUECOLOR=TRUE\n");
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    if (truecolor) {
        sprintf(buf, "GRASS_RENDER_TRUECOLOR=TRUE\n");
<<<<<<< HEAD
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
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
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
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
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    if (truecolor) {
        sprintf(buf, "GRASS_RENDER_TRUECOLOR=TRUE\n");
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    close(fd);

    /* create cmd file (list of GRASS display commands to render) */
    G_debug(1, "Monitor name=%s, cmdfile = %s", name, cmd_file);
    if (0 > creat(cmd_file, 0666))
        G_fatal_error(_("Unable to create file <%s>"), cmd_file);

    /* select monitor if requested */
    if (select)
        G_setenv("MONITOR", name);

    G_free(mon_path);
    G_free(out_file);
    G_free(env_file);

    return 0;
}

void error_handler(void *p)
{
    const char *name = (const char *)p;

    stop_mon(name);
}
