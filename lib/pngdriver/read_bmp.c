/*!
   \file lib/pngdriver/read_bmp.c

   \brief GRASS png display driver - read bitmap (lower level functions)

   (C) 2007-2014 by Glynn Clements and the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Glynn Clements
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <grass/gis.h>
#include "pngdriver.h"

static unsigned int get_2(const unsigned char **q)
{
    const unsigned char *p = *q;
    unsigned int n = (p[0] << 0) | (p[1] << 8);

    *q += 2;
    return n;
}

static unsigned int get_4(const unsigned char **q)
{
    const unsigned char *p = *q;
    unsigned int n = (p[0] << 0) | (p[1] << 8) | (p[2] << 16) | (p[3] << 24);

    *q += 4;
    return n;
}

static int read_bmp_header(const unsigned char *p)
{
    if (*p++ != 'B')
        return 0;
    if (*p++ != 'M')
        return 0;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
>>>>>>> osgeo-main
    if (get_4(&p) != HEADER_SIZE + png.width * png.height * 4)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
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
    if (get_4(&p) != HEADER_SIZE + png.width * png.height * 4)
=======
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
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
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
    if (get_4(&p) != HEADER_SIZE + png.width * png.height * 4)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
    if (get_4(&p) != HEADER_SIZE + png.width * png.height * 4)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    if (get_4(&p) != (unsigned int)HEADER_SIZE + png.width * png.height * 4)
=======
    if (get_4(&p) != HEADER_SIZE + png.width * png.height * 4)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
        return 0;

    get_4(&p);

    if (get_4(&p) != HEADER_SIZE)
        return 0;

    if (get_4(&p) != 40)
        return 0;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
    if (get_4(&p) != (unsigned int)png.width)
        return 0;
    if (get_4(&p) != (unsigned int)-png.height)
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
=======
<<<<<<< HEAD
>>>>>>> main
    if (get_4(&p) != (unsigned int)png.width)
        return 0;
    if (get_4(&p) != (unsigned int)-png.height)
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    if (get_4(&p) != png.width)
        return 0;
    if (get_4(&p) != -png.height)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    if (get_4(&p) != png.width)
        return 0;
    if (get_4(&p) != -png.height)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> osgeo-main
    if (get_4(&p) != (unsigned int)png.width)
        return 0;
    if (get_4(&p) != (unsigned int)-png.height)
<<<<<<< HEAD
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
=======
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != png.width)
        return 0;
    if (get_4(&p) != -png.height)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
    if (get_4(&p) != (unsigned int)png.width)
        return 0;
    if (get_4(&p) != (unsigned int)-png.height)
<<<<<<< HEAD
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != png.width)
        return 0;
    if (get_4(&p) != -png.height)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
    if (get_4(&p) != (unsigned int)png.width)
        return 0;
    if (get_4(&p) != (unsigned int)-png.height)
<<<<<<< HEAD
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    if (get_4(&p) != png.width)
        return 0;
    if (get_4(&p) != -png.height)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    if (get_4(&p) != (unsigned int)png.width)
        return 0;
    if (get_4(&p) != (unsigned int)-png.height)
<<<<<<< HEAD
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
        return 0;

    get_2(&p);
    if (get_2(&p) != 32)
        return 0;

    if (get_4(&p) != 0)
        return 0;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
>>>>>>> osgeo-main
    if (get_4(&p) != png.width * png.height * 4)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    if (get_4(&p) != png.width * png.height * 4)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
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
    if (get_4(&p) != png.width * png.height * 4)
=======
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
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
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
    if (get_4(&p) != png.width * png.height * 4)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (get_4(&p) != png.width * png.height * 4)
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
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
    if (get_4(&p) != png.width * png.height * 4)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (get_4(&p) != png.width * png.height * 4)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    if (get_4(&p) != (unsigned int)png.width * png.height * 4)
=======
    if (get_4(&p) != png.width * png.height * 4)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    if (get_4(&p) != png.width * png.height * 4)
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
        return 0;

    get_4(&p);
    get_4(&p);
    get_4(&p);
    get_4(&p);

    return 1;
}

void read_bmp(void)
{
    unsigned char header[HEADER_SIZE];
    FILE *input;
    int x, y;
    unsigned int *p;

    if (!png.true_color)
        G_fatal_error("PNG: cannot use BMP with indexed color");

    input = fopen(png.file_name, "rb");
    if (!input)
        G_fatal_error("PNG: couldn't open input file %s", png.file_name);

    if (fread(header, sizeof(header), 1, input) != 1)
        G_fatal_error("PNG: invalid input file %s", png.file_name);

    if (!read_bmp_header(header))
        G_fatal_error("PNG: invalid BMP header for %s", png.file_name);

    for (y = 0, p = png.grid; y < png.height; y++) {
        for (x = 0; x < png.width; x++, p++) {
            int b = fgetc(input);
            int g = fgetc(input);
            int r = fgetc(input);
            int a = fgetc(input);
            unsigned int c = png_get_color(r, g, b, a);

            *p = c;
        }
    }

    fclose(input);
}
