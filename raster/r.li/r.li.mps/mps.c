/****************************************************************************
 *
 * MODULE:       r.li.patchnum
 * AUTHOR(S):    Serena Pallecchi (original contributor)
 *                student of Computer Science University of Pisa (Italy)
 *               Commission from Faunalia Pontedera (PI) www.faunalia.it
 *               Rewrite: Markus Metz
 *               Patch identification: Michael Shapiro - CERL
 *
 * PURPOSE:      calculates mean patch size index
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
#include "../r.li.daemon/GenericCell.h"

/* template is patchnum */

/* cell count and type of each patch */
struct pst {
    long count;
    generic_cell type;
};

rli_func meanPatchSize;
int calculate(int fd, struct area_entry *ad, double *result);
int calculateD(int fd, struct area_entry *ad, double *result);
int calculateF(int fd, struct area_entry *ad, double *result);

int main(int argc, char *argv[])
{
    struct Option *raster, *conf, *output;
    struct GModule *module;

    G_gisinit(argv[0]);
    module = G_define_module();
    module->description = _("Calculates mean patch size index on a raster map, "
                            "using a 4 neighbour algorithm");
    G_add_keyword(_("raster"));
    G_add_keyword(_("landscape structure analysis"));
    G_add_keyword(_("patch index"));

    /* define options */

    raster = G_define_standard_option(G_OPT_R_INPUT);

    conf = G_define_standard_option(G_OPT_F_INPUT);
    conf->key = "config";
    conf->description = _("Configuration file");
    conf->required = YES;

    output = G_define_standard_option(G_OPT_R_OUTPUT);

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    return calculateIndex(conf->answer, meanPatchSize, NULL, raster->answer,
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
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
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
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
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
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
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
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
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
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
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
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
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
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
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
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
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
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
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
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
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
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
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
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
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
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
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
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
=======
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
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
int meanPatchSize(int fd, char **par UNUSED, struct area_entry *ad,
                  double *result)
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
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
int meanPatchSize(int fd, char **par, struct area_entry *ad, double *result)
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
    CELL *buf, *buf_sup, *buf_null;
    CELL corrCell, precCell, supCell;
    long npatch, area;
    long pid, old_pid, new_pid, *pid_corr, *pid_sup, *ltmp;
    struct pst *pst;
    long nalloc, incr;
    int i, j, k;
    int connected;
    int mask_fd, *mask_buf, *mask_sup, *mask_tmp, masked;
    struct Cell_head hd;

    Rast_get_window(&hd);

    buf_null = Rast_allocate_c_buf();
    Rast_set_c_null_value(buf_null, Rast_window_cols());
    buf_sup = buf_null;

    /* initialize patch ids */
    pid_corr = G_malloc(ad->cl * sizeof(long));
    pid_sup = G_malloc(ad->cl * sizeof(long));

    for (j = 0; j < ad->cl; j++) {
        pid_corr[j] = 0;
        pid_sup[j] = 0;
    }

    /* open mask if needed */
    mask_fd = -1;
    mask_buf = mask_sup = NULL;
    masked = FALSE;
    if (ad->mask == 1) {
        if ((mask_fd = open(ad->mask_name, O_RDONLY, 0755)) < 0)
            return RLI_ERRORE;
        mask_buf = G_malloc(ad->cl * sizeof(int));
        if (mask_buf == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        mask_sup = G_malloc(ad->cl * sizeof(int));
        if (mask_sup == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        for (j = 0; j < ad->cl; j++)
            mask_buf[j] = 0;

        masked = TRUE;
    }

    /* calculate number of patches */
    npatch = 0;
    area = 0;
    pid = 0;

    /* patch size and type */
    incr = 1024;
    if (incr > ad->rl)
        incr = ad->rl;
    if (incr > ad->cl)
        incr = ad->cl;
    if (incr < 2)
        incr = 2;
    nalloc = incr;
    pst = G_malloc(nalloc * sizeof(struct pst));
    for (k = 0; k < nalloc; k++) {
        pst[k].count = 0;
    }

    for (i = 0; i < ad->rl; i++) {
        buf = RLI_get_cell_raster_row(fd, i + ad->y, ad);
        if (i > 0) {
            buf_sup = RLI_get_cell_raster_row(fd, i - 1 + ad->y, ad);
        }

        if (masked) {
            mask_tmp = mask_sup;
            mask_sup = mask_buf;
            mask_buf = mask_tmp;
            if (read(mask_fd, mask_buf, (ad->cl * sizeof(int))) < 0)
                return 0;
        }

        ltmp = pid_sup;
        pid_sup = pid_corr;
        pid_corr = ltmp;

        Rast_set_c_null_value(&precCell, 1);

        connected = 0;
        for (j = 0; j < ad->cl; j++) {
            pid_corr[j] = 0;

            corrCell = buf[j + ad->x];
            if (masked && (mask_buf[j] == 0)) {
                Rast_set_c_null_value(&corrCell, 1);
            }

            if (Rast_is_c_null_value(&corrCell)) {
                connected = 0;
                precCell = corrCell;
                continue;
            }

            area++;

            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_c_null_value(&supCell, 1);
            }

            if (!Rast_is_c_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j] = pid_corr[j - 1];
                connected = 1;
                pst[pid_corr[j]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_c_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j] != pid_sup[j]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

                    old_pid = pid_corr[j];
                    new_pid = pid_sup[j];
                    pid_corr[j] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k] == old_pid)
                                pid_corr[k] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k] == old_pid)
                                pid_sup[k] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

                        if (old_pid == pid)
                            pid--;
                    }
                    else {
                        pst[new_pid].count++;
                    }
                }
                connected = 1;
            }

            if (!connected) {
                /* start new patch */
                npatch++;
                pid++;
                pid_corr[j] = pid;

                if (pid >= nalloc) {
                    pst = (struct pst *)G_realloc(pst, (pid + incr) *
                                                           sizeof(struct pst));

                    for (k = nalloc; k < pid + incr; k++)
                        pst[k].count = 0;

                    nalloc = pid + incr;
                }

                pst[pid].count = 1;
                pst[pid].type.t = CELL_TYPE;
                pst[pid].type.val.c = corrCell;
            }
            precCell = corrCell;
        }
    }

    if (npatch > 0) {
        double EW_DIST1, EW_DIST2, NS_DIST1, NS_DIST2;
        double area_units;

        /* calculate distance */
        G_begin_distance_calculations();
        /* EW Dist at North edge */
        EW_DIST1 = G_distance(hd.east, hd.north, hd.west, hd.north);
        /* EW Dist at South Edge */
        EW_DIST2 = G_distance(hd.east, hd.south, hd.west, hd.south);
        /* NS Dist at East edge */
        NS_DIST1 = G_distance(hd.east, hd.north, hd.east, hd.south);
        /* NS Dist at West edge */
        NS_DIST2 = G_distance(hd.west, hd.north, hd.west, hd.south);

        area_units = (((EW_DIST1 + EW_DIST2) / 2) / hd.cols) *
                     (((NS_DIST1 + NS_DIST2) / 2) / hd.rows) * area;

        *result = area_units / (npatch * 10000);
    }
    else {
        *result = 0;
    }

    if (masked) {
        close(mask_fd);
        G_free(mask_buf);
        G_free(mask_sup);
    }
    G_free(buf_null);
    G_free(pid_corr);
    G_free(pid_sup);
    G_free(pst);

    return RLI_OK;
}

int calculateD(int fd, struct area_entry *ad, double *result)
{
    DCELL *buf, *buf_sup, *buf_null;
    DCELL corrCell, precCell, supCell;
    long npatch, area;
    long pid, old_pid, new_pid, *pid_corr, *pid_sup, *ltmp;
    struct pst *pst;
    long nalloc, incr;
    int i, j, k;
    int connected;
    int mask_fd, *mask_buf, *mask_sup, *mask_tmp, masked;
    struct Cell_head hd;

    Rast_get_window(&hd);

    buf_null = Rast_allocate_d_buf();
    Rast_set_d_null_value(buf_null, Rast_window_cols());
    buf_sup = buf_null;

    /* initialize patch ids */
    pid_corr = G_malloc(ad->cl * sizeof(long));
    pid_sup = G_malloc(ad->cl * sizeof(long));

    for (j = 0; j < ad->cl; j++) {
        pid_corr[j] = 0;
        pid_sup[j] = 0;
    }

    /* open mask if needed */
    mask_fd = -1;
    mask_buf = mask_sup = NULL;
    masked = FALSE;
    if (ad->mask == 1) {
        if ((mask_fd = open(ad->mask_name, O_RDONLY, 0755)) < 0)
            return RLI_ERRORE;
        mask_buf = G_malloc(ad->cl * sizeof(int));
        if (mask_buf == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        mask_sup = G_malloc(ad->cl * sizeof(int));
        if (mask_sup == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        for (j = 0; j < ad->cl; j++)
            mask_buf[j] = 0;

        masked = TRUE;
    }

    /* calculate number of patches */
    npatch = 0;
    area = 0;
    pid = 0;

    /* patch size and type */
    incr = 1024;
    if (incr > ad->rl)
        incr = ad->rl;
    if (incr > ad->cl)
        incr = ad->cl;
    if (incr < 2)
        incr = 2;
    nalloc = incr;
    pst = G_malloc(nalloc * sizeof(struct pst));
    for (k = 0; k < nalloc; k++) {
        pst[k].count = 0;
    }

    for (i = 0; i < ad->rl; i++) {
        buf = RLI_get_dcell_raster_row(fd, i + ad->y, ad);
        if (i > 0) {
            buf_sup = RLI_get_dcell_raster_row(fd, i - 1 + ad->y, ad);
        }

        if (masked) {
            mask_tmp = mask_sup;
            mask_sup = mask_buf;
            mask_buf = mask_tmp;
            if (read(mask_fd, mask_buf, (ad->cl * sizeof(int))) < 0)
                return 0;
        }

        ltmp = pid_sup;
        pid_sup = pid_corr;
        pid_corr = ltmp;

        Rast_set_d_null_value(&precCell, 1);

        connected = 0;
        for (j = 0; j < ad->cl; j++) {
            pid_corr[j] = 0;

            corrCell = buf[j + ad->x];
            if (masked && (mask_buf[j] == 0)) {
                Rast_set_d_null_value(&corrCell, 1);
            }

            if (Rast_is_d_null_value(&corrCell)) {
                connected = 0;
                precCell = corrCell;
                continue;
            }

            area++;

            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_d_null_value(&supCell, 1);
            }

            if (!Rast_is_d_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j] = pid_corr[j - 1];
                connected = 1;
                pst[pid_corr[j]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_d_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j] != pid_sup[j]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

                    old_pid = pid_corr[j];
                    new_pid = pid_sup[j];
                    pid_corr[j] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k] == old_pid)
                                pid_corr[k] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k] == old_pid)
                                pid_sup[k] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

                        if (old_pid == pid)
                            pid--;
                    }
                    else {
                        pst[new_pid].count++;
                    }
                }
                connected = 1;
            }

            if (!connected) {
                /* start new patch */
                npatch++;
                pid++;
                pid_corr[j] = pid;

                if (pid >= nalloc) {
                    pst = (struct pst *)G_realloc(pst, (pid + incr) *
                                                           sizeof(struct pst));

                    for (k = nalloc; k < pid + incr; k++)
                        pst[k].count = 0;

                    nalloc = pid + incr;
                }

                pst[pid].count = 1;
                pst[pid].type.t = CELL_TYPE;
                pst[pid].type.val.c = corrCell;
            }
            precCell = corrCell;
        }
    }

    if (npatch > 0) {
        double EW_DIST1, EW_DIST2, NS_DIST1, NS_DIST2;
        double area_units;

        /* calculate distance */
        G_begin_distance_calculations();
        /* EW Dist at North edge */
        EW_DIST1 = G_distance(hd.east, hd.north, hd.west, hd.north);
        /* EW Dist at South Edge */
        EW_DIST2 = G_distance(hd.east, hd.south, hd.west, hd.south);
        /* NS Dist at East edge */
        NS_DIST1 = G_distance(hd.east, hd.north, hd.east, hd.south);
        /* NS Dist at West edge */
        NS_DIST2 = G_distance(hd.west, hd.north, hd.west, hd.south);

        area_units = (((EW_DIST1 + EW_DIST2) / 2) / hd.cols) *
                     (((NS_DIST1 + NS_DIST2) / 2) / hd.rows) * area;

        *result = area_units / (npatch * 10000);
    }
    else {
        *result = 0;
    }

    if (masked) {
        close(mask_fd);
        G_free(mask_buf);
        G_free(mask_sup);
    }
    G_free(buf_null);
    G_free(pid_corr);
    G_free(pid_sup);
    G_free(pst);

    return RLI_OK;
}

int calculateF(int fd, struct area_entry *ad, double *result)
{
    FCELL *buf, *buf_sup, *buf_null;
    FCELL corrCell, precCell, supCell;
    long npatch, area;
    long pid, old_pid, new_pid, *pid_corr, *pid_sup, *ltmp;
    struct pst *pst;
    long nalloc, incr;
    int i, j, k;
    int connected;
    int mask_fd, *mask_buf, *mask_sup, *mask_tmp, masked;
    struct Cell_head hd;

    Rast_get_window(&hd);

    buf_null = Rast_allocate_f_buf();
    Rast_set_f_null_value(buf_null, Rast_window_cols());
    buf_sup = buf_null;

    /* initialize patch ids */
    pid_corr = G_malloc(ad->cl * sizeof(long));
    pid_sup = G_malloc(ad->cl * sizeof(long));

    for (j = 0; j < ad->cl; j++) {
        pid_corr[j] = 0;
        pid_sup[j] = 0;
    }

    /* open mask if needed */
    mask_fd = -1;
    mask_buf = mask_sup = NULL;
    masked = FALSE;
    if (ad->mask == 1) {
        if ((mask_fd = open(ad->mask_name, O_RDONLY, 0755)) < 0)
            return RLI_ERRORE;
        mask_buf = G_malloc(ad->cl * sizeof(int));
        if (mask_buf == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        mask_sup = G_malloc(ad->cl * sizeof(int));
        if (mask_sup == NULL) {
            G_fatal_error("malloc mask_buf failed");
            return RLI_ERRORE;
        }
        for (j = 0; j < ad->cl; j++)
            mask_buf[j] = 0;

        masked = TRUE;
    }

    /* calculate number of patches */
    npatch = 0;
    area = 0;
    pid = 0;

    /* patch size and type */
    incr = 1024;
    if (incr > ad->rl)
        incr = ad->rl;
    if (incr > ad->cl)
        incr = ad->cl;
    if (incr < 2)
        incr = 2;
    nalloc = incr;
    pst = G_malloc(nalloc * sizeof(struct pst));
    for (k = 0; k < nalloc; k++) {
        pst[k].count = 0;
    }

    for (i = 0; i < ad->rl; i++) {
        buf = RLI_get_fcell_raster_row(fd, i + ad->y, ad);
        if (i > 0) {
            buf_sup = RLI_get_fcell_raster_row(fd, i - 1 + ad->y, ad);
        }

        if (masked) {
            mask_tmp = mask_sup;
            mask_sup = mask_buf;
            mask_buf = mask_tmp;
            if (read(mask_fd, mask_buf, (ad->cl * sizeof(int))) < 0)
                return 0;
        }

        ltmp = pid_sup;
        pid_sup = pid_corr;
        pid_corr = ltmp;

        Rast_set_f_null_value(&precCell, 1);

        connected = 0;
        for (j = 0; j < ad->cl; j++) {
            pid_corr[j] = 0;

            corrCell = buf[j + ad->x];
            if (masked && (mask_buf[j] == 0)) {
                Rast_set_f_null_value(&corrCell, 1);
            }

            if (Rast_is_f_null_value(&corrCell)) {
                connected = 0;
                precCell = corrCell;
                continue;
            }

            area++;

            supCell = buf_sup[j + ad->x];
            if (masked && (mask_sup[j] == 0)) {
                Rast_set_f_null_value(&supCell, 1);
            }

            if (!Rast_is_f_null_value(&precCell) && corrCell == precCell) {
                pid_corr[j] = pid_corr[j - 1];
                connected = 1;
                pst[pid_corr[j]].count++;
            }
            else {
                connected = 0;
            }

            if (!Rast_is_f_null_value(&supCell) && corrCell == supCell) {

                if (pid_corr[j] != pid_sup[j]) {
                    /* connect or merge */
                    /* after r.clump */
                    if (connected) {
                        npatch--;

                        if (npatch == 0) {
                            G_fatal_error("npatch == 0 at row %d, col %d", i,
                                          j);
                        }
                    }

                    old_pid = pid_corr[j];
                    new_pid = pid_sup[j];
                    pid_corr[j] = new_pid;
                    if (old_pid > 0) {
                        /* merge */
                        /* update left side of the current row */
                        for (k = 0; k < j; k++) {
                            if (pid_corr[k] == old_pid)
                                pid_corr[k] = new_pid;
                        }
                        /* update right side of the previous row */
                        for (k = j + 1; k < ad->cl; k++) {
                            if (pid_sup[k] == old_pid)
                                pid_sup[k] = new_pid;
                        }
                        pst[new_pid].count += pst[old_pid].count;
                        pst[old_pid].count = 0;

                        if (old_pid == pid)
                            pid--;
                    }
                    else {
                        pst[new_pid].count++;
                    }
                }
                connected = 1;
            }

            if (!connected) {
                /* start new patch */
                npatch++;
                pid++;
                pid_corr[j] = pid;

                if (pid >= nalloc) {
                    pst = (struct pst *)G_realloc(pst, (pid + incr) *
                                                           sizeof(struct pst));

                    for (k = nalloc; k < pid + incr; k++)
                        pst[k].count = 0;

                    nalloc = pid + incr;
                }

                pst[pid].count = 1;
                pst[pid].type.t = CELL_TYPE;
                pst[pid].type.val.c = corrCell;
            }
            precCell = corrCell;
        }
    }

    if (npatch > 0) {
        double EW_DIST1, EW_DIST2, NS_DIST1, NS_DIST2;
        double area_units;

        /* calculate distance */
        G_begin_distance_calculations();
        /* EW Dist at North edge */
        EW_DIST1 = G_distance(hd.east, hd.north, hd.west, hd.north);
        /* EW Dist at South Edge */
        EW_DIST2 = G_distance(hd.east, hd.south, hd.west, hd.south);
        /* NS Dist at East edge */
        NS_DIST1 = G_distance(hd.east, hd.north, hd.east, hd.south);
        /* NS Dist at West edge */
        NS_DIST2 = G_distance(hd.west, hd.north, hd.west, hd.south);

        area_units = (((EW_DIST1 + EW_DIST2) / 2) / hd.cols) *
                     (((NS_DIST1 + NS_DIST2) / 2) / hd.rows) * area;

        *result = area_units / (npatch * 10000);
    }
    else {
        *result = 0;
    }

    if (masked) {
        close(mask_fd);
        G_free(mask_buf);
        G_free(mask_sup);
    }
    G_free(buf_null);
    G_free(pid_corr);
    G_free(pid_sup);
    G_free(pst);

    return RLI_OK;
}
