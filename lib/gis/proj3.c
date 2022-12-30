/*!
   \file lib/gis/proj3.c

   \brief GIS Library - Projection support (database)

   (C) 2001-2014 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Original author CERL
 */

/* TODO: the G_database_*() functions should be renamed to G_location_*()
 * because they apply to a GRASS location, not to a GRASS database */

#include <string.h>
#include <grass/gis.h>
#include <grass/glocale.h>

static const char *lookup_proj(const char *);
static const char *lookup_units(const char *);
static const char *lookup_epsg(void);
static int equal(const char *, const char *);
static int lower(char);

static int initialized;
static struct Key_Value *proj_info, *proj_units, *proj_epsg;

static void init(void)
{
    if (G_is_initialized(&initialized))
        return;

    proj_info = G_get_projinfo();
    proj_units = G_get_projunits();
    proj_epsg = G_get_projepsg();

    G_initialize_done(&initialized);
}

/*!
   \brief Get units (localized) name for the current location

   Returns a string describing the database grid units. It returns a
   plural form (eg. 'feet') if <i>plural</i> is non-zero. Otherwise it
   returns a singular form (eg. 'foot').

   \param plural plural form if non-zero

   \return localized units name
 */
const char *G_database_unit_name(int plural)
{
    int units;

    units = G_database_unit();
    return G_get_units_name(units, plural, FALSE);
}

/*!
   \brief Get units id for the current location

   \return units id
 */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
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
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
int G_database_unit(void)
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
=======
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca99b767dd (Fix missing function prototypes (#2727))
=======
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
int G_database_unit(void)
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
int G_database_unit(void)
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
int G_database_unit(void)
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
int G_database_unit(void)
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int G_database_unit(void)
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
int G_database_unit(void)
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
int G_database_unit(void)
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
int G_database_unit(void)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int G_database_unit(void)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
int G_database_unit(void)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
int G_database_unit()
=======
int G_database_unit(void)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
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
>>>>>>> osgeo-main
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 8544eecf2f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
=======
int G_database_unit(void)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
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
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
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
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 7733cc06c4 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e9b4321267 (r.horizon manual - fix typo (#2794))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d7db4d7708 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d54647dc67 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c99e518a1a (Fix missing function prototypes (#2727))
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
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
int G_database_unit(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ca99b767dd (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ef2654d3c4 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int G_database_unit()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
{
    int units;
    const char *name;

    units = G_projection_units(G_projection());

    if (units == U_UNDEFINED) {
        name = lookup_units("unit");
        if (!name)
            return U_UNKNOWN;

        if (strcasecmp(name, "meter") == 0 || strcasecmp(name, "metre") == 0 ||
            strcasecmp(name, "meters") == 0 || strcasecmp(name, "metres") == 0)
            units = U_METERS;
        else if (strcasecmp(name, "kilometer") == 0 ||
                 strcasecmp(name, "kilometre") == 0 ||
                 strcasecmp(name, "kilometers") == 0 ||
                 strcasecmp(name, "kilometres") == 0)
            units = U_KILOMETERS;
        else if (strcasecmp(name, "acre") == 0 ||
                 strcasecmp(name, "acres") == 0)
            units = U_ACRES;
        else if (strcasecmp(name, "hectare") == 0 ||
                 strcasecmp(name, "hectares") == 0)
            units = U_HECTARES;
        else if (strcasecmp(name, "mile") == 0 ||
                 strcasecmp(name, "miles") == 0)
            units = U_MILES;
        else if (strcasecmp(name, "foot") == 0 || strcasecmp(name, "feet") == 0)
            units = U_FEET;
        else if (strcasecmp(name, "foot_us") == 0 ||
                 strcasecmp(name, "foot_uss") == 0)
            units = U_USFEET;
        else if (strcasecmp(name, "degree") == 0 ||
                 strcasecmp(name, "degrees") == 0)
            units = U_DEGREES;
        else
            units = U_UNKNOWN;
    }
    return units;
}

/*!
   \brief Query cartographic projection for the current location

   Returns a pointer to a string which is a printable name for
   projection code <i>proj</i> (as returned by G_projection). Returns
   NULL if <i>proj</i> is not a valid projection.

   \return projection name
 */
const char *G_database_projection_name(void)
{
    int n;
    const char *name;

    switch (n = G_projection()) {
    case PROJECTION_XY:
    case PROJECTION_UTM:
    case PROJECTION_LL:
        return G_projection_name(n);
    }

    name = lookup_proj("name");
    if (!name)
        return _("Unknown projection");

    return name;
}

/*!
   \brief Conversion to meters

   Returns a factor which converts the grid unit to meters (by
   multiplication). If the database is not metric (eg. imagery) then
   0.0 is returned.

   \return value
 */
double G_database_units_to_meters_factor(void)
{
    const char *unit;
    const char *buf;
    double factor;
    int n;

    /* TODO: sync with definitions in ../proj/units.table */
    static const struct {
        char *unit;
        double factor;
    } table[] = {{"unit", 1.0},   {"meter", 1.0},
                 {"foot", .3048}, {"foot_us", 1200 / 3937.},
                 {"inch", .0254}, {NULL, 0.0}};

    factor = 0.0;
    buf = lookup_units("meters");
    if (buf)
        sscanf(buf, "%lf", &factor);
    if (factor <= 0.0) {
        unit = G_database_unit_name(0);
        for (n = 0; table[n].unit; n++)
            if (equal(unit, table[n].unit)) {
                factor = table[n].factor;
                break;
            }
    }
    return factor;
}

/*!
   \brief Get datum name for the current location

   Returns a pointer to the name of the map datum of the current
   database. If there is no map datum explicitly associated with the
   actual database, the standard map datum WGS84 is returned, on error
   a NULL pointer is returned.

   \return datum name
 */
const char *G_database_datum_name(void)
{
    const char *name;
    char buf[256], params[256];
    int datumstatus;

    name = lookup_proj("datum");
    if (name)
        return name;
    else if (!proj_info)
        return NULL;
    else
        datumstatus = G_get_datumparams_from_projinfo(proj_info, buf, params);

    if (datumstatus == 2)
        return G_store(params);
    else
        return NULL;
}

/*!
   \brief Get ellipsoid name for the current location

   \return pointer to valid name if ok
   \return NULL on error
 */
const char *G_database_ellipse_name(void)
{
    const char *name;

    name = lookup_proj("ellps");
    if (!name) {
        char buf[256];
        double a, es;

        G_get_ellipsoid_parameters(&a, &es);
        sprintf(buf, "a=%.16g es=%.16g", a, es);
        name = G_store(buf);
    }

    /* strcpy (name, "Unknown ellipsoid"); */
    return name;
}

/*!
   \brief Get EPGS code for the current location

   \return pointer to valid EPSG code on success
   \return NULL on error
 */
const char *G_database_epsg_code(void)
{
    return lookup_epsg();
}

const char *lookup_proj(const char *key)
{
    init();
    return G_find_key_value(key, proj_info);
}

const char *lookup_units(const char *key)
{
    init();
    return G_find_key_value(key, proj_units);
}

const char *lookup_epsg(void)
{
    init();
    return G_find_key_value("epsg", proj_epsg);
}

int equal(const char *a, const char *b)
{
    if (a == NULL || b == NULL)
        return a == b;
    while (*a && *b)
        if (lower(*a++) != lower(*b++))
            return 0;
    if (*a || *b)
        return 0;
    return 1;
}

int lower(char c)
{
    if (c >= 'A' && c <= 'Z')
        c += 'a' - 'A';
    return c;
}
