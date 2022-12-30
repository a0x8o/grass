/****************************************************************************
 *
 * MODULE:       g.filename
 * AUTHOR(S):    Michael Shapiro CERL (original contributor)
 *               Markus Neteler <neteler itc.it>,
 *               Bernhard Reiter <bernhard intevation.de>,
 *               Glynn Clements <glynn gclements.plus.com>,
 *               Hamish Bowman <hamish_b yahoo.com>,
 *               Jan-Oliver Wagner <jan intevation.de>
 * PURPOSE:      Prints GRASS data base file names
 * COPYRIGHT:    (C) 1999-2006 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <grass/gis.h>
#include <grass/glocale.h>

int main(int argc, char *argv[])
{
    char path[1024];
    const char *element;
    const char *mapset;
    const char *name;
    struct GModule *module;
    struct Option *opt1;
    struct Option *opt2;
    struct Option *opt3;
    struct Flag *flag_create;

    G_gisinit(argv[0]);

    module = G_define_module();
    G_add_keyword(_("general"));
    G_add_keyword(_("map management"));
    G_add_keyword(_("scripts"));
    module->description = _("Prints GRASS data base file names.");

    /* Define the different options */

    opt1 = G_define_option();
    opt1->key = "element";
    opt1->type = TYPE_STRING;
    opt1->required = YES;
    opt1->description = _("Name of an element");

    opt3 = G_define_option();
    opt3->key = "file";
    opt3->type = TYPE_STRING;
    opt3->required = YES;
    opt3->description = _("Name of a database file");

    opt2 = G_define_option();
    opt2->key = "mapset";
    opt2->type = TYPE_STRING;
    opt2->required = NO;
    opt2->description = _("Name of a mapset (default: current)");

    flag_create = G_define_flag();
    flag_create->key = 'c';
    flag_create->label = _("Create element directory in the current mapset");
    flag_create->description =
        _("If element directory for database file does not exist, create it");

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);

    element = opt1->answer;
    name = opt3->answer;

    if (opt2->answer)
        mapset = opt2->answer;
    else
        mapset = G_mapset();

    if (strcmp(mapset, ".") == 0 || strcmp(mapset, "") == 0)
        mapset = G_mapset();
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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

    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1dfda93def (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 14e4def588 (libcairodriver: enable Cairo with and without Fontconfig (#1697))
        G_make_mapset_object_group(element);
<<<<<<< HEAD
    }

<<<<<<< HEAD
=======
    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
        G_make_mapset_element(element);
=======
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
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
=======
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
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
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))

    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
        G_make_mapset_object_group(element);
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7ce58cb82a (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 486a1e2551 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0b689384c0 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
>>>>>>> c75ae04d0e (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 0758bb6a96 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 58d3e01cce (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 11db328c38 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> a61a313997 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de5fa2147f (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD

    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
        G_make_mapset_object_group(element);
<<<<<<< HEAD
    }

<<<<<<< HEAD
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c75ae04d0e (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> 11db328c38 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> a61a313997 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> de5fa2147f (pygrass: Add update parameters method to Module (#1712))
    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> de5fa2147f (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> a61a313997 (pygrass: Add update parameters method to Module (#1712))
        G_make_mapset_element(element);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 11db328c38 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
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
=======
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
>>>>>>> osgeo-main
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))

    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
        G_make_mapset_object_group(element);
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
=======
<<<<<<< HEAD
=======
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
=======
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD

    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
        G_make_mapset_object_group(element);
<<<<<<< HEAD
    }

<<<<<<< HEAD
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 0758bb6a96 (pygrass: Add update parameters method to Module (#1712))
    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
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
=======
>>>>>>> c75ae04d0e (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 0758bb6a96 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
        G_make_mapset_element(element);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        G_make_mapset_object_group(element);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))

=======
<<<<<<< HEAD
=======
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        G_make_mapset_object_group(element);
    }

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 58d3e01cce (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
=======
<<<<<<< HEAD
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 1dfda93def (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
=======
    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 58d3e01cce (pygrass: Add update parameters method to Module (#1712))
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
        G_make_mapset_element(element);
<<<<<<< HEAD
<<<<<<< HEAD
=======
        G_make_mapset_object_group(element);
>>>>>>> 9d4a079d2e (libcairodriver: enable Cairo with and without Fontconfig (#1697))
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 92d65cd4a6 (pygrass: Add update parameters method to Module (#1712))
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
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f75642e9e3 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dd9ee76548 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1dfda93def (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))

=======
<<<<<<< HEAD
=======
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
    /* Create element directory if requested and in current mapset. */
    if (flag_create) {
        if (strcmp(mapset, G_mapset()) != 0) {
            G_fatal_error("Cannot create <%s> (flag -%c):"
                          " <%s> is not the current mapset (%s)",
                          element, flag_create->key, mapset, G_mapset());
        }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        G_make_mapset_object_group(element);
    }

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
        G_make_mapset_element(element);
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 0b689384c0 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 486a1e2551 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 7ce58cb82a (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> c75ae04d0e (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 0758bb6a96 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 58d3e01cce (pygrass: Add update parameters method to Module (#1712))
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
    }

>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 11db328c38 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> a61a313997 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> de5fa2147f (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
    G_file_name(path, element, name, mapset);

    fprintf(stdout, "file='%s'\n", path);
    exit(EXIT_SUCCESS);
}
