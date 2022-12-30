/****************************************************************************
 *
 * MODULE:       r.li.simpson
 * AUTHOR(S):    Serena Pallecchi (original contributor)
 *                student of Computer Science University of Pisa (Italy)
 *               Commission from Faunalia Pontedera (PI) www.faunalia.it
 *               Rewrite: Markus Metz
 *
 * PURPOSE:      calculates Simpson's diversity index
 * COPYRIGHT:    (C) 2007-2014 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <stdlib.h>
#include <fcntl.h>
#include <math.h>

#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>

#include "../r.li.daemon/daemon.h"
#include "../r.li.daemon/avlDefs.h"
#include "../r.li.daemon/avl.h"

/* template is shannon */

rli_func simpson;
int calculate(int fd, struct area_entry *ad, double *result);
int calculateD(int fd, struct area_entry *ad, double *result);
int calculateF(int fd, struct area_entry *ad, double *result);

int main(int argc, char *argv[])
{
    struct Option *raster, *conf, *output;
    struct GModule *module;

    G_gisinit(argv[0]);
    module = G_define_module();
    module->description =
        _("Calculates Simpson's diversity index on a raster map");
    G_add_keyword(_("raster"));
    G_add_keyword(_("landscape structure analysis"));
    G_add_keyword(_("diversity index"));

    /* define options */

    raster = G_define_standard_option(G_OPT_R_INPUT);

    conf = G_define_standard_option(G_OPT_F_INPUT);
    conf->key = "config";
    conf->description = _("Configuration file");
    conf->required = YES;

    output = G_define_standard_option(G_OPT_R_OUTPUT);

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    return calculateIndex(conf->answer, simpson, NULL, raster->answer,
                          output->answer);
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
=======
>>>>>>> osgeo-main
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
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
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int simpson(int fd, char **par UNUSED, struct area_entry *ad, double *result)
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
int simpson(int fd, char **par, struct area_entry *ad, double *result)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
{
    int ris = RLI_OK;
    double indice = 0;

    switch (ad->data_type) {
    case CELL_TYPE: {
        ris = calculate(fd, ad, &indice);
        break;
    }
    case DCELL_TYPE: {
        ris = calculateD(fd, ad, &indice);
        break;
    }
    case FCELL_TYPE: {
        ris = calculateF(fd, ad, &indice);
        break;
    }
    default: {
        G_fatal_error("data type unknown");
        return RLI_ERRORE;
    }
    }

    if (ris != RLI_OK) {
        return RLI_ERRORE;
    }

    *result = indice;

    return RLI_OK;
}

int calculate(int fd, struct area_entry *ad, double *result)
{
    CELL *buf;
    CELL corrCell;
    CELL precCell;

    int i, j;
    int mask_fd = -1, *mask_buf = NULL;
    int ris = 0;
    int masked = FALSE;

    long m = 0;
    long tot = 0;
    long zero = 0;
    long totCorr = 1;

    long area = 0;

    avl_tree albero = NULL;
    AVL_table array;
    generic_cell uc;

    uc.t = CELL_TYPE;

    /* open mask if needed */
    if (ad->mask == 1) {
        if ((mask_fd = open(ad->mask_name, O_RDONLY, 0755)) < 0)
            return RLI_ERRORE;
        mask_buf = G_malloc(ad->cl * sizeof(int));
        if (mask_buf == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        masked = TRUE;
    }

    Rast_set_c_null_value(&precCell, 1);
    for (j = 0; j < ad->rl; j++) { /* for each row */
        if (masked) {
            if (read(mask_fd, mask_buf, (ad->cl * sizeof(int))) < 0) {
                G_fatal_error("mask read failed");
                return RLI_ERRORE;
            }
        }

        buf = RLI_get_cell_raster_row(fd, j + ad->y, ad);

        for (i = 0; i < ad->cl; i++) { /* for each cell in the row */
            corrCell = buf[i + ad->x];

            if ((masked) && (mask_buf[i] == 0)) {
                Rast_set_c_null_value(&corrCell, 1);
            }

            if (!(Rast_is_null_value(&corrCell, uc.t))) {
                /* total patch area */
                area++;
            }

            if (!(Rast_is_null_value(&precCell, uc.t)) &&
                corrCell == precCell) {

                totCorr++;
            }
            else if (!(Rast_is_null_value(&precCell, uc.t)) &&
                     corrCell != precCell) {

                /* add precCell to search tree */
                if (albero == NULL) {
                    uc.val.c = precCell;
                    albero = avl_make(uc, totCorr);
                    if (albero == NULL) {
                        G_fatal_error("avl_make error");
                        return RLI_ERRORE;
                    }
                    m++;
                }
                else {
                    uc.val.c = precCell;
                    ris = avl_add(&albero, uc, totCorr);
                    switch (ris) {
                    case AVL_ERR: {
                        G_fatal_error("avl_add error");
                        return RLI_ERRORE;
                    }
                    case AVL_ADD: {
                        m++;
                        break;
                    }
                    case AVL_PRES: {
                        break;
                    }
                    default: {
                        G_fatal_error("avl_make unknown error");
                        return RLI_ERRORE;
                    }
                    }
                }
                totCorr = 1;
            } /* endif not equal cells */
            precCell = corrCell;
        }
    }

    /* last closing */
    if (area > 0 && !(Rast_is_null_value(&precCell, uc.t))) {
        if (albero == NULL) {
            uc.val.c = precCell;
            albero = avl_make(uc, totCorr);
            if (albero == NULL) {
                G_fatal_error("avl_make error");
                return RLI_ERRORE;
            }
            m++;
        }
        else {
            uc.val.c = precCell;
            ris = avl_add(&albero, uc, totCorr);
            switch (ris) {
            case AVL_ERR: {
                G_fatal_error("avl_add error");
                return RLI_ERRORE;
            }
            case AVL_ADD: {
                m++;
                break;
            }
            case AVL_PRES: {
                break;
            }
            default: {
                G_fatal_error("avl_add unknown error");
                return RLI_ERRORE;
            }
            }
        }
    }

    if (area > 0) {
        double t;
        double p;
        double simpson;

        array = G_malloc(m * sizeof(AVL_tableRow));
        if (array == NULL) {
            G_fatal_error("malloc array failed");
            return RLI_ERRORE;
        }
        tot = avl_to_array(albero, zero, array);
        if (tot != m) {
            G_warning(
                "avl_to_array unexpected value. the result could be wrong");
            return RLI_ERRORE;
        }

        /* calculate simpson */
        simpson = 0;
        for (i = 0; i < m; i++) {
            t = (double)(array[i].tot);
            p = t / area;
            simpson += (p * p);
        }
        G_free(array);

        *result = 1 - simpson;
    }
    else
        Rast_set_d_null_value(result, 1);

    avl_destroy(albero);
    if (masked) {
        close(mask_fd);
        G_free(mask_buf);
    }

    return RLI_OK;
}

int calculateD(int fd, struct area_entry *ad, double *result)
{
    DCELL *buf;
    DCELL corrCell;
    DCELL precCell;

    int i, j;
    int mask_fd = -1, *mask_buf = NULL;
    int ris = 0;
    int masked = FALSE;

    long m = 0;
    long tot = 0;
    long zero = 0;
    long totCorr = 1;

    long area = 0;

    avl_tree albero = NULL;
    AVL_table array;
    generic_cell uc;

    uc.t = DCELL_TYPE;

    /* open mask if needed */
    if (ad->mask == 1) {
        if ((mask_fd = open(ad->mask_name, O_RDONLY, 0755)) < 0)
            return RLI_ERRORE;
        mask_buf = G_malloc(ad->cl * sizeof(int));
        if (mask_buf == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        masked = TRUE;
    }

    Rast_set_d_null_value(&precCell, 1);
    for (j = 0; j < ad->rl; j++) { /* for each row */
        if (masked) {
            if (read(mask_fd, mask_buf, (ad->cl * sizeof(int))) < 0) {
                G_fatal_error("mask read failed");
                return RLI_ERRORE;
            }
        }

        buf = RLI_get_dcell_raster_row(fd, j + ad->y, ad);

        for (i = 0; i < ad->cl; i++) { /* for each cell in the row */
            corrCell = buf[i + ad->x];

            if ((masked) && (mask_buf[i] == 0)) {
                Rast_set_d_null_value(&corrCell, 1);
            }

            if (!(Rast_is_null_value(&corrCell, uc.t))) {
                /* total patch area */
                area++;
            }

            if (!(Rast_is_null_value(&precCell, uc.t)) &&
                corrCell == precCell) {

                totCorr++;
            }
            else if (!(Rast_is_null_value(&precCell, uc.t)) &&
                     corrCell != precCell) {

                /* add precCell to search tree */
                if (albero == NULL) {
                    uc.val.dc = precCell;
                    albero = avl_make(uc, totCorr);
                    if (albero == NULL) {
                        G_fatal_error("avl_make error");
                        return RLI_ERRORE;
                    }
                    m++;
                }
                else {
                    uc.val.dc = precCell;
                    ris = avl_add(&albero, uc, totCorr);
                    switch (ris) {
                    case AVL_ERR: {
                        G_fatal_error("avl_add error");
                        return RLI_ERRORE;
                    }
                    case AVL_ADD: {
                        m++;
                        break;
                    }
                    case AVL_PRES: {
                        break;
                    }
                    default: {
                        G_fatal_error("avl_make unknown error");
                        return RLI_ERRORE;
                    }
                    }
                }
                totCorr = 1;
            } /* endif not equal cells */
            precCell = corrCell;
        }
    }

    /* last closing */
    if (area > 0 && !(Rast_is_null_value(&precCell, uc.t))) {
        if (albero == NULL) {
            uc.val.dc = precCell;
            albero = avl_make(uc, totCorr);
            if (albero == NULL) {
                G_fatal_error("avl_make error");
                return RLI_ERRORE;
            }
            m++;
        }
        else {
            uc.val.dc = precCell;
            ris = avl_add(&albero, uc, totCorr);
            switch (ris) {
            case AVL_ERR: {
                G_fatal_error("avl_add error");
                return RLI_ERRORE;
            }
            case AVL_ADD: {
                m++;
                break;
            }
            case AVL_PRES: {
                break;
            }
            default: {
                G_fatal_error("avl_add unknown error");
                return RLI_ERRORE;
            }
            }
        }
    }

    if (area > 0) {
        double t;
        double p;
        double simpson;

        array = G_malloc(m * sizeof(AVL_tableRow));
        if (array == NULL) {
            G_fatal_error("malloc array failed");
            return RLI_ERRORE;
        }
        tot = avl_to_array(albero, zero, array);
        if (tot != m) {
            G_warning(
                "avl_to_array unexpected value. the result could be wrong");
            return RLI_ERRORE;
        }

        /* calculate simpson */
        simpson = 0;
        for (i = 0; i < m; i++) {
            t = (double)(array[i].tot);
            p = t / area;
            simpson += (p * p);
        }
        G_free(array);

        *result = 1 - simpson;
    }
    else
        Rast_set_d_null_value(result, 1);

    avl_destroy(albero);
    if (masked) {
        close(mask_fd);
        G_free(mask_buf);
    }

    return RLI_OK;
}

int calculateF(int fd, struct area_entry *ad, double *result)
{
    FCELL *buf;
    FCELL corrCell;
    FCELL precCell;

    int i, j;
    int mask_fd = -1, *mask_buf = NULL;
    int ris = 0;
    int masked = FALSE;

    long m = 0;
    long tot = 0;
    long zero = 0;
    long totCorr = 1;

    long area = 0;

    avl_tree albero = NULL;
    AVL_table array;
    generic_cell uc;

    uc.t = FCELL_TYPE;

    /* open mask if needed */
    if (ad->mask == 1) {
        if ((mask_fd = open(ad->mask_name, O_RDONLY, 0755)) < 0)
            return RLI_ERRORE;
        mask_buf = G_malloc(ad->cl * sizeof(int));
        if (mask_buf == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        masked = TRUE;
    }

    Rast_set_f_null_value(&precCell, 1);
    for (j = 0; j < ad->rl; j++) { /* for each row */
        if (masked) {
            if (read(mask_fd, mask_buf, (ad->cl * sizeof(int))) < 0) {
                G_fatal_error("mask read failed");
                return RLI_ERRORE;
            }
        }

        buf = RLI_get_fcell_raster_row(fd, j + ad->y, ad);

        for (i = 0; i < ad->cl; i++) { /* for each cell in the row */
            corrCell = buf[i + ad->x];

            if ((masked) && (mask_buf[i] == 0)) {
                Rast_set_f_null_value(&corrCell, 1);
            }

            if (!(Rast_is_null_value(&corrCell, uc.t))) {
                /* total patch area */
                area++;
            }

            if (!(Rast_is_null_value(&precCell, uc.t)) &&
                corrCell == precCell) {

                totCorr++;
            }
            else if (!(Rast_is_null_value(&precCell, uc.t)) &&
                     corrCell != precCell) {

                /* add precCell to search tree */
                if (albero == NULL) {
                    uc.val.fc = precCell;
                    albero = avl_make(uc, totCorr);
                    if (albero == NULL) {
                        G_fatal_error("avl_make error");
                        return RLI_ERRORE;
                    }
                    m++;
                }
                else {
                    uc.val.fc = precCell;
                    ris = avl_add(&albero, uc, totCorr);
                    switch (ris) {
                    case AVL_ERR: {
                        G_fatal_error("avl_add error");
                        return RLI_ERRORE;
                    }
                    case AVL_ADD: {
                        m++;
                        break;
                    }
                    case AVL_PRES: {
                        break;
                    }
                    default: {
                        G_fatal_error("avl_make unknown error");
                        return RLI_ERRORE;
                    }
                    }
                }
                totCorr = 1;
            } /* endif not equal cells */
            precCell = corrCell;
        }
    }

    /* last closing */
    if (area > 0 && !(Rast_is_null_value(&precCell, uc.t))) {
        if (albero == NULL) {
            uc.val.fc = precCell;
            albero = avl_make(uc, totCorr);
            if (albero == NULL) {
                G_fatal_error("avl_make error");
                return RLI_ERRORE;
            }
            m++;
        }
        else {
            uc.val.fc = precCell;
            ris = avl_add(&albero, uc, totCorr);
            switch (ris) {
            case AVL_ERR: {
                G_fatal_error("avl_add error");
                return RLI_ERRORE;
            }
            case AVL_ADD: {
                m++;
                break;
            }
            case AVL_PRES: {
                break;
            }
            default: {
                G_fatal_error("avl_add unknown error");
                return RLI_ERRORE;
            }
            }
        }
    }

    if (area > 0) {
        double t;
        double p;
        double simpson;

        array = G_malloc(m * sizeof(AVL_tableRow));
        if (array == NULL) {
            G_fatal_error("malloc array failed");
            return RLI_ERRORE;
        }
        tot = avl_to_array(albero, zero, array);
        if (tot != m) {
            G_warning(
                "avl_to_array unexpected value. the result could be wrong");
            return RLI_ERRORE;
        }

        /* calculate simpson */
        simpson = 0;
        for (i = 0; i < m; i++) {
            t = (double)(array[i].tot);
            p = t / area;
            simpson += (p * p);
        }
        G_free(array);

        *result = 1 - simpson;
    }
    else
        Rast_set_d_null_value(result, 1);

    avl_destroy(albero);
    if (masked) {
        close(mask_fd);
        G_free(mask_buf);
    }

    return RLI_OK;
}
