#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <grass/glocale.h>
#include "global.h"

int parse_command_line(int argc, char *argv[])
{
    int i;
    char *desc;
    struct {
        struct Option *cell;
        struct Option *units;
        struct Option *pl; /* page length */
        struct Option *pw; /* page width */
        struct Option *outfile;
        struct Option *nv;
        struct Option *nsteps;
        struct Option *sort;
        struct Option *format;
    } parms;
    struct {
        struct Flag *f;
        struct Flag *m;
        struct Flag *h;
        struct Flag *q;
        struct Flag *e;
        struct Flag *n;
        struct Flag *N;
        struct Flag *i; /* use quant rules for fp map,
                           i.e. read it as int */
        struct Flag *C; /*  report for fp ranges in Cats file
                           (fp maps only) */
    } flags;

    parms.cell = G_define_standard_option(G_OPT_R_MAPS);
    parms.cell->description = _("Name of raster map(s) to report on");

    parms.units = G_define_option();
    parms.units->key = "units";
    parms.units->type = TYPE_STRING;
    parms.units->required = NO;
    parms.units->multiple = YES;
    parms.units->description = _("Units to report");
    desc = NULL;
    G_asprintf(&desc,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> dbc81233ab (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d4461869e8 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9c120ffe33 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> c01342bea9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b75a91e7a6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bfcc03842f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fcadc7e13f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d60d422dbe (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 7ec793d809 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a2ef6edc89 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a37726dc18 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f03e5ccef0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 44759847fe (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 8a7994d157 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2ee3ec7759 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a7a7080cfc (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 8dcc73d184 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 3ff45b1287 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2f250dd5e8 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a32e8a4fd1 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ebf514d546 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a8f007a736 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f1d253615b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ba68f04a85 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 735793be5b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d65864657f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 47ae4a1f0b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a7929f96f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f6796399ec (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a117ae3039 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 96919f4588 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd5e136394 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 0e12acb042 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14410d46fe (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 080da2a524 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 80a8eaeb2b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fe15d84827 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
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
=======
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3953b29f4d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f68b0fd740 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4e857df9d2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 9766eb6ce9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43b05ab727 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bcdce38fd1 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28ba50a5ea (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bf8e093a53 (r.report: add default units, change to full unit names (#1666))
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
=======
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
=======
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9c120ffe33 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 70b9875805 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c01342bea9 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b75a91e7a6 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a9170040dc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bfcc03842f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fcadc7e13f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> f3162d6aeb (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d60d422dbe (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 948e158f3d (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ec793d809 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> c7e767a1cc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a2ef6edc89 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 5f5ba2af03 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
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
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> edf7780032 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a37726dc18 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 07ae314ad5 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f03e5ccef0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 747ff50cd8 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 44759847fe (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ed995162de (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a7994d157 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dceb60f5b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ee3ec7759 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 6ac86966bf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a7a7080cfc (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 97a8b8e667 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8dcc73d184 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 57aae04049 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3ff45b1287 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1c84c0d40e (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2f250dd5e8 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 90f3380cbf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a32e8a4fd1 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 8cbe3dcd02 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 38ca4b8512 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 029e33e9f0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 910ce69f58 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bc87ec126b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a9b0c66c34 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3ddce5eb55 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f0ae57bd (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 4e857df9d2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 70b9875805 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9766eb6ce9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 43b05ab727 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a9170040dc (r.report: add default units, change to full unit names (#1666))
>>>>>>> bcdce38fd1 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 28ba50a5ea (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> f3162d6aeb (r.report: add default units, change to full unit names (#1666))
>>>>>>> bf8e093a53 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 24754e005d (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
>>>>>>> ebf514d546 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> c7e767a1cc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a8f007a736 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> d90c40bd96 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
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
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a78b7099e3 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
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
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f1d253615b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 07ae314ad5 (r.report: add default units, change to full unit names (#1666))
>>>>>>> ba68f04a85 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 747ff50cd8 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 735793be5b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ed995162de (r.report: add default units, change to full unit names (#1666))
>>>>>>> d65864657f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dceb60f5b (r.report: add default units, change to full unit names (#1666))
>>>>>>> 47ae4a1f0b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 0a7929f96f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 6ac86966bf (r.report: add default units, change to full unit names (#1666))
>>>>>>> f6796399ec (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a117ae3039 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 97a8b8e667 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 96919f4588 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
>>>>>>> bd5e136394 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 57aae04049 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 0e12acb042 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 14410d46fe (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1c84c0d40e (r.report: add default units, change to full unit names (#1666))
>>>>>>> 080da2a524 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 80a8eaeb2b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 90f3380cbf (r.report: add default units, change to full unit names (#1666))
>>>>>>> fe15d84827 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 6171565840 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
>>>>>>> a2a2cec695 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 910ce69f58 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 73ec075236 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 5ea900f7e5 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3ddce5eb55 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 637f8ada3d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
               "miles;%s;meters;%s;kilometers;%s;acres;%s;hectares;%s;cells;%s;"
               "percent;%s",
               _("area in square miles"), _("area in square meters"),
               _("area in square kilometers"), _("area in acres"),
               _("area in hectares"), _("number of cells"), _("percent cover"));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    parms.units->descriptions = desc;
    parms.units->options =
        "miles,meters,kilometers,acres,hectares,cells,percent";
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    parms.units->descriptions = desc;
    parms.units->options =
        "miles,meters,kilometers,acres,hectares,cells,percent";
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> osgeo-main
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> dbc81233ab (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> d4461869e8 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 9c120ffe33 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 70b9875805 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> c01342bea9 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> b75a91e7a6 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a9170040dc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bfcc03842f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> fcadc7e13f (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3162d6aeb (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> d60d422dbe (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
    parms.units->descriptions = desc;
    parms.units->options =
        "miles,meters,kilometers,acres,hectares,cells,percent";
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 948e158f3d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 7ec793d809 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> c7e767a1cc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a2ef6edc89 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 5f5ba2af03 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> edf7780032 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a37726dc18 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 07ae314ad5 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> f03e5ccef0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 747ff50cd8 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 44759847fe (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> ed995162de (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 8a7994d157 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 1dceb60f5b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2ee3ec7759 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 6ac86966bf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a7a7080cfc (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 97a8b8e667 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 8dcc73d184 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 57aae04049 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 3ff45b1287 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 1c84c0d40e (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2f250dd5e8 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 90f3380cbf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a32e8a4fd1 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 8cbe3dcd02 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 38ca4b8512 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 029e33e9f0 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 910ce69f58 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bc87ec126b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a9b0c66c34 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 3ddce5eb55 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 88f0ae57bd (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 3953b29f4d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> f68b0fd740 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 4e857df9d2 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 70b9875805 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 9766eb6ce9 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 43b05ab727 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a9170040dc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bcdce38fd1 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 28ba50a5ea (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3162d6aeb (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bf8e093a53 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
    parms.units->descriptions = desc;
    parms.units->options =
        "miles,meters,kilometers,acres,hectares,cells,percent";
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 24754e005d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> ebf514d546 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> c7e767a1cc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a8f007a736 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> d90c40bd96 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a78b7099e3 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> f1d253615b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 07ae314ad5 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> ba68f04a85 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 747ff50cd8 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 735793be5b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> ed995162de (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> d65864657f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 1dceb60f5b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 47ae4a1f0b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 0a7929f96f (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 6ac86966bf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> f6796399ec (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a117ae3039 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 97a8b8e667 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 96919f4588 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bd5e136394 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 57aae04049 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 0e12acb042 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 14410d46fe (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 1c84c0d40e (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 080da2a524 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 80a8eaeb2b (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 90f3380cbf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> fe15d84827 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 6171565840 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a2a2cec695 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 910ce69f58 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 73ec075236 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 5ea900f7e5 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 3ddce5eb55 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 637f8ada3d (r.report: add default units, change to full unit names (#1666))
	       "miles;%s;meters;%s;kilometers;%s;acres;%s;hectares;%s;cells;%s;percent;%s",
	       _("area in square miles"),
	       _("area in square meters"),
	       _("area in square kilometers"),
	       _("area in acres"),
	       _("area in hectares"),
	       _("number of cells"),
	       _("percent cover"));
    parms.units->descriptions = desc;
    parms.units->options = "miles,meters,kilometers,acres,hectares,cells,percent";
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2a2cec695 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 73ec075236 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 5ea900f7e5 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 637f8ada3d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 6171565840 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fe15d84827 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 80a8eaeb2b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 080da2a524 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 14410d46fe (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 0e12acb042 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bd5e136394 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 96919f4588 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a117ae3039 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f6796399ec (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 0a7929f96f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 47ae4a1f0b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d65864657f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 735793be5b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ba68f04a85 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f1d253615b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a78b7099e3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d90c40bd96 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 5f5ba2af03 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> edf7780032 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a37726dc18 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f03e5ccef0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 44759847fe (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 8a7994d157 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2ee3ec7759 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a7a7080cfc (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 8dcc73d184 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 3ff45b1287 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2f250dd5e8 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a32e8a4fd1 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> 029e33e9f0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bc87ec126b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a9b0c66c34 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 88f0ae57bd (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 38ca4b8512 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 8cbe3dcd02 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> dbc81233ab (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d4461869e8 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9c120ffe33 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> c01342bea9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> b75a91e7a6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bfcc03842f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fcadc7e13f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d60d422dbe (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 948e158f3d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 7ec793d809 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a2ef6edc89 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 3953b29f4d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f68b0fd740 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 4e857df9d2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 9766eb6ce9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 43b05ab727 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bcdce38fd1 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 28ba50a5ea (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bf8e093a53 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 24754e005d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ebf514d546 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a8f007a736 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
=======
    parms.units->descriptions = desc;
    parms.units->options =
        "miles,meters,kilometers,acres,hectares,cells,percent";
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
    parms.units->descriptions = desc;
    parms.units->options =
        "miles,meters,kilometers,acres,hectares,cells,percent";
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> dbc81233ab (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> d4461869e8 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
    parms.units->descriptions = desc;
    parms.units->options =
        "miles,meters,kilometers,acres,hectares,cells,percent";
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
    parms.units->descriptions = desc;
    parms.units->options =
        "miles,meters,kilometers,acres,hectares,cells,percent";
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9c120ffe33 (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 9766eb6ce9 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 70b9875805 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c01342bea9 (r.report: add default units, change to full unit names (#1666))
=======
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b75a91e7a6 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> bcdce38fd1 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a9170040dc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bfcc03842f (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fcadc7e13f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> bf8e093a53 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3162d6aeb (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d60d422dbe (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
>>>>>>> 24754e005d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 948e158f3d (r.report: add default units, change to full unit names (#1666))
=======
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 7ec793d809 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
=======
<<<<<<< HEAD
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> c7e767a1cc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a2ef6edc89 (r.report: add default units, change to full unit names (#1666))
=======
=======
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 5f5ba2af03 (r.report: add default units, change to full unit names (#1666))
=======
=======
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> edf7780032 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> f1d253615b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a37726dc18 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ba68f04a85 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 07ae314ad5 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f03e5ccef0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 735793be5b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 747ff50cd8 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 44759847fe (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> d65864657f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> ed995162de (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a7994d157 (r.report: add default units, change to full unit names (#1666))
=======
=======
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 47ae4a1f0b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 1dceb60f5b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ee3ec7759 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> f6796399ec (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 6ac86966bf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a7a7080cfc (r.report: add default units, change to full unit names (#1666))
=======
=======
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 96919f4588 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 97a8b8e667 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8dcc73d184 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 0e12acb042 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 57aae04049 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3ff45b1287 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 080da2a524 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 1c84c0d40e (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2f250dd5e8 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> fe15d84827 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 90f3380cbf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a32e8a4fd1 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 8cbe3dcd02 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 6171565840 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 38ca4b8512 (r.report: add default units, change to full unit names (#1666))
=======
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
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 029e33e9f0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 910ce69f58 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bc87ec126b (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a9b0c66c34 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 3ddce5eb55 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 88f0ae57bd (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 3953b29f4d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f68b0fd740 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 4e857df9d2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 9766eb6ce9 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 43b05ab727 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bcdce38fd1 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 28ba50a5ea (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bf8e093a53 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 24754e005d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 4ce3494716 (r.report: add default units, change to full unit names (#1666))
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
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> ebf514d546 (r.report: add default units, change to full unit names (#1666))
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
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
=======
<<<<<<< HEAD
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> c7e767a1cc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a8f007a736 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 95128cd1b3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> d90c40bd96 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
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
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 60fcd6afe6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a78b7099e3 (r.report: add default units, change to full unit names (#1666))
=======
=======
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
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f1d253615b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ba68f04a85 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 735793be5b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d65864657f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 47ae4a1f0b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 0a7929f96f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f6796399ec (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a117ae3039 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 96919f4588 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
>>>>>>> bd5e136394 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 0e12acb042 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 14410d46fe (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 080da2a524 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 80a8eaeb2b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fe15d84827 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 6171565840 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2774115069 (r.report: add default units, change to full unit names (#1666))
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
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a2a2cec695 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 910ce69f58 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 73ec075236 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 5ea900f7e5 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 3ddce5eb55 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 637f8ada3d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
    parms.units->answer = "cells,percent";
    parms.units->guisection = _("Statistics");

    parms.outfile = G_define_standard_option(G_OPT_F_OUTPUT);
    parms.outfile->required = NO;
    parms.outfile->label = _("Name for output file to hold the report");
    parms.outfile->description =
        _("If no output file given report is printed to standard output");

    parms.nv = G_define_standard_option(G_OPT_M_NULL_VALUE);
    parms.nv->answer = "*";
    parms.nv->guisection = _("Formatting");

    parms.pl = G_define_option();
    parms.pl->key = "page_length";
    parms.pl->type = TYPE_INTEGER;
    parms.pl->required = NO;
    parms.pl->description = _("Page length");
    parms.pl->answer = DEFAULT_PAGE_LENGTH;
    parms.pl->guisection = _("Formatting");

    parms.pw = G_define_option();
    parms.pw->key = "page_width";
    parms.pw->type = TYPE_INTEGER;
    parms.pw->required = NO;
    parms.pw->description = _("Page width");
    parms.pw->answer = DEFAULT_PAGE_WIDTH;
    parms.pw->guisection = _("Formatting");

    parms.nsteps = G_define_option();
    parms.nsteps->key = "nsteps";
    parms.nsteps->type = TYPE_INTEGER;
    parms.nsteps->required = NO;
    parms.nsteps->multiple = NO;
    parms.nsteps->answer = "255";
    parms.nsteps->description =
        _("Number of floating-point subranges to collect stats from");
    parms.nsteps->guisection = _("Floating point");

    parms.sort = G_define_option();
    parms.sort->key = "sort";
    parms.sort->type = TYPE_STRING;
    parms.sort->required = NO;
    parms.sort->multiple = NO;
    parms.sort->label = _("Sort output statistics by cell counts");
    parms.sort->description = _("Default: sorted by categories or intervals");
    parms.sort->options = "asc,desc";
    G_asprintf((char **)&(parms.sort->descriptions), "asc;%s;desc;%s",
               _("Sort by cell counts in ascending order"),
               _("Sort by cell counts in descending order"));
    parms.sort->guisection = _("Formatting");

    parms.format = G_define_standard_option(G_OPT_F_FORMAT);
    parms.format->guisection = _("Formatting");

    flags.h = G_define_flag();
    flags.h->key = 'h';
    flags.h->description = _("Suppress page headers");
    flags.h->guisection = _("Formatting");

    flags.f = G_define_flag();
    flags.f->key = 'f';
    flags.f->description = _("Use formfeeds between pages");
    flags.f->guisection = _("Formatting");

    flags.e = G_define_flag();
    flags.e->key = 'e';
    flags.e->description = _("Scientific format");
    flags.e->guisection = _("Formatting");

    flags.n = G_define_flag();
    flags.n->key = 'n';
    flags.n->description = _("Do not report no data value");
    flags.n->guisection = _("No data");

    flags.N = G_define_flag();
    flags.N->key = 'a';
    flags.N->description = _("Do not report cells where all maps have no data");
    flags.N->guisection = _("No data");

    flags.C = G_define_flag();
    flags.C->key = 'c';
    flags.C->description =
        _("Report for cats floating-point ranges (floating-point maps only)");
    flags.C->guisection = _("Floating point");

    flags.i = G_define_flag();
    flags.i->key = 'i';
    flags.i->description =
        _("Read floating-point map as integer (use map's quant rules)");
    flags.i->guisection = _("Floating point");

    /* hidden feature.
     * if first arg is >file just run r.stats into this file and quit
     * if first arg is <file, run report from stats in file
     * (this feature is for the interactive version of this program -
     *  to get more than one report without re-running r.stats)
     */
    stats_flag = EVERYTHING;
    if (argc > 1) {
        if (argv[1][0] == '<' || argv[1][0] == '>') {
            stats_file = argv[1] + 1;
            if (argv[1][0] == '<')
                stats_flag = REPORT_ONLY;
            else {
                unlink(stats_file);
                stats_flag = STATS_ONLY;
            }
            argc--;
            argv++;
        }
    }

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    use_formfeed = flags.f->answer;
    with_headers = !flags.h->answer;
    e_format = flags.e->answer;
    no_nulls = flags.n->answer;
    no_nulls_all = flags.N->answer;
    cat_ranges = flags.C->answer;
    as_int = flags.i->answer;

    if (strcmp(parms.format->answer, "json") == 0) {
        format = JSON;
    }
    else {
        format = PLAIN;
    }

    for (i = 0; parms.cell->answers[i]; i++)
        parse_layer(parms.cell->answers[i]);
    if (parms.units->answers)
        for (i = 0; parms.units->answers[i]; i++)
            parse_units(parms.units->answers[i]);

    sscanf(parms.nsteps->answer, "%d", &nsteps);
    if (nsteps <= 0) {
        G_warning(_("nsteps has to be > 0; using nsteps=255"));
        nsteps = 255;
    }

    if (sscanf(parms.pl->answer, "%d", &page_length) != 1 || page_length < 0) {
        G_fatal_error(_("Illegal page length"));
    }

    if (sscanf(parms.pw->answer, "%d", &page_width) != 1 || page_width < 1) {
        G_fatal_error(_("Illegal page width"));
    }

    if (parms.outfile->answer) {
        if (freopen(parms.outfile->answer, "w", stdout) == NULL) {
            perror(parms.outfile->answer);
            exit(EXIT_FAILURE);
        }
    }
    no_data_str = parms.nv->answer;

    /* determine sorting method */
    do_sort = SORT_DEFAULT; /* sort by cats by default */
    if (parms.sort->answer) {
        switch (parms.sort->answer[0]) {
        case 'a':
            do_sort = SORT_ASC;
            break;
        case 'd':
            do_sort = SORT_DESC;
            break;
        default:
            G_debug(1, "Sorting by '%s' not supported", parms.sort->answer);
            break;
        }
    }

    return 0;
}

int parse_units(char *s)
{
    int x;

    if (match(s, "miles", 2))
        x = SQ_MILES;
    else if (match(s, "meters", 2))
        x = SQ_METERS;
    else if (match(s, "kilometers", 1))
        x = SQ_KILOMETERS;
    else if (match(s, "acres", 1))
        x = ACRES;
    else if (match(s, "hectares", 1))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9c120ffe33 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b75a91e7a6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fcadc7e13f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a7929f96f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a117ae3039 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd5e136394 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14410d46fe (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 80a8eaeb2b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> b75a91e7a6 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> fcadc7e13f (r.report: add default units, change to full unit names (#1666))
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
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
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
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
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
=======
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
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
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
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
        x = HECTARES;
    else if (match(s, "cells", 1))
        x = CELL_COUNTS;
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 8cbe3dcd02 (r.report: add default units, change to full unit names (#1666))
=======
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
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 029e33e9f0 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a9b0c66c34 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 4e857df9d2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43b05ab727 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28ba50a5ea (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 43b05ab727 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 28ba50a5ea (r.report: add default units, change to full unit names (#1666))
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
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
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
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
=======
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
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
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
=======
=======
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
        x = HECTARES;
    else if (match(s, "cells", 1))
        x = CELL_COUNTS;
=======
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 029e33e9f0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a9b0c66c34 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 8cbe3dcd02 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
        x = HECTARES;
    else if (match(s, "cells", 1))
        x = CELL_COUNTS;
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
=======
<<<<<<< HEAD
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
=======
=======
<<<<<<< HEAD
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8cbe3dcd02 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 029e33e9f0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a9b0c66c34 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
=======
<<<<<<< HEAD
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 0a7929f96f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
>>>>>>> a117ae3039 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
>>>>>>> bd5e136394 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 14410d46fe (r.report: add default units, change to full unit names (#1666))
=======
=======
<<<<<<< HEAD
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 80a8eaeb2b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
>>>>>>> a2a2cec695 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 5ea900f7e5 (r.report: add default units, change to full unit names (#1666))
	x = HECTARES;
    else if (match(s, "cells", 1))
	x = CELL_COUNTS;
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9c120ffe33 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> b75a91e7a6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fcadc7e13f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8cbe3dcd02 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 029e33e9f0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a9b0c66c34 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43b05ab727 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 28ba50a5ea (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0a7929f96f (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a117ae3039 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd5e136394 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14410d46fe (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 80a8eaeb2b (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2a2cec695 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ea900f7e5 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4e857df9d2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
        x = HECTARES;
    else if (match(s, "cells", 1))
        x = CELL_COUNTS;
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
        x = HECTARES;
    else if (match(s, "cells", 1))
        x = CELL_COUNTS;
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
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
        x = HECTARES;
    else if (match(s, "cells", 1))
        x = CELL_COUNTS;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
        x = HECTARES;
    else if (match(s, "cells", 1))
        x = CELL_COUNTS;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
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
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
=======
        x = HECTARES;
    else if (match(s, "cells", 1))
        x = CELL_COUNTS;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
        x = HECTARES;
    else if (match(s, "cells", 1))
        x = CELL_COUNTS;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9c120ffe33 (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b75a91e7a6 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fcadc7e13f (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> aa6627647b (r.report: add default units, change to full unit names (#1666))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de7c0c8532 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bb2b4ce7ef (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 51375b865a (r.report: add default units, change to full unit names (#1666))
=======
=======
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
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 852e51da65 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a405775a95 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> d2caf4b753 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bb54dfab34 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> e72675b39d (r.report: add default units, change to full unit names (#1666))
=======
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
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 61cfc5bf9d (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 85a4794a95 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 881be39b4f (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> fc4eec9ad0 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 901aaec734 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bd55e4817e (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 8cbe3dcd02 (r.report: add default units, change to full unit names (#1666))
=======
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
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 029e33e9f0 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a9b0c66c34 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 26eb6eb23c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 4e857df9d2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 905468f175 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 43b05ab727 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 28ba50a5ea (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9b491a9166 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
>>>>>>> ba75bc97c9 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 382767a94c (r.report: add default units, change to full unit names (#1666))
>>>>>>> 749b1e14fa (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 004496fb45 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 2c11d30dc6 (r.report: add default units, change to full unit names (#1666))
=======
=======
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
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 2686990028 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 3aa8160733 (r.report: add default units, change to full unit names (#1666))
=======
=======
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
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> b7dd487b9b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04463aaa06 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 853a53eb64 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 34cabaea1c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 72cfe4b0db (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 222f5507fd (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> e62d1f3a00 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> d79db3d3aa (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 76ed2b4b4a (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 75bcf4759c (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 0a7929f96f (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 18f6cb33e9 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> a117ae3039 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 093f9734fc (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> bd5e136394 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e9045a0d92 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 14410d46fe (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6a73bac014 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 80a8eaeb2b (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> 703d631ab6 (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
>>>>>>> c6e15ef3ac (r.report: add default units, change to full unit names (#1666))
=======
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
=======
>>>>>>> 3cc5926ebf (r.report: add default units, change to full unit names (#1666))
>>>>>>> a2a2cec695 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 796386b4d9 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 5ea900f7e5 (r.report: add default units, change to full unit names (#1666))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
    else if (match(s, "percent_cover", 1))
        x = PERCENT_COVER;
    else {
        G_usage();
        exit(EXIT_FAILURE);
    }
    if (nunits >= MAX_UNITS) {
        G_fatal_error(_("Only %d unit%s allowed"), MAX_UNITS,
                      MAX_UNITS == 1 ? "" : "s");
    }
    unit[nunits].type = x;
    nunits++;

    return 0;
}

int parse_layer(char *s)
{
    char name[GNAME_MAX];
    const char *mapset;
    struct FPRange fp_range;
    int n;

    strcpy(name, s);
    mapset = G_find_raster2(name, "");

    if (mapset == NULL)
        G_fatal_error(_("Raster map <%s> not found"), s);

    n = nlayers++;
    layers = (LAYER *)G_realloc(layers, nlayers * sizeof(LAYER));
    is_fp = (int *)G_realloc(is_fp, (nlayers + 1) * sizeof(int));
    DMAX = (DCELL *)G_realloc(DMAX, (nlayers + 1) * sizeof(DCELL));
    DMIN = (DCELL *)G_realloc(DMIN, (nlayers + 1) * sizeof(DCELL));
    if (!as_int)
        is_fp[n] = Rast_map_is_fp(name, mapset);
    else
        is_fp[n] = 0;
    if (is_fp[n]) {
        if (Rast_read_fp_range(name, mapset, &fp_range) < 0)
            G_fatal_error(_("Unable to read fp range for raster map <%s>"),
                          name);
        Rast_get_fp_range_min_max(&fp_range, &DMIN[n], &DMAX[n]);
    }

    layers[n].name = G_store(name);
    layers[n].mapset = mapset;
    if (Rast_read_cats(name, mapset, &layers[n].labels) < 0)
        G_fatal_error(_("Unable to read category file of raster map <%s@%s>"),
                      name, mapset);

    return 0;
}

int match(char *s, char *key, int min)
{
    size_t len;

    len = strlen(s);
    if ((int)len < min)
        return 0;
    return strncmp(s, key, len) == 0;
}
