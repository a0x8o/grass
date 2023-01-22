/*!
   \file lib/ogsf/gsd_wire.c

   \brief OGSF library -

   GRASS OpenGL gsurf OGSF Library

   (C) 1999-2008 by the GRASS Development Team

   This program is free software under the
   GNU General Public License (>=v2).
   Read the file COPYING that comes with GRASS
   for details.

   \author Bill Brown USACERL (January 1993)
   \author Doxygenized by Martin Landa <landa.martin gmail.com> (May 2008)
 */

#include <grass/gis.h>
#include <grass/ogsf.h>

#include "gsget.h"
#include "rowcol.h"

#define DO_ARROWS

/************************************************************************/
/* Notes on exageration:
   vertical exageration is of two forms:
   1) global exageration (from geoview struct)
   2) vertical exageration for each surface - not implemented
 */

/************************************************************************/
/* may need to add more parameters to tell it which window or off_screen
 * pixmap to draw into. nah - just have one current (OpenGL limitation)
 */

/*!
   \brief Draw surface wire

   \param surf surface (geosurf)

   \return
 */
int gsd_wire_surf(geosurf *surf)
{
    int desc, ret;

    G_debug(3, "gsd_wire_surf(): id=%d", surf->gsurf_id);

    desc = ATT_TOPO;

    switch (gs_get_att_src(surf, desc)) {
    case NOTSET_ATT:
        ret = (-1);

        break;

    case MAP_ATT:
        if (surf->draw_mode & DM_GRID_WIRE)
            ret = (gsd_wire_surf_map(surf)); /* draw mesh */
        else
            ret = (gsd_coarse_surf_map(surf)); /* draw coarse surf */

#ifdef DO_ARROWS
            /*
               gsd_wire_arrows(surf);
             */
#endif

        break;

    case CONST_ATT:
        ret = (gsd_wire_surf_const(surf, surf->att[desc].constant));
        break;

    case FUNC_ATT:
        ret = (gsd_wire_surf_func(surf, surf->att[desc].user_func));

        break;

    default:
        ret = (-1);

        break;
    }

    return (ret);
}

/*!
   \brief ADD

   \param surf surface (geosurf)

   \return
 */
int gsd_wire_surf_map(geosurf *surf)
{
    int check_mask, check_color;
    typbuff *buff, *cobuff;
    int xmod, ymod, row, col, cnt, xcnt, ycnt, x1off;
    long offset, y1off;
    float pt[4], xres, yres, ymax, zexag;
    int col_src, curcolor;
    gsurf_att *coloratt;

    G_debug(3, "gsd_wire_surf_map");

    buff = gs_get_att_typbuff(surf, ATT_TOPO, 0);
    cobuff = gs_get_att_typbuff(surf, ATT_COLOR, 0);

    gs_update_curmask(surf);
    check_mask = surf->curmask ? 1 : 0;

    /*
       checks ATT_TOPO & ATT_COLOR no_zero flags, make a mask from each,
       combine it/them with any current mask, put in typbuff:
       if(surf->att[ATT_TOPO].constant)
     */

    xmod = surf->x_modw;
    ymod = surf->y_modw;
    xres = xmod * surf->xres;
    yres = ymod * surf->yres;
    ymax = (surf->rows - 1) * surf->yres;
    xcnt = 1 + (surf->cols - 1) / xmod;
    ycnt = 1 + (surf->rows - 1) / ymod;

    gsd_pushmatrix();
    gsd_do_scale(1);
    gsd_translate(surf->x_trans, surf->y_trans, surf->z_trans);

    zexag = surf->z_exag;

    gsd_colormode(CM_COLOR);

    /* will need to check for color source of FUNC_ATT & NOTSET_ATT,
       or else use more general and inefficient gets */

    check_color = (surf->wire_color == WC_COLOR_ATT);

    if (check_color) {
        coloratt = &(surf->att[ATT_COLOR]);
        col_src = surf->att[ATT_COLOR].att_src;

        if (col_src != MAP_ATT) {
            if (col_src == CONST_ATT) {
                gsd_color_func((int)surf->att[ATT_COLOR].constant);
            }
            else {
                gsd_color_func(surf->wire_color);
            }

            check_color = 0;
        }
    }
    else {
        gsd_color_func(surf->wire_color);
    }

    /* would also be good to check if colormap == surfmap, to increase speed */
    for (row = 0; row < ycnt; row++) {
        pt[Y] = ymax - row * yres;
        y1off = row * ymod * surf->cols;

        gsd_bgnline();
        cnt = 0;

        for (col = 0; col < xcnt; col++) {
            pt[X] = col * xres;
            x1off = col * xmod;
            offset = x1off + y1off;

            if (check_mask) {
                if (BM_get(surf->curmask, col * xmod, row * ymod)) {
                    gsd_endline();
                    gsd_bgnline();
                    cnt = 0;
                    continue;
                }
            }

            GET_MAPATT(buff, offset, pt[Z]);

            if (check_color) {
                curcolor = gs_mapcolor(cobuff, coloratt, offset);
                gsd_color_func(curcolor);
                /* could use this & skip the GET if colordata == elevdata
                   gsd_color_func(gs_fastmapcolor(cobuff, coloratt, offset,
                   (int)pt[Z]));
                 */
            }

            pt[Z] = pt[Z] * zexag;

            gsd_vert_func(pt);

            if (cnt == 255) {
                gsd_endline();
                gsd_bgnline();
                cnt = 0;
                gsd_vert_func(pt);
            }

            cnt++;
        }

        gsd_endline();
    }

    for (col = 0; col < xcnt; col++) {
        pt[X] = col * xres;
        x1off = col * xmod;

        gsd_bgnline();
        cnt = 0;

        for (row = 0; row < ycnt; row++) {
            pt[Y] = ymax - row * yres;
            y1off = row * ymod * surf->cols;
            offset = x1off + y1off;

            if (check_mask) {
                if (BM_get(surf->curmask, col * xmod, row * ymod)) {
                    gsd_endline();
                    gsd_bgnline();
                    cnt = 0;
                    continue;
                }
            }

            GET_MAPATT(buff, offset, pt[Z]);

            if (check_color) {
                curcolor = gs_mapcolor(cobuff, coloratt, offset);
                gsd_color_func(curcolor);
                /* could use this & skip the GET if colordata == elevdata
                   gsd_color_func(gs_fastmapcolor(coloratt, offset,
                   (int)pt[Z]));
                 */
            }

            pt[Z] = pt[Z] * zexag;

            gsd_vert_func(pt);

            if (cnt == 255) {
                gsd_endline();
                gsd_bgnline();
                cnt = 0;
                gsd_vert_func(pt);
            }

            cnt++;
        }

        gsd_endline();
    }

    gsd_popmatrix();
    gsd_colormode(CM_DIFFUSE);

    return (1);
}

/*!
   \brief ADD

   \param surf surface (geosurf)
   \param k

   \return
 */
int gsd_wire_surf_const(geosurf *surf, float k)
{
    int do_diff, check_mask, check_color;
    int xmod, ymod, row, col, cnt, xcnt, ycnt, x1off;
    long offset, y1off;
    float pt[4], xres, yres, ymax, zexag;
    int col_src;
    gsurf_att *coloratt;
    typbuff *cobuff;

    G_debug(3, "gsd_wire_surf_const");

    cobuff = gs_get_att_typbuff(surf, ATT_COLOR, 0);

    gs_update_curmask(surf);
    check_mask = surf->curmask ? 1 : 0;

    do_diff = (NULL != gsdiff_get_SDref());

    xmod = surf->x_modw;
    ymod = surf->y_modw;
    xres = xmod * surf->xres;
    yres = ymod * surf->yres;

    xcnt = 1 + (surf->cols - 1) / xmod;
    ycnt = 1 + (surf->rows - 1) / ymod;
    ymax = (surf->rows - 1) * surf->yres;

    gsd_pushmatrix();
    gsd_do_scale(1);
    gsd_translate(surf->x_trans, surf->y_trans, surf->z_trans);

    zexag = surf->z_exag;

    gsd_colormode(CM_COLOR);

    /* will need to check for color source of FUNC_ATT & NOTSET_ATT,
       or else use more general and inefficient gets */

    check_color = (surf->wire_color == WC_COLOR_ATT);

    if (check_color) {
        coloratt = &(surf->att[ATT_COLOR]);
        col_src = surf->att[ATT_COLOR].att_src;

        if (col_src != MAP_ATT) {
            if (col_src == CONST_ATT) {
                gsd_color_func((int)surf->att[ATT_COLOR].constant);
            }
            else {
                gsd_color_func(surf->wire_color);
            }

            check_color = 0;
        }
    }
    else {
        gsd_color_func(surf->wire_color);
    }

    pt[Z] = k * zexag;

    for (row = 0; row < ycnt; row++) {
        pt[Y] = ymax - row * yres;
        y1off = row * ymod * surf->cols;

        gsd_bgnline();
        cnt = 0;

        for (col = 0; col < xcnt; col++) {
            pt[X] = col * xres;
            x1off = col * xmod;
            offset = x1off + y1off;

            if (check_mask) {
                if (BM_get(surf->curmask, col * xmod, row * ymod)) {
                    gsd_endline();
                    gsd_bgnline();
                    cnt = 0;
                    continue;
                }
            }

            if (check_color) {
                gsd_color_func(gs_mapcolor(cobuff, coloratt, offset));
            }

            if (do_diff) {
                pt[Z] = gsdiff_do_SD(k * zexag, offset);
            }

            gsd_vert_func(pt);

            if (cnt == 255) {
                gsd_endline();
                gsd_bgnline();
                cnt = 0;
                gsd_vert_func(pt);
            }

            cnt++;
        }

        gsd_endline();
    }

    for (col = 0; col < xcnt; col++) {
        pt[X] = col * xres;
        x1off = col * xmod;

        gsd_bgnline();
        cnt = 0;

        for (row = 0; row < ycnt; row++) {
            pt[Y] = ymax - row * yres;
            y1off = row * ymod * surf->cols;
            offset = x1off + y1off;

            if (check_mask) {
                if (BM_get(surf->curmask, col * xmod, row * ymod)) {
                    gsd_endline();
                    gsd_bgnline();
                    cnt = 0;
                    continue;
                }
            }

            if (check_color) {
                gsd_color_func(gs_mapcolor(cobuff, coloratt, offset));
            }

            if (do_diff) {
                pt[Z] = gsdiff_do_SD(k * zexag, offset);
            }

            gsd_vert_func(pt);

            if (cnt == 255) {
                gsd_endline();
                gsd_bgnline();
                cnt = 0;
                gsd_vert_func(pt);
            }

            cnt++;
        }

        gsd_endline();
    }

    gsd_popmatrix();
    gsd_colormode(CM_DIFFUSE);

    return (1);
}

/*!
   \brief ADD

   Not yet implemented.

   \param gs surface (geosurf) [unused]
   \param user_func user defined function [unused]

   \return 1
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
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
int gsd_wire_surf_func(geosurf *gs, int (*user_func)(void))
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
=======
>>>>>>> main
int gsd_wire_surf_func(geosurf *gs, int (*user_func)(void))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
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
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
<<<<<<< HEAD
>>>>>>> osgeo-main
<<<<<<< HEAD
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
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
int gsd_wire_surf_func(geosurf *gs UNUSED, int (*user_func)(void) UNUSED)
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)(void))
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)(void))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)(void))
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)(void))
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
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int gsd_wire_surf_func(geosurf *gs, int (*user_func)())
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
{
    return (1);
}

/*!
   \brief ADD

   Need to do Zexag scale of normal for arrow direction, drawing
   routine unexags z for arrow

   \param surf surface (geosurf)

   \return
 */
int gsd_wire_arrows(geosurf *surf)
{
    typbuff *buff, *cobuff;
    int check_mask, check_color;
    int xmod, ymod, row, col, xcnt, ycnt;
    long offset, y1off;
    float tx, ty, tz, sz;
    float n[3], pt[4], xres, yres, ymax, zexag;
    int col_src, curcolor;
    gsurf_att *coloratt;

    G_debug(3, "gsd_norm_arrows");

    /* avoid scaling by zero */
    GS_get_scale(&tx, &ty, &tz, 1);

    if (tz == 0.0) {
        return (0);
    }

    sz = GS_global_exag();

    gs_update_curmask(surf);
    check_mask = surf->curmask ? 1 : 0;

    /*
       checks ATT_TOPO & ATT_COLOR no_zero flags, make a mask from each,
       combine it/them with any current mask, put in surf->curmask:
     */

    check_color = 1;
    curcolor = 0;
    coloratt = &(surf->att[ATT_COLOR]);
    col_src = surf->att[ATT_COLOR].att_src;

    if (col_src != MAP_ATT) {
        if (col_src == CONST_ATT) {
            curcolor = (int)surf->att[ATT_COLOR].constant;
        }
        else {
            curcolor = surf->wire_color;
        }

        check_color = 0;
    }

    buff = gs_get_att_typbuff(surf, ATT_TOPO, 0);
    cobuff = gs_get_att_typbuff(surf, ATT_COLOR, 0);

    xmod = surf->x_modw;
    ymod = surf->y_modw;
    xres = xmod * surf->xres;
    yres = ymod * surf->yres;
    ymax = (surf->rows - 1) * surf->yres;
    xcnt = 1 + (surf->cols - 1) / xmod;
    ycnt = 1 + (surf->rows - 1) / ymod;

    gsd_pushmatrix();
    gsd_do_scale(1);
    gsd_translate(surf->x_trans, surf->y_trans, surf->z_trans);

    zexag = surf->z_exag;
    /* CURRENTLY ALWAYS 1.0 */

    gsd_colormode(CM_COLOR);

    for (row = 0; row < ycnt; row++) {
        pt[Y] = ymax - row * yres;
        y1off = row * ymod * surf->cols;

        for (col = 0; col < xcnt; col++) {
            pt[X] = col * xres;
            offset = col * xmod + y1off;

            if (check_mask) {
                if (BM_get(surf->curmask, col * xmod, row * ymod)) {
                    continue;
                }
            }

            FNORM(surf->norms[offset], n);
            GET_MAPATT(buff, offset, pt[Z]);
            pt[Z] *= zexag;

            if (check_color) {
                curcolor = gs_mapcolor(cobuff, coloratt, offset);
            }

            gsd_arrow(pt, curcolor, xres * 2, n, sz, surf);
        } /* ea col */
<<<<<<< HEAD
<<<<<<< HEAD
    } /* ea row */
=======
    }     /* ea row */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    }     /* ea row */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    gsd_popmatrix();
    gsd_colormode(CM_DIFFUSE);

    return (1);
}

/*!
   \brief Draw coarse surface

   New (TEST) wire routine that draws low res surface
   Based on new Trinagle Fan routine
   Resolution is a function of current surface resolution
   times wire resolution

   \todo normals have to be recalculated before proper low
   res surface can be drawn

   In window optimization has been removed

   \param surf surface (geosurf)

   \return
 */
int gsd_coarse_surf_map(geosurf *surf)
{
    int /* check_mask, */ check_color, check_transp;
    int check_material, check_emis, check_shin;
    typbuff *buff, *cobuff, *trbuff, *embuff, *shbuff;
    int xmod, ymod;
    int row, col, xcnt, ycnt;
    long y1off, y2off, y3off;
    long offset2[10];
    float pt2[10][2];
    int ii;
    float x1, x2, x3, y1, y2, y3, tx, ty, tz, ttr;
    float n[3], pt[4], xres, yres, ymax, zexag;
    int em_src, sh_src, trans_src, col_src, curcolor;
    gsurf_att *ematt, *shatt, *tratt, *coloratt;

    int datacol1, datacol2, datacol3;

    /* int datarow1, datarow2, datarow3; */

    float kem, ksh, pkem, pksh;
    unsigned int ktrans;

    int step_val = 2 * surf->x_modw; /* should always be factor of 2 for fan */
    int start_val = surf->x_modw;

    /* ensure normals are correct */
    gs_calc_normals(surf);

    /* avoid scaling by zero */
    GS_get_scale(&tx, &ty, &tz, 1);

    if (tz == 0.0) {
        return (gsd_surf_const(surf, 0.0));
    }
    /* else if (surf->z_exag  == 0.0)
       {
       return(gsd_surf_const(surf, surf->z_min));
       }
       NOT YET IMPLEMENTED */

    buff = gs_get_att_typbuff(surf, ATT_TOPO, 0);
    cobuff = gs_get_att_typbuff(surf, ATT_COLOR, 0);

    gs_update_curmask(surf);
    /* check_mask = surf->curmask ? 1 : 0; */

    /*
       checks ATT_TOPO & ATT_COLOR no_zero flags, make a mask from each,
       combine it/them with any current mask, put in surf->curmask:
     */
    xmod = surf->x_mod;
    ymod = surf->y_mod;
    xres = xmod * surf->xres;
    yres = ymod * surf->yres;
    ymax = (surf->rows - 1) * surf->yres;

    xcnt = VCOLS(surf);
    ycnt = VROWS(surf);

    gsd_pushmatrix();
    gsd_do_scale(1);
    gsd_translate(surf->x_trans, surf->y_trans, surf->z_trans);
    zexag = surf->z_exag;

    gsd_colormode(CM_DIFFUSE);

    /* CURRENTLY ALWAYS 1.0 */
#ifdef CALC_AREA
    sz = GS_global_exag();
#endif

    /* TODO: get rid of (define) these magic numbers scaling the attribute vals
     */
    check_transp = 0;
    tratt = &(surf->att[ATT_TRANSP]);
    ktrans = (255U << 24);
    trans_src = surf->att[ATT_TRANSP].att_src;

    if (CONST_ATT == trans_src && surf->att[ATT_TRANSP].constant != 0.0) {
        ktrans = (255 - (int)surf->att[ATT_TRANSP].constant) << 24;
        gsd_blend(1);
        gsd_zwritemask(0x0);
    }
    else if (MAP_ATT == trans_src) {
        trbuff = gs_get_att_typbuff(surf, ATT_TRANSP, 0);
        check_transp = trbuff ? 1 : 0;
        gsd_blend(1);
        gsd_zwritemask(0x0);
    }

    check_emis = 0;
    ematt = &(surf->att[ATT_EMIT]);
    kem = 0.0;
    pkem = 1.0;
    em_src = surf->att[ATT_EMIT].att_src;

    if (CONST_ATT == em_src) {
        kem = surf->att[ATT_EMIT].constant / 255.;
    }
    else if (MAP_ATT == em_src) {
        embuff = gs_get_att_typbuff(surf, ATT_EMIT, 0);
        check_emis = embuff ? 1 : 0;
    }

    check_shin = 0;
    shatt = &(surf->att[ATT_SHINE]);
    ksh = 0.0;
    pksh = 1.0;
    sh_src = surf->att[ATT_SHINE].att_src;

    if (CONST_ATT == sh_src) {
        ksh = surf->att[ATT_SHINE].constant / 255.;
        gsd_set_material(1, 0, ksh, kem, 0x0);
    }
    else if (MAP_ATT == sh_src) {
        shbuff = gs_get_att_typbuff(surf, ATT_SHINE, 0);
        check_shin = shbuff ? 1 : 0;
    }

    /* will need to check for color source of FUNC_ATT & NOTSET_ATT,
       or else use more general and inefficient gets */
    check_color = 1;
    curcolor = 0;
    coloratt = &(surf->att[ATT_COLOR]);
    col_src = surf->att[ATT_COLOR].att_src;

    if (col_src != MAP_ATT) {
        if (col_src == CONST_ATT) {
            curcolor = (int)surf->att[ATT_COLOR].constant;
        }
        else {
            curcolor = surf->wire_color;
        }

        check_color = 0;
    }

    check_material = (check_shin || check_emis || (kem && check_color));

    /* would also be good to check if colormap == surfmap, to increase speed */
    /* will also need to set check_transp, check_shine, etc & fix material */
    for (row = start_val; row <= ycnt - start_val; row += step_val) {

        /*
           datarow1 = row * ymod;
           datarow2 = (row - (step_val / 2)) * ymod;
           datarow3 = (row + (step_val / 2)) * ymod;
         */

        y1 = ymax - row * yres;
        y2 = ymax - (row - (step_val / 2)) * yres;
        y3 = ymax - (row + (step_val / 2)) * yres;

        y1off = row * ymod * surf->cols;
        y2off = (row - (step_val / 2)) * ymod * surf->cols;
        y3off = (row + (step_val / 2)) * ymod * surf->cols;

        for (col = start_val; col <= xcnt - start_val; col += step_val) {

            datacol1 = col * xmod;
            datacol2 = (col - (step_val / 2)) * xmod;
            datacol3 = (col + (step_val / 2)) * xmod;

            x1 = col * xres;
            x2 = (col - (step_val / 2)) * xres;
            x3 = (col + (step_val / 2)) * xres;

            /* Do not need BM_get because GET_MAPATT calls
             * same and returns zero if masked
             */
            offset2[0] = y1off + datacol1; /* fan center */
            pt2[0][X] = x1;
            pt2[0][Y] = y1; /* fan center */
            pt[X] = pt2[0][X];
            pt[Y] = pt2[0][Y];
            if (!GET_MAPATT(buff, offset2[0], pt[Z]))
                continue; /* masked */
            pt[Z] *= zexag;

            offset2[1] = y2off + datacol2;
            offset2[2] = y2off + datacol1;
            offset2[3] = y2off + datacol3;
            offset2[4] = y1off + datacol3;
            offset2[5] = y3off + datacol3;
            offset2[6] = y3off + datacol1;
            offset2[7] = y3off + datacol2;
            offset2[8] = y1off + datacol2;
            offset2[9] = y2off + datacol2; /* repeat 1st corner to close */

            pt2[1][X] = x2;
            pt2[1][Y] = y2;
            pt2[2][X] = x1;
            pt2[2][Y] = y2;
            pt2[3][X] = x3;
            pt2[3][Y] = y2;
            pt2[4][X] = x3;
            pt2[4][Y] = y1;
            pt2[5][X] = x3;
            pt2[5][Y] = y3;
            pt2[6][X] = x1;
            pt2[6][Y] = y3;
            pt2[7][X] = x2;
            pt2[7][Y] = y3;
            pt2[8][X] = x2;
            pt2[8][Y] = y1;
            pt2[9][X] = x2;
            pt2[9][Y] = y2; /* repeat 1st corner to close */

            /* Run through triangle fan */
            gsd_bgntfan();
            for (ii = 0; ii < 10; ii++) {

                if (ii > 0) {
                    pt[X] = pt2[ii][X];
                    pt[Y] = pt2[ii][Y];
                    if (!GET_MAPATT(buff, offset2[ii], pt[Z]))
                        continue;
                    pt[Z] *= zexag;
                }

                FNORM(surf->norms[offset2[ii]], n);

                if (check_color)
                    curcolor = gs_mapcolor(cobuff, coloratt, offset2[ii]);

                if (check_transp) {
                    GET_MAPATT(trbuff, offset2[ii], ttr);
                    ktrans = (char)SCALE_ATT(tratt, ttr, 0, 255);
<<<<<<< HEAD
<<<<<<< HEAD
                    ktrans = (char)(255U - ktrans) << 24;
=======
                    ktrans = (char)(255 - ktrans) << 24;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                    ktrans = (char)(255 - ktrans) << 24;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                }

                if (check_material) {
                    if (check_emis) {
                        GET_MAPATT(embuff, offset2[ii], kem);
                        kem = SCALE_ATT(ematt, kem, 0., 1.);
                    }

                    if (check_shin) {
                        GET_MAPATT(shbuff, offset2[ii], ksh);
                        ksh = SCALE_ATT(shatt, ksh, 0., 1.);
                    }

                    if (pksh != ksh || pkem != kem || (kem && check_color)) {
                        pksh = ksh;
                        pkem = kem;
                        gsd_set_material(check_shin, check_emis, ksh, kem,
                                         curcolor);
                    }
                }

                gsd_litvert_func(n, ktrans | curcolor, pt);

            } /* close ii loop */
            gsd_endtfan();

        } /* end col */

    } /* end row */

    gsd_popmatrix();
    /*
       gsd_colormode(CM_DIFFUSE);
     */
    gsd_blend(0);
    gsd_zwritemask(0xffffffff);

    return (0);
}
