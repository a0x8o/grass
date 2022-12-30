/*****************************************************************************
 *
 * MODULE:       g.proj
 * AUTHOR(S):    Paul Kelly - paul-grass@stjohnspoint.co.uk
 *               Frank Warmerdam
 *               Radim Blazek
 * PURPOSE:      Provides a means of reporting the contents of GRASS
 *               projection information files and creating
 *               new projection information files.
 * COPYRIGHT:    (C) 2001-2007 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <grass/gis.h>
#include <grass/gprojects.h>
#include <grass/glocale.h>
#include <grass/config.h>

#ifdef HAVE_OGR
#include <gdal.h>
#include <ogr_api.h>
#include <cpl_csv.h>
#endif

#include "local_proto.h"

static void set_default_region(void);

/**
 * \brief Read projection and region information from current location
 *
 * Reads projection and region information from current location and
 * stores in global structs cellhd, projinfo and projunits.
 **/

void input_currloc(void)
{
    G_get_default_window(&cellhd);
    if (cellhd.proj != PROJECTION_XY) {
        projsrid = G_get_projsrid();
        projwkt = G_get_projwkt();
        projinfo = G_get_projinfo();
        projunits = G_get_projunits();
        /* projepsg = G_get_projepsg(); */
    }

    return;
}

/**
 * \brief Populates global cellhd with "default" region settings
 **/

static void set_default_region(void)
{
    /* If importing projection there will be no region information, so
     * set some default values */
    cellhd.rows = 1;
    cellhd.rows3 = 1;
    cellhd.cols = 1;
    cellhd.cols3 = 1;
    cellhd.depths = 1.;
    cellhd.north = 1.;
    cellhd.ns_res = 1.;
    cellhd.ns_res3 = 1.;
    cellhd.south = 0.;
    cellhd.west = 0.;
    cellhd.ew_res = 1.;
    cellhd.ew_res3 = 1.;
    cellhd.east = 1.;
    cellhd.top = 1.;
    cellhd.tb_res = 1.;
    cellhd.bottom = 0.;

    return;
}

#ifdef HAVE_OGR
static void set_gdal_region(GDALDatasetH);
static void set_authnamecode(OGRSpatialReferenceH);

/**
 * \brief Read projection information in WKT format from stdin or a file
 *
 * Reads projection information from a file or stdin and stores in global
 * structs projinfo and projunits.
 * Populates global cellhd with default region information.
 *
 * \param wktfile File to read WKT co-ordinate system description from; -
 *                for stdin
 *
 * \return        2 if a projected or lat/long co-ordinate system has been
 *                defined; 1 if an unreferenced XY co-ordinate system has
 *                been defined
 **/

int input_wkt(char *wktfile)
{
    FILE *infd;
    char buff[8192], *tmpwkt;
    OGRSpatialReferenceH hSRS;
    char *papszOptions[3];
    int ret;

    if (strcmp(wktfile, "-") == 0)
        infd = stdin;
    else
        infd = fopen(wktfile, "r");

    if (infd) {
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d4879ffd54 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d69d602427 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> da1f354017 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> dd6ab211c8 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eec6e0dfee (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> ebd08a840c (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 651687e3fd (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2285639e2 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
=======
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 42a6a4145b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> fb966e4371 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 65f70a77ac (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 396b5cfa4f (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 89f6fd2f96 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> ffbd80b751 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 174adf65f4 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3b2c5a2ad2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> de8a1fa341 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> d241321b80 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 478eacddcd (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 79c09abba5 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 46a965d9e9 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f92b908048 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7c43c51dde (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 284a65cbb8 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> cfd6be023a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> b5184deb8b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fab41f991b (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 8ef5c8e5e3 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 016af75c85 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 6a06d2e78c (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> cdb769bc1e (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
=======
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> d7be28bb1b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 47ada2c507 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e4a266d5e1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> c3243bb1bd (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 79d87b3f39 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5ec354b4a4 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 65f70a77ac (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 04f7859177 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 396b5cfa4f (g.proj: fix reading input WKT (#1582))
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
>>>>>>> 284a65cbb8 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 89f6fd2f96 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 0338dc8268 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ffbd80b751 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> eb4ab86d92 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 174adf65f4 (g.proj: fix reading input WKT (#1582))
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
>>>>>>> fab41f991b (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b2c5a2ad2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de8a1fa341 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> d9be065247 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d241321b80 (g.proj: fix reading input WKT (#1582))
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
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 5b2a09c6ef (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 478eacddcd (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5202d5f7da (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> f296bbcae1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 1f00014c4a (g.proj: fix reading input WKT (#1582))
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
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
>>>>>>> 53cfc6049b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> b1985ef3ca (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 01a2cb48f6 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 47f2e379fb (g.proj: fix reading input WKT (#1582))
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
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> db9ea57391 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 42533ebf37 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 46c77518c7 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 8fa433b01b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ac5d03ef05 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5806596b34 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 140d339c38 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 59def94d1b (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> d7be28bb1b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> dd6ab211c8 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> c3b982c5a4 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 47ada2c507 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> eec6e0dfee (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 16e0f7fc96 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ebd08a840c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 769ad64a54 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> e4a266d5e1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 651687e3fd (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 35a60eb901 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
>>>>>>> a2285639e2 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e8925c7df7 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 56bc21b402 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> e4a266d5e1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> db23316322 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 74ab7a866e (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 573458c7fe (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e1642feb6f (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> d6601a1e75 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> a095a57fb9 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 9400969c2f (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> c1b258ffc4 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 0d53ace193 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> dab7af79b2 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 67baae8b16 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 1d80a62f1a (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> edc424b09b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e70434a447 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 9a000933e9 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 9af2478db1 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6d863be9ad (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 71b8975be5 (g.proj: fix reading input WKT (#1582))
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
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 82881aaaec (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 1306fa28a0 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> dc8b886312 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 2f9b4a6e73 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 17c5b80c11 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 38fcad4cdf (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> a3706b16a1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3ef949b911 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 460748a7fb (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ab354ae66a (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 9fb6588182 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 4b305e9816 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> c1a5635118 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 53865df964 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> a97572757d (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 8bfd50f462 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 10ccb1268a (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 0539d4fc84 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> cd0e4defc1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 33f2655b34 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6307e79ee9 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> a6287b7801 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 819b2acedb (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 8bc71453f2 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 8e791e0ba5 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 122aa064f5 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> c585c92c1e (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> bc42470098 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> eb742340df (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> a21a1674c5 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 21a0d24296 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5844bf14a6 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 76ed571f8d (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3b8c627dda (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 1f5d06186a (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> cfb8a4e049 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 8271eeb64f (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 43c1641739 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> da1f354017 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 7a9bff206b (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> c3243bb1bd (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> d69d602427 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3e625d40bb (g.proj: fix reading input WKT (#1582))
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
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 79d87b3f39 (g.proj: fix reading input WKT (#1582))
>>>>>>> d4879ffd54 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 674042b19b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 1411c71e15 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 2c11751de0 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> d6e1feb5a7 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 7350ba56e1 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 7d640949f0 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> f77988fa9b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> dbe7a0c10a (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 851366e8db (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 2867fee4a7 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 66af96f1a0 (g.proj: fix reading input WKT (#1582))
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
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 5336d0cf12 (g.proj: fix reading input WKT (#1582))
>>>>>>> ef05990d3a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5ec354b4a4 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> f92b908048 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 04f7859177 (g.proj: fix reading input WKT (#1582))
>>>>>>> 7c43c51dde (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 284a65cbb8 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 0338dc8268 (g.proj: fix reading input WKT (#1582))
>>>>>>> cfd6be023a (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> eb4ab86d92 (g.proj: fix reading input WKT (#1582))
>>>>>>> b5184deb8b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fab41f991b (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
>>>>>>> 8ef5c8e5e3 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> d9be065247 (g.proj: fix reading input WKT (#1582))
>>>>>>> 016af75c85 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> f296bbcae1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> d0e4dde627 (g.proj: fix reading input WKT (#1582))
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
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
>>>>>>> 53cfc6049b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> bca28e773e (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> edaa97bcbf (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
        size_t wktlen;

        wktlen = fread(buff, 1, sizeof(buff), infd);
        if (wktlen == sizeof(buff))
            G_fatal_error(_("Input WKT definition is too long"));
        if (ferror(infd))
            G_fatal_error(_("Error reading WKT definition"));
        else
            fclose(infd);
        /* terminate WKT string */
        buff[wktlen] = '\0';
        /* Get rid of newlines */
        G_squeeze(buff);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> main
>>>>>>> d69d602427 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> 53cfc6049b (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dd6ab211c8 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> 651687e3fd (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
=======
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> d0e4dde627 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
>>>>>>> f296bbcae1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5b2a09c6ef (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5806596b34 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 9400969c2f (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> edc424b09b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 82881aaaec (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a3706b16a1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> c1a5635118 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> cd0e4defc1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 8e791e0ba5 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 21a0d24296 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 8271eeb64f (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7d640949f0 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5336d0cf12 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6a06d2e78c (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> f92b908048 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7c43c51dde (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 8ef5c8e5e3 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 016af75c85 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
>>>>>>> 284a65cbb8 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> fab41f991b (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 5b2a09c6ef (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> fab41f991b (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ef05990d3a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> f77988fa9b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 43c1641739 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5844bf14a6 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 122aa064f5 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 33f2655b34 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 53865df964 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3ef949b911 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 1306fa28a0 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e70434a447 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> c1b258ffc4 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 74ab7a866e (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 140d339c38 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> db9ea57391 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5202d5f7da (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 478eacddcd (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3b2c5a2ad2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> d7be28bb1b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 47ada2c507 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
=======
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e4a266d5e1 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
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
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> c3243bb1bd (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 79d87b3f39 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 89f6fd2f96 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 284a65cbb8 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 42a6a4145b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> fb966e4371 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cdb769bc1e (g.proj: fix reading input WKT (#1582))
=======
=======
<<<<<<< HEAD
>>>>>>> b1985ef3ca (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5ec354b4a4 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65f70a77ac (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c43c51dde (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 04f7859177 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 396b5cfa4f (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 89f6fd2f96 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 0338dc8268 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ffbd80b751 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b5184deb8b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> eb4ab86d92 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 174adf65f4 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b2c5a2ad2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de8a1fa341 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 016af75c85 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> d9be065247 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d241321b80 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5b2a09c6ef (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 478eacddcd (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5202d5f7da (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
>>>>>>> d0e4dde627 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f296bbcae1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 1f00014c4a (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> f296bbcae1 (g.proj: fix reading input WKT (#1582))
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
>>>>>>> 53cfc6049b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b1985ef3ca (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a2cb48f6 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> edaa97bcbf (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> b845e8d135 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 47f2e379fb (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> db9ea57391 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 42533ebf37 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 46c77518c7 (g.proj: fix reading input WKT (#1582))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 8fa433b01b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ac5d03ef05 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5806596b34 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 140d339c38 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 59def94d1b (g.proj: fix reading input WKT (#1582))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> d7be28bb1b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> dd6ab211c8 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> c3b982c5a4 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 47ada2c507 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> eec6e0dfee (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 16e0f7fc96 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
=======
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ebd08a840c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 769ad64a54 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e4a266d5e1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 651687e3fd (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 35a60eb901 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
>>>>>>> a2285639e2 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e8925c7df7 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 56bc21b402 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> e4a266d5e1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> db23316322 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 74ab7a866e (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 573458c7fe (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e1642feb6f (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> d6601a1e75 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> a095a57fb9 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 9400969c2f (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> c1b258ffc4 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 0d53ace193 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> dab7af79b2 (g.proj: fix reading input WKT (#1582))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 67baae8b16 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 1d80a62f1a (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> edc424b09b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e70434a447 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 9a000933e9 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 9af2478db1 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 6d863be9ad (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 71b8975be5 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 82881aaaec (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 1306fa28a0 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> dc8b886312 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 2f9b4a6e73 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 17c5b80c11 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 38fcad4cdf (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> a3706b16a1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3ef949b911 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 460748a7fb (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ab354ae66a (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 9fb6588182 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 4b305e9816 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> c1a5635118 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 53865df964 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> a97572757d (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 8bfd50f462 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 10ccb1268a (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 0539d4fc84 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> cd0e4defc1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 33f2655b34 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6307e79ee9 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> a6287b7801 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 819b2acedb (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 8bc71453f2 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 8e791e0ba5 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 122aa064f5 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> c585c92c1e (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> bc42470098 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> eb742340df (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> a21a1674c5 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 21a0d24296 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5844bf14a6 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 76ed571f8d (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3b8c627dda (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 1f5d06186a (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> cfb8a4e049 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 8271eeb64f (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 43c1641739 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> da1f354017 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 7a9bff206b (g.proj: fix reading input WKT (#1582))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> c3243bb1bd (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> d69d602427 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3e625d40bb (g.proj: fix reading input WKT (#1582))
=======
=======
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 79d87b3f39 (g.proj: fix reading input WKT (#1582))
>>>>>>> d4879ffd54 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 674042b19b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 1411c71e15 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 2c11751de0 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> d6e1feb5a7 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 7350ba56e1 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7d640949f0 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> f77988fa9b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> dbe7a0c10a (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 851366e8db (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 2867fee4a7 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 66af96f1a0 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5336d0cf12 (g.proj: fix reading input WKT (#1582))
>>>>>>> ef05990d3a (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 79c09abba5 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 46a965d9e9 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 6a06d2e78c (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5ec354b4a4 (g.proj: fix reading input WKT (#1582))
>>>>>>> f92b908048 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7c43c51dde (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
>>>>>>> 284a65cbb8 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 0338dc8268 (g.proj: fix reading input WKT (#1582))
>>>>>>> cfd6be023a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> b5184deb8b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
>>>>>>> fab41f991b (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
>>>>>>> 8ef5c8e5e3 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 016af75c85 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5b2a09c6ef (g.proj: fix reading input WKT (#1582))
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> f296bbcae1 (g.proj: fix reading input WKT (#1582))
>>>>>>> d0e4dde627 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
>>>>>>> bca28e773e (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> edaa97bcbf (g.proj: fix reading input WKT (#1582))
	size_t wktlen;

	wktlen = fread(buff, 1, sizeof(buff), infd);
	if (wktlen == sizeof(buff))
	    G_fatal_error(_("Input WKT definition is too long"));
	if (ferror(infd))
	    G_fatal_error(_("Error reading WKT definition"));
	else
	    fclose(infd);
	/* terminate WKT string */
	buff[wktlen] = '\0';
	/* Get rid of newlines */
	G_squeeze(buff);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 47ada2c507 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
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
>>>>>>> 79d87b3f39 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> cdb769bc1e (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 65f70a77ac (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> ffbd80b751 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> cfd6be023a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
>>>>>>> 89f6fd2f96 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> de8a1fa341 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 478eacddcd (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5202d5f7da (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> b1985ef3ca (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 01a2cb48f6 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> db9ea57391 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 46c77518c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 140d339c38 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 59def94d1b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 16e0f7fc96 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 769ad64a54 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e8925c7df7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 56bc21b402 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 74ab7a866e (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e1642feb6f (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> c1b258ffc4 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> dab7af79b2 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e70434a447 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 9af2478db1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 1306fa28a0 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 2f9b4a6e73 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3ef949b911 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> ab354ae66a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 53865df964 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 8bfd50f462 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 33f2655b34 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a6287b7801 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 122aa064f5 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> bc42470098 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5844bf14a6 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3b8c627dda (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 43c1641739 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 7a9bff206b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 674042b19b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 2c11751de0 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> f77988fa9b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 851366e8db (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> ef05990d3a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 8ef5c8e5e3 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> bca28e773e (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b2c5a2ad2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 5b2a09c6ef (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 478eacddcd (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5202d5f7da (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
>>>>>>> 53cfc6049b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b1985ef3ca (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> db9ea57391 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5806596b34 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 140d339c38 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> ebd08a840c (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a2285639e2 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> da1f354017 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> d4879ffd54 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 47ada2c507 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> eec6e0dfee (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 16e0f7fc96 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
>>>>>>> a2285639e2 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e8925c7df7 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 74ab7a866e (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 9400969c2f (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> c1b258ffc4 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> edc424b09b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e70434a447 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 82881aaaec (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 1306fa28a0 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> a3706b16a1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3ef949b911 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> c1a5635118 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 53865df964 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> cd0e4defc1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 33f2655b34 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 8e791e0ba5 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 122aa064f5 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 21a0d24296 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5844bf14a6 (g.proj: fix reading input WKT (#1582))
=======
=======
<<<<<<< HEAD
>>>>>>> 8271eeb64f (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 43c1641739 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 79d87b3f39 (g.proj: fix reading input WKT (#1582))
>>>>>>> d4879ffd54 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 674042b19b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 7d640949f0 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> f77988fa9b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5336d0cf12 (g.proj: fix reading input WKT (#1582))
>>>>>>> ef05990d3a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6a06d2e78c (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> f92b908048 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
>>>>>>> 284a65cbb8 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
>>>>>>> fab41f991b (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 5b2a09c6ef (g.proj: fix reading input WKT (#1582))
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
=======
        size_t wktlen;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
        size_t wktlen;

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
>>>>>>> main
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
=======
>>>>>>> osgeo-main
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
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
        size_t wktlen;

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
        size_t wktlen;

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
        wktlen = fread(buff, 1, sizeof(buff), infd);
        if (wktlen == sizeof(buff))
            G_fatal_error(_("Input WKT definition is too long"));
        if (ferror(infd))
            G_fatal_error(_("Error reading WKT definition"));
        else
            fclose(infd);
        /* terminate WKT string */
        buff[wktlen] = '\0';
        /* Get rid of newlines */
        G_squeeze(buff);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
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
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 53cfc6049b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 89f6fd2f96 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3b2c5a2ad2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 478eacddcd (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> db9ea57391 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 140d339c38 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 16e0f7fc96 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e8925c7df7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 74ab7a866e (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> c1b258ffc4 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> e70434a447 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 1306fa28a0 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 3ef949b911 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 53865df964 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 33f2655b34 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 122aa064f5 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5844bf14a6 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 43c1641739 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 674042b19b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> f77988fa9b (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> ef05990d3a (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> eec6e0dfee (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> a2285639e2 (g.proj: fix reading input WKT (#1582))
>>>>>>> osgeo-main
>>>>>>> 53cfc6049b (g.proj: fix reading input WKT (#1582))
>>>>>>> b1985ef3ca (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d4879ffd54 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 284a65cbb8 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> fab41f991b (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 47ada2c507 (g.proj: fix reading input WKT (#1582))
=======
<<<<<<< HEAD
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
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
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 79d87b3f39 (g.proj: fix reading input WKT (#1582))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cdb769bc1e (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 5ec354b4a4 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65f70a77ac (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 89f6fd2f96 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 0338dc8268 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ffbd80b751 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3b2c5a2ad2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> de8a1fa341 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5b2a09c6ef (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 478eacddcd (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> osgeo-main
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5202d5f7da (g.proj: fix reading input WKT (#1582))
=======
=======
<<<<<<< HEAD
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
>>>>>>> 53cfc6049b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b1985ef3ca (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a2cb48f6 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 250c6900d1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> db9ea57391 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 42533ebf37 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 46c77518c7 (g.proj: fix reading input WKT (#1582))
=======
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5806596b34 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 140d339c38 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> be93d1fccc (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e2ac90a444 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 59def94d1b (g.proj: fix reading input WKT (#1582))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 47ada2c507 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> eec6e0dfee (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 16e0f7fc96 (g.proj: fix reading input WKT (#1582))
=======
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ebd08a840c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 769ad64a54 (g.proj: fix reading input WKT (#1582))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
>>>>>>> a2285639e2 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e8925c7df7 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> d752fc407c (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 56bc21b402 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95f198e1e0 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 74ab7a866e (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 573458c7fe (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e1642feb6f (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9400969c2f (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> c1b258ffc4 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 0d53ace193 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> dab7af79b2 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> edc424b09b (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> e70434a447 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 9a000933e9 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 9af2478db1 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82881aaaec (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 1306fa28a0 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> dc8b886312 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 2f9b4a6e73 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3706b16a1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3ef949b911 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 460748a7fb (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> ab354ae66a (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c1a5635118 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 53865df964 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> a97572757d (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 8bfd50f462 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cd0e4defc1 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 33f2655b34 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 6307e79ee9 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> a6287b7801 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8e791e0ba5 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 122aa064f5 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> c585c92c1e (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> bc42470098 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 21a0d24296 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 5844bf14a6 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 76ed571f8d (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 3b8c627dda (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8271eeb64f (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 43c1641739 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 24abee9ad6 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> da1f354017 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 7a9bff206b (g.proj: fix reading input WKT (#1582))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 79d87b3f39 (g.proj: fix reading input WKT (#1582))
>>>>>>> d4879ffd54 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 674042b19b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 1411c71e15 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 2c11751de0 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7d640949f0 (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> f77988fa9b (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> dbe7a0c10a (g.proj: fix reading input WKT (#1582))
<<<<<<< HEAD
>>>>>>> 851366e8db (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5336d0cf12 (g.proj: fix reading input WKT (#1582))
>>>>>>> ef05990d3a (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c10386e82 (g.proj: fix reading input WKT (#1582))
>>>>>>> 7e7871fd90 (g.proj: fix reading input WKT (#1582))
>>>>>>> 6a06d2e78c (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 5ec354b4a4 (g.proj: fix reading input WKT (#1582))
>>>>>>> f92b908048 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e56c7523eb (g.proj: fix reading input WKT (#1582))
>>>>>>> 284a65cbb8 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 0338dc8268 (g.proj: fix reading input WKT (#1582))
>>>>>>> cfd6be023a (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a61698b913 (g.proj: fix reading input WKT (#1582))
>>>>>>> fab41f991b (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> d3904a14b8 (g.proj: fix reading input WKT (#1582))
>>>>>>> 8ef5c8e5e3 (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5b2a09c6ef (g.proj: fix reading input WKT (#1582))
>>>>>>> a9a25aa0c7 (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 5f176f4600 (g.proj: fix reading input WKT (#1582))
>>>>>>> 95b6e0779d (g.proj: fix reading input WKT (#1582))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3a4a5ec94f (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> b3579a4902 (g.proj: fix reading input WKT (#1582))
>>>>>>> 398a3c2388 (g.proj: fix reading input WKT (#1582))
>>>>>>> bca28e773e (g.proj: fix reading input WKT (#1582))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
    }
    else
        G_fatal_error(_("Unable to open file '%s' for reading"), wktfile);

    projwkt = G_store(buff);

#if PROJ_VERSION_MAJOR >= 6
    /* validate input WKT */
    {
        PROJ_STRING_LIST wkt_warnings, wkt_grammar_errors;
        PJ *obj;

        wkt_warnings = NULL;
        wkt_grammar_errors = NULL;

        /* no strict validation */
        obj = proj_create_from_wkt(NULL, buff, NULL, &wkt_warnings,
                                   &wkt_grammar_errors);

        if (wkt_warnings) {
            int i;

            G_warning(_("WKT validation warnings:"));
            for (i = 0; wkt_warnings[i]; i++)
                G_warning("%s", wkt_warnings[i]);

            proj_string_list_destroy(wkt_warnings);
        }

        if (wkt_grammar_errors) {
            int i;

            G_warning(_("WKT validation grammar errors:"));
            for (i = 0; wkt_grammar_errors[i]; i++)
                G_warning("%s", wkt_grammar_errors[i]);

            proj_string_list_destroy(wkt_grammar_errors);
        }
        proj_destroy(obj);
    }
#endif

    /* get GRASS proj info + units */
    /* NOTE: GPJ_wkt_to_grass() converts any WKT version to WKT1 */
    ret = GPJ_wkt_to_grass(&cellhd, &projinfo, &projunits, buff, 0);
    if (ret < 2)
        G_fatal_error(_("WKT not recognized: %s"), buff);

    set_default_region();

    /* find authname and authcode */
    hSRS = OSRNewSpatialReference(buff);
    /* get clean WKT definition */
#if GDAL_VERSION_MAJOR >= 3
    papszOptions[0] = G_store("MULTILINE=YES");
    papszOptions[1] = G_store("FORMAT=WKT2");
    papszOptions[2] = NULL;
    OSRExportToWktEx(hSRS, &tmpwkt, (const char **)papszOptions);
    G_free(papszOptions[0]);
    G_free(papszOptions[1]);
#else
    OSRExportToPrettyWkt(hSRS, &tmpwkt, FALSE);
#endif
    projwkt = G_store(tmpwkt);
    CPLFree(tmpwkt);
    set_authnamecode(hSRS);
    OSRDestroySpatialReference(hSRS);

    return ret;
}

/**
 * \brief Read projection information in PROJ.4 format from a string
 *        or stdin
 *
 * Reads projection information from a string or stdin and stores in global
 * structs projinfo and projunits.
 * Populates global cellhd with default region information.
 *
 * \param proj4params String representation of PROJ.4 co-ordinate system
 *                    description, or - to read it from stdin
 *
 * \return        2 if a projected or lat/long co-ordinate system has been
 *                defined; 1 if an unreferenced XY co-ordinate system has
 *                been defined
 **/

int input_proj4(char *proj4params)
{
    FILE *infd;
    char buff[8000];
    char *proj4string;
    OGRSpatialReferenceH hSRS;
    int ret = 0;

    /* TEST: use PROJ proj_create(), convert to WKT,
     *       OSRImportFromWkt  */
    if (strcmp(proj4params, "-") == 0) {
        infd = stdin;
        if (fgets(buff, sizeof(buff), infd) == NULL)
            G_warning(_("Failed to read PROJ.4 parameter from stdin"));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    }
    else {
        if (G_strlcpy(buff, proj4params, sizeof(buff)) >= sizeof(buff)) {
            G_fatal_error(_("PROJ.4 parameter string is too long: %s"),
                          proj4params);
        }
    }
=======
    }
    else
        strcpy(buff, proj4params);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    }
    else
        strcpy(buff, proj4params);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

#if PROJ_VERSION_MAJOR >= 6
    if (!strstr(buff, "+type=crs"))
        G_asprintf(&proj4string, "%s +no_defs +type=crs", buff);
    else
        G_asprintf(&proj4string, "%s +no_defs", buff);
#else
    G_asprintf(&proj4string, "%s +no_defs", buff);
#endif

    /* Set finder function for locating OGR csv co-ordinate system tables */
    /* SetCSVFilenameHook(GPJ_set_csv_loc); */

    hSRS = OSRNewSpatialReference(NULL);
    if (OSRImportFromProj4(hSRS, proj4string) != OGRERR_NONE)
        G_fatal_error(_("Can't parse PROJ.4-style parameter string"));

    G_free(proj4string);

    ret = GPJ_osr_to_grass(&cellhd, &projinfo, &projunits, hSRS, 0);

    /* authority name and code not available in PROJ definitions */

    OSRDestroySpatialReference(hSRS);

    set_default_region();

    return ret;
}

/**
 * \brief Read projection information corresponding to a spatial
 *        reference id (srid)
 *
 * Determines projection information corresponding to a srid
 * composed of authority name and code and stores in global structs
 * projinfo and projunits. Populates global cellhd with default region
 * information.
 *
 * Examples: "EPSG:4326", "urn:ogc:def:crs:EPSG::4326"
 *
 * \param srid    spatial reference id
 *
 * \return        2 if a projected or lat/long co-ordinate system has been
 *                defined; 1 if an unreferenced XY co-ordinate system has
 *                been defined
 **/

int input_srid(char *srid)
{
#if PROJ_VERSION_MAJOR >= 6
    OGRSpatialReferenceH hSRS;
    int ret = 0;
    char *papszOptions[3];
    PJ *obj;
    const char *tmpwkt;

    /* GDAL alternative: OSRSetFromUserInput() */
    obj = proj_create(NULL, srid);
    if (!obj)
        G_fatal_error(_("SRID <%s> not recognized by PROJ"), srid);

    tmpwkt = proj_as_wkt(NULL, obj, PJ_WKT2_LATEST, NULL);
    hSRS = OSRNewSpatialReference(tmpwkt);
    if (!hSRS)
        G_fatal_error(_("WKT for SRID <%s> not recognized by GDAL"), srid);

    projsrid = G_store(srid);

    /* WKT */
    papszOptions[0] = G_store("MULTILINE=YES");
    papszOptions[1] = G_store("FORMAT=WKT2");
    papszOptions[2] = NULL;
    if (OSRExportToWktEx(hSRS, &projwkt, (const char **)papszOptions) !=
        OGRERR_NONE)
        G_warning(_("Unable to convert srid to WKT"));
    G_free(papszOptions[0]);
    G_free(papszOptions[1]);
    /* GRASS proj info + units */
    ret = GPJ_osr_to_grass(&cellhd, &projinfo, &projunits, hSRS, 0);

    proj_destroy(obj);
    OSRDestroySpatialReference(hSRS);

    set_default_region();
    return ret;
#else
    G_fatal_error(_("Input srid requires GDAL 3+ and PROJ 6+"));

    return 0;
#endif
}

/**
 * \brief Read projection information corresponding to an EPSG co-ordinate
 *        system number
 *
 * Determines projection information corresponding to an EPSG co-ordinate
 * system number and stores in global structs projinfo and projunits.
 * Populates global cellhd with default region information.
 *
 * \param epsg_num    EPSG number for co-ordinate system
 *
 * \return        2 if a projected or lat/long co-ordinate system has been
 *                defined; 1 if an unreferenced XY co-ordinate system has
 *                been defined
 **/

int input_epsg(int epsg_num)
{
    OGRSpatialReferenceH hSRS;
    char epsgstr[100];
    int ret = 0;
    char *papszOptions[3];

    /* Set finder function for locating OGR csv co-ordinate system tables */
    /* SetCSVFilenameHook(GPJ_set_csv_loc); */

    hSRS = OSRNewSpatialReference(NULL);
    if (OSRImportFromEPSG(hSRS, epsg_num) != OGRERR_NONE)
        G_fatal_error(_("Unable to translate EPSG code"));

    /* GRASS proj info + units */
    ret = GPJ_osr_to_grass(&cellhd, &projinfo, &projunits, hSRS, 0);

    /* EPSG code */
    sprintf(epsgstr, "%d", epsg_num);
    projepsg = G_create_key_value();
    G_set_key_value("epsg", epsgstr, projepsg);
    /* srid as AUTHORITY:CODE */
    G_asprintf(&projsrid, "EPSG:%s", epsgstr);

#if GDAL_VERSION_MAJOR >= 3
    /* WKT */
    papszOptions[0] = G_store("MULTILINE=YES");
    papszOptions[1] = G_store("FORMAT=WKT2");
    papszOptions[2] = NULL;
    if (OSRExportToWktEx(hSRS, &projwkt, (const char **)papszOptions) !=
        OGRERR_NONE)
        G_warning(_("Unable to convert EPSG code to WKT"));

    G_free(papszOptions[0]);
    G_free(papszOptions[1]);
#endif

    OSRDestroySpatialReference(hSRS);

    set_default_region();

    return ret;
}

/**
 * \brief Read projection and region information associated with a
 *        georeferenced file
 *
 * Reads projection information associated with a georeferenced file, if
 * available. Attempts are made to open the file with OGR and GDAL in turn.
 * (GDAL conventionally supports raster formats, and OGR vector formats.)
 *
 * If successful, projection and region information are read from the file
 * using GDAL/OGR functions and stored in global structs cellhd, projinfo
 * and projunits.
 *
 * \param geofile Path to georeferenced file
 *
 * \return        2 if a projected or lat/long co-ordinate system has been
 *                defined; 1 if an unreferenced XY co-ordinate system has
 *                been defined
 **/

int input_georef(char *geofile)
{
    /* GDAL >= 3 */
#if GDAL_VERSION_MAJOR >= 3
    GDALDatasetH hDS = NULL;
    OGRSpatialReferenceH hSRS = NULL;
    int ret = 0;

    GDALAllRegister();

    /* Try opening file as vector first because it doesn't output a
     * (potentially confusing) error message if it can't open the file */

    /* Try opening as vector */
    G_debug(1, "Trying to open <%s> as vector...", geofile);
    if ((hDS = GDALOpenEx(geofile, GDAL_OF_VECTOR, NULL, NULL, NULL)) &&
        GDALDatasetGetLayerCount(hDS) > 0) {

        OGRLayerH ogr_layer;

        ogr_layer = GDALDatasetGetLayer(hDS, 0);
        hSRS = OGR_L_GetSpatialRef(ogr_layer);

        if (hSRS)
            set_default_region();
    }
    else {
        /* Try opening as raster */
        G_debug(1, "Trying to open <%s> as raster...", geofile);

        if ((hDS = GDALOpen(geofile, GA_ReadOnly))) {
            char **sds;

            /* does the dataset include subdatasets? */
            sds = GDALGetMetadata(hDS, "SUBDATASETS");
            if (sds && *sds) {
                G_warning(_("Input dataset <%s> contains subdatasets. "
                            "Please select a subdataset."),
                          geofile);
            }
            else {
                hSRS = GDALGetSpatialRef(hDS);

                if (hSRS)
                    set_gdal_region(hDS);
            }
        }
        else {
            int namelen;

            namelen = strlen(geofile);
            if (namelen > 4 &&
                G_strcasecmp(geofile + (namelen - 4), ".prj") == 0) {
                G_warning(_("<%s> is not a GDAL dataset, trying to open it as "
                            "ESRI WKT"),
                          geofile);

                return input_wkt(geofile);
            }
            else {
                G_fatal_error(_("Unable to read georeferenced file <%s> using "
                                "GDAL library"),
                              geofile);
            }
        }
    }
    if (hSRS) {
        char **papszOptions = NULL;

        ret = GPJ_osr_to_grass(&cellhd, &projinfo, &projunits, hSRS, 0);

        if (cellhd.proj == PROJECTION_XY)
            G_warning(
                _("Read of file %s was successful, but it did not contain "
                  "projection information. 'XY (unprojected)' will be used"),
                geofile);

        papszOptions = G_calloc(3, sizeof(char *));
        papszOptions[0] = G_store("MULTILINE=YES");
        papszOptions[1] = G_store("FORMAT=WKT2");
        OSRExportToWktEx(hSRS, &projwkt, (const char **)papszOptions);
        G_free(papszOptions[0]);
        G_free(papszOptions[1]);
        G_free(papszOptions);

        set_authnamecode(hSRS);
    }
    if (hDS)
        GDALClose(hDS);

    return ret;

    /* GDAL < 3 */
#else
    OGRDataSourceH ogr_ds;
    OGRSpatialReferenceH hSRS;
    int ret = 0;

    /* Try opening file with OGR first because it doesn't output a
     * (potentially confusing) error message if it can't open the file */
    G_debug(1, "Trying to open <%s> with OGR...", geofile);
    OGRRegisterAll();

    ogr_ds = NULL;
    hSRS = NULL;
    /* Try opening with OGR */
    if ((ogr_ds = OGROpen(geofile, FALSE, NULL)) &&
        (OGR_DS_GetLayerCount(ogr_ds) > 0)) {
        OGRLayerH ogr_layer;

        G_debug(1, "...succeeded.");
        /* Get the first layer */
        ogr_layer = OGR_DS_GetLayer(ogr_ds, 0);
        hSRS = OGR_L_GetSpatialRef(ogr_layer);
        ret = GPJ_osr_to_grass(&cellhd, &projinfo, &projunits, hSRS, 0);
        OSRExportToWkt(hSRS, &projwkt);
        set_default_region();
    }
    else {
        /* Try opening with GDAL */
        GDALDatasetH gdal_ds;

        G_debug(1, "Trying to open with GDAL...");
        GDALAllRegister();

        if ((gdal_ds = GDALOpen(geofile, GA_ReadOnly))) {
            char *wktstring;

            G_debug(1, "...succeeded.");
            /* TODO: change for GDAL 3+ */
            wktstring = (char *)GDALGetProjectionRef(gdal_ds);
            projwkt = G_store(wktstring);
            ret = GPJ_wkt_to_grass(&cellhd, &projinfo, &projunits, projwkt, 0);

            set_gdal_region(gdal_ds);
            hSRS = OSRNewSpatialReference(projwkt);
            GDALClose(gdal_ds);
        }
        else {
            int namelen;

            namelen = strlen(geofile);
            if (namelen > 4 &&
                G_strcasecmp(geofile + (namelen - 4), ".prj") == 0) {
                G_warning(_("<%s> is not a GDAL dataset, trying to open it as "
                            "ESRI WKT"),
                          geofile);

                return input_wkt(geofile);
            }
            else {
                G_fatal_error(_("Unable to read georeferenced file <%s> using "
                                "GDAL library"),
                              geofile);
            }
        }
    }

    if (cellhd.proj == PROJECTION_XY)
        G_warning(_("Read of file %s was successful, but it did not contain "
                    "projection information. 'XY (unprojected)' will be used"),
                  geofile);

    set_authnamecode(hSRS);

    if (ogr_ds)
        OGR_DS_Destroy(ogr_ds);
    else
        OSRDestroySpatialReference(hSRS);

    return ret;
#endif
}

/**
 * \brief Populates global cellhd with region settings based on
 *        georeferencing information in a GDAL dataset
 *
 * \param hDS GDAL dataset object to retrieve georeferencing information from
 **/

static void set_gdal_region(GDALDatasetH hDS)
{
    double adfGeoTransform[6];

    /* Populate with initial values in case we can't set everything */
    set_default_region();

    /* Code below originally from r.in.gdal */
    cellhd.rows = GDALGetRasterYSize(hDS);
    cellhd.cols = GDALGetRasterXSize(hDS);

    cellhd.rows3 = cellhd.rows;
    cellhd.cols3 = cellhd.cols;

    if (GDALGetGeoTransform(hDS, adfGeoTransform) == CE_None &&
        adfGeoTransform[5] < 0.0) {
        if (adfGeoTransform[2] != 0.0 || adfGeoTransform[4] != 0.0) {
            /* Map is rotated. Calculation of north/south extents and
             * resolution more complicated.
             * TODO: do it anyway */

            return;
        }

        cellhd.north = adfGeoTransform[3];
        cellhd.ns_res = fabs(adfGeoTransform[5]);
        cellhd.south = cellhd.north - cellhd.ns_res * cellhd.rows;
        cellhd.west = adfGeoTransform[0];
        cellhd.ew_res = adfGeoTransform[1];
        cellhd.east = cellhd.west + cellhd.cols * cellhd.ew_res;

        cellhd.ns_res3 = cellhd.ns_res;
        cellhd.ew_res3 = cellhd.ew_res;
    }
    else {
        cellhd.north = cellhd.rows;
        cellhd.east = cellhd.cols;
    }

    return;
}

void set_authnamecode(OGRSpatialReferenceH hSRS)
{
    const char *authkey, *authname, *authcode;

    if (!hSRS)
        return;

    authkey = NULL;
    if (OSRIsProjected(hSRS))
        authkey = "PROJCS";
    else if (OSRIsGeographic(hSRS))
        authkey = "GEOGCS";

    if (authkey) {
        authname = OSRGetAuthorityName(hSRS, authkey);
        if (authname && *authname) {
            authcode = OSRGetAuthorityCode(hSRS, authkey);
            if (authcode && *authcode) {
                G_asprintf(&projsrid, "%s:%s", authname, authcode);
                /* for backwards compatibility; remove ? */
                if (strcmp(authname, "EPSG") == 0) {
                    projepsg = G_create_key_value();
                    G_set_key_value("epsg", authcode, projepsg);
                }
            }
        }
    }
}

#endif /* HAVE_OGR */
