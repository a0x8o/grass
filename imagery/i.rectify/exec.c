/* CMD mode from Bob Covill 2001
 * exec.c --
 *
 * Loop through all files to be rectified and do the retification.
 * Handles things like support files.
 *
 * small fixes: MN
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <time.h>
#include <unistd.h>
#include <math.h>
#include "global.h"

int exec_rectify(struct Image_Group *group, int *ref_list, char *extension,
                 char *interp_method, int order)
{
    char *name;
    char *mapset;
    char *result;
    char *type = "raster";
    int n;
    struct Colors colr;
    struct Categories cats;
    struct History hist;
    int colr_ok, cats_ok;
    time_t start_time, rectify_time;

    Rast_set_output_window(&target_window);
    G_message("-----------------------------------------------");

    /* rectify each file */
    for (n = 0; n < group->ref.nfiles; n++) {
        if (!ref_list[n])
            continue;

        name = group->ref.file[n].name;
        mapset = group->ref.file[n].mapset;

        /* generate out name, add extension to output */
        result =
            G_malloc(strlen(group->ref.file[n].name) + strlen(extension) + 1);
        strcpy(result, group->ref.file[n].name);
        strcat(result, extension);

        select_current_env();

        cats_ok = Rast_read_cats(name, mapset, &cats) >= 0;
        colr_ok = Rast_read_colors(name, mapset, &colr) > 0;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        /* Initialze History */
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
        /* Initialize History */
=======
        /* Initialze History */
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
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        /* Initialze History */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
        if (Rast_read_history(name, mapset, &hist) < 0)
            Rast_short_history(result, type, &hist);

        time(&start_time);

        if (rectify(group, name, mapset, result, order, interp_method)) {
            select_target_env();

            if (cats_ok) {
                Rast_write_cats(result, &cats);
                Rast_free_cats(&cats);
            }
            if (colr_ok) {
                Rast_write_colors(result, G_mapset(), &colr);
                Rast_free_colors(&colr);
            }
            /* Write out History */
            Rast_command_history(&hist);
            Rast_write_history(result, &hist);

            select_current_env();
            time(&rectify_time);
            report(rectify_time - start_time, 1);
        }
        else
            report(0, 0);

        G_free(result);
    }

    return 0;
}
