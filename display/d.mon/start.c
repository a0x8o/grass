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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 558d40de40 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2940bcf2c1 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
>>>>>>> f063811cb8 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67806956ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 8f6808ee3d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 99ec0a9e3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b339c662ab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1cabd030d3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> cdd2375514 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1e595a59e6 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4eab8f90cb (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 28e7b3b34d (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6007b09add (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7b9fb7e19e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 81fd408422 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
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
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
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
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
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
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
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
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
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
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
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
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
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
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
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
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
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
=======
<<<<<<< HEAD
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
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
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
<<<<<<< HEAD
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
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
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_FILE_READ=FALSE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
        sprintf(buf, "GRASS_RENDER_TRANSPARENT=TRUE\n");
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
<<<<<<< HEAD
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
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
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
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
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
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
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
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
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
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
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
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
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
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
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
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
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
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
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
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
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
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
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
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
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
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
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
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
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
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
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
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    else {
        sprintf(buf, "GRASS_RENDER_IMMEDIATE=%s\n", name);
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
        G_fatal_error(_("Failed to write to file <%s>"), env_file);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81fd408422 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7b9fb7e19e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
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
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
>>>>>>> 81fd408422 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
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
<<<<<<< HEAD
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    if (truecolor) {
        sprintf(buf, "GRASS_RENDER_TRUECOLOR=TRUE\n");
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7b9fb7e19e (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 558d40de40 (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    if (truecolor) {
        sprintf(buf, "GRASS_RENDER_TRUECOLOR=TRUE\n");
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    if (truecolor) {
        sprintf(buf, "GRASS_RENDER_TRUECOLOR=TRUE\n");
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7b9fb7e19e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 28e7b3b34d (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4eab8f90cb (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1e595a59e6 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cdd2375514 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 1cabd030d3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b339c662ab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 99ec0a9e3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8f6808ee3d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 67806956ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
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
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    if (truecolor) {
        sprintf(buf, "GRASS_RENDER_TRUECOLOR=TRUE\n");
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
            G_fatal_error(_("Failed to write to file <%s>"), env_file);
    }
    if (truecolor) {
        sprintf(buf, "GRASS_RENDER_TRUECOLOR=TRUE\n");
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
>>>>>>> 28e7b3b34d (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
>>>>>>> 4eab8f90cb (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
>>>>>>> 1e595a59e6 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
>>>>>>> cdd2375514 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
>>>>>>> 1cabd030d3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
>>>>>>> b339c662ab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
>>>>>>> 99ec0a9e3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
>>>>>>> 8f6808ee3d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
>>>>>>> 67806956ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
>>>>>>> 558d40de40 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
>>>>>>> 2940bcf2c1 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28e7b3b34d (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4eab8f90cb (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1e595a59e6 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cdd2375514 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1cabd030d3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b339c662ab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99ec0a9e3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f6808ee3d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67806956ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 558d40de40 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2940bcf2c1 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f063811cb8 (r.horizon manual - fix typo (#2794))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28e7b3b34d (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
>>>>>>> 4eab8f90cb (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1e595a59e6 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
>>>>>>> cdd2375514 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1cabd030d3 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
>>>>>>> b339c662ab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99ec0a9e3c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
>>>>>>> 8f6808ee3d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67806956ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f063811cb8 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 558d40de40 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
>>>>>>> 2940bcf2c1 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28e7b3b34d (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4eab8f90cb (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1e595a59e6 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cdd2375514 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1cabd030d3 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b339c662ab (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99ec0a9e3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f6808ee3d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67806956ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f063811cb8 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 558d40de40 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2940bcf2c1 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f063811cb8 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
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
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
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
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
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
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28e7b3b34d (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 5952770ec6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d01c2a12f1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 4130b8db48 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1e595a59e6 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> f76eb8a5c2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3e5aeb1393 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cdd2375514 (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 00f0aa1333 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ef6112573 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1cabd030d3 (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 10cb905c76 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d365e50fab (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b339c662ab (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 24ce20f07c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dc8416910a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 99ec0a9e3c (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> d3f123638e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b2d4dc1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f6808ee3d (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 580af7cb72 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ae49d6292b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67806956ee (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> c7104d8e5e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 060d4359ef (r.horizon manual - fix typo (#2794))
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
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 51c6907b22 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 558d40de40 (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 2656f886ff (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2727f115f1 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2940bcf2c1 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 1a771fd4a9 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d8b2703006 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 6cd91d8b03 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> c66f377132 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9eb4ab8390 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
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
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 576b696e91 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
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
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 50e307f19e (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 70e2d172cf (r.horizon manual - fix typo (#2794))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
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
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 81fd408422 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
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
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7b9fb7e19e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
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
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 6007b09add (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
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
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
>>>>>>> 50fc95a76f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c2460610a9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> a2c0a963b1 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28e7b3b34d (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
>>>>>>> 770600e1cd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> 3ee8648585 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 4eab8f90cb (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 97a4a9ea37 (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
=======
        if (write(fd, buf, strlen(buf)) != strlen(buf))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1e595a59e6 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
>>>>>>> cc0be293e5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cdd2375514 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
>>>>>>> 67e8f1691f (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1cabd030d3 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
>>>>>>> 460fa595c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b339c662ab (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
>>>>>>> 7ed89f83a7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 99ec0a9e3c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
>>>>>>> cb77e7994f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f6808ee3d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
>>>>>>> ae1809f882 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67806956ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
>>>>>>> a3175e513d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
        if (write(fd, buf, strlen(buf)) != (ssize_t)strlen(buf))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dfb114d4e3 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f063811cb8 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5c0a5aef3c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 558d40de40 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
>>>>>>> 6f3e89dc82 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2940bcf2c1 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> 50a5313262 (r.horizon manual - fix typo (#2794))
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
