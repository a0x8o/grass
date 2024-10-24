/*!
   \file lib/pngdriver/draw_bitmap.c

   \brief GRASS png display driver - draw bitmap

   (C) 2003-2014 by Per Henrik Johansen and the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Per Henrik Johansen (original contributor)
   \author Glynn Clements
 */

#include <math.h>
#include "pngdriver.h"

#ifndef min
#define min(a, b) ((a) < (b) ? (a) : (b))
#endif
#ifndef max
#define max(a, b) ((a) > (b) ? (a) : (b))
#endif

/*!
   \brief Draw bitmap

   \param ncols,nrows number of columns and rows
   \param threshold threshold value
   \param buf data buffer
 */

void PNG_draw_bitmap(int ncols, int nrows, int threshold,
                     const unsigned char *buf)
{
    int i0 = max(png.clip_left - cur_x, 0);
    int i1 = min(png.clip_rite - cur_x, ncols);
    int j0 = max(png.clip_top - cur_y, 0);
    int j1 = min(png.clip_bot - cur_y, nrows);

    if (!png.true_color) {
        int i, j;

        for (j = j0; j < j1; j++) {
            int y = cur_y + j;

            for (i = i0; i < i1; i++) {
                int x = cur_x + i;
                unsigned int k = buf[j * ncols + i];
                unsigned int *p = &png.grid[y * png.width + x];

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                if (k > (unsigned int)threshold)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                if (k > (unsigned int)threshold)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
=======
                if (k > (unsigned int)threshold)
=======
>>>>>>> osgeo-main
                if (k > threshold)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                if (k > threshold)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                if (k > (unsigned int)threshold)
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
                if (k > threshold)
=======
                if (k > (unsigned int)threshold)
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
                if (k > (unsigned int)threshold)
=======
                if (k > threshold)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                if (k > threshold)
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
                if (k > (unsigned int)threshold)
=======
                if (k > threshold)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                if (k > threshold)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
                if (k > (unsigned int)threshold)
=======
                if (k > threshold)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                if (k > threshold)
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
                    *p = png.current_color;
            }
        }
    }
    else {
        int r1, g1, b1, a1;
        int i, j;

        png_get_pixel(png.current_color, &r1, &g1, &b1, &a1);

        for (j = j0; j < j1; j++) {
            int y = cur_y + j;

            for (i = i0; i < i1; i++) {
                int x = cur_x + i;
                unsigned int k = buf[j * ncols + i];
                unsigned int *p = &png.grid[y * png.width + x];
                int a0, r0, g0, b0;
                unsigned int a, r, g, b;

                png_get_pixel(*p, &r0, &g0, &b0, &a0);

                a = (a0 * (255 - k) + a1 * k) / 255;
                r = (r0 * (255 - k) + r1 * k) / 255;
                g = (g0 * (255 - k) + g1 * k) / 255;
                b = (b0 * (255 - k) + b1 * k) / 255;

                *p = png_get_color(r, g, b, a);
            }
        }
    }

    png.modified = 1;
}
