/* Functions: do_grid, do_grid_numbers, format_northing, format_easting
 **
 ** These functions are much modified versions of the p.map functions.
 **
 ** Author: Paul W. Carlson     April 1992
 */

#include <string.h>
#include <math.h>
#include "local_proto.h"

#define LEFT   0
#define RIGHT  1
#define LOWER  0
#define UPPER  1
#define CENTER 2

static char *format_northing(double, int);
static char *format_easting(double, int);

int do_grid(void)
{
    double g, e1, e2;
    int j;

    if (PS.grid <= 0)
        return 1;

    /* set color and set line width to 1 */
    set_ps_color(&PS.grid_color);
    set_line_width(PS.grid_width);

    /* draw horizontal lines in 3 pieces -- lat-lon lines must not
     * extend more than half the globe
     * start with first grid line just south of the window north
     */
    e1 = (PS.w.east * 2 + PS.w.west) / 3;
    e2 = (PS.w.west * 2 + PS.w.east) / 3;

    g = floor(PS.w.north / PS.grid) * PS.grid;
    for (j = 0; g >= PS.w.south; j++, g -= PS.grid) {
        if (g == PS.w.north || g == PS.w.south)
            continue;

        start_line(PS.w.east, g);
        sec_draw = 0;
        G_plot_line(PS.w.east, g, e1, g);
        fprintf(PS.fp, " D ");

        start_line(e1, g);
        sec_draw = 0;
        G_plot_line(e1, g, e2, g);
        fprintf(PS.fp, " D ");

        start_line(e2, g);
        sec_draw = 0;
        G_plot_line(e2, g, PS.w.west, g);
        fprintf(PS.fp, " D\n");
    }

    /* vertical lines */
    /* start with first grid line just west of the window east */
    g = floor(PS.w.east / PS.grid) * PS.grid;
    for (j = 0; g > PS.w.west; j++, g -= PS.grid) {
        if (g == PS.w.east || g == PS.w.west)
            continue;
        start_line(g, PS.w.north);
        sec_draw = 0;
        G_plot_line(g, PS.w.north, g, PS.w.south);
        if (j & 1)
            fprintf(PS.fp, " D\n");
        else
            fprintf(PS.fp, " D ");
    }

    return 0;
}

int do_grid_cross(void)
{
    double g_north, g_east;

    if (PS.grid <= 0)
        return 1;

    /* set color and set line width to 1 */
    set_ps_color(&PS.grid_color);
    set_line_width(PS.grid_width);

    g_north = floor(PS.w.north / PS.grid) * PS.grid;
    g_east = floor(PS.w.east / PS.grid) * PS.grid;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
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
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
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
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
>>>>>>> osgeo-main
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
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
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
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
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
=======
    for (j = 0; g_north >= PS.w.south; j++, g_north -= PS.grid) {
        for (k = 0; g_east > PS.w.west; k++, g_east -= PS.grid) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
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
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
    for (; g_north >= PS.w.south; g_north -= PS.grid) {
        for (; g_east > PS.w.west; g_east -= PS.grid) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))

            if (g_north == PS.w.north || g_north == PS.w.south)
                continue;
            if (g_east == PS.w.east || g_east == PS.w.west)
                continue;

            start_line(g_east - PS.grid_cross, g_north);
            G_plot_line(g_east - PS.grid_cross, g_north, g_east + PS.grid_cross,
                        g_north);
            fprintf(PS.fp, " D ");
            start_line(g_east, g_north - PS.grid_cross);
            G_plot_line(g_east, g_north - PS.grid_cross, g_east,
                        g_north + PS.grid_cross);
            fprintf(PS.fp, " D ");
        }
        g_east = floor(PS.w.east / PS.grid) * PS.grid;
    }

    return 0;
}

int do_grid_numbers(void)
{
    double g;
    char num_text[50];
    int grid, vy, vx, hy = 0, hx = 0;
    int first, len, x, y, last_bottom, last_right;
    int rounded_grid, margin;

    if (PS.grid <= 0 || PS.grid_numbers <= 0)
        return 1;
    grid = PS.grid * PS.grid_numbers;

    /* round grid to multiple of 10 */
    rounded_grid = 1;
    if (PS.w.proj != PROJECTION_LL) {
        sprintf(num_text, "%d", PS.grid);
        len = strlen(num_text);
        while (len-- && num_text[len] == '0')
            rounded_grid *= 10;
        if (rounded_grid == 10)
            rounded_grid = 1;
    }

    /* initialize */
    set_font_name(PS.grid_font);
    set_font_size(PS.grid_fontsize);
    set_ps_color(&PS.grid_numbers_color);
    first = 1;

    /* horizontal grid numbers
     * these numbers only appear on the left edge of the first panel.
     * center the numbers on each grid line.
     * suppress number if it falls off the map or would overlay the previous
     *  label
     */
    margin = (int)(0.2 * (double)PS.grid_fontsize + 0.5);
    if (margin < 2)
        margin = 2;
    fprintf(PS.fp, "/mg %d def\n", margin);
    g = floor(PS.w.north / grid) * grid;
    last_bottom = (int)PS.map_top;
    first = 1;
    /* x = XCONV(PS.w.west); */

    for (; g > PS.w.south; g -= grid) {
        /*y = YCONV(g); */

        G_plot_where_xy(PS.w.west, g, &vx, &vy);
        x = (double)vx / 10.;
        y = (double)vy / 10.;

        if (y + PS.grid_fontsize > last_bottom)
            continue;
        if (y - PS.grid_fontsize < (int)PS.map_bot)
            continue;
        sprintf(num_text, "%s", format_northing(g, rounded_grid));
        text_box_path(x, y, LEFT, CENTER, num_text, 0);
        set_rgb_color(WHITE);
        fprintf(PS.fp, "F ");
        set_ps_color(&PS.grid_numbers_color);
        fprintf(PS.fp, "TIB\n");
        last_bottom = y - PS.grid_fontsize;
        if (first) {
            first = 0;
            hy = y + (int)(0.5 * (double)PS.grid_fontsize + 0.5) + margin;
            hx = x + 0.7 * strlen(num_text) * PS.grid_fontsize + 2 * margin;
        }
    }

    /* vertical grid numbers
     * center the numbers on each grid line.
     * suppress number if it falls of the map or would overlay the previous
     *  label
     */
    g = floor(PS.w.west / grid) * grid;
    last_right = (int)PS.map_left;
    /* y = YCONV(PS.w.north); */
    for (; g < PS.w.east; g += grid) {
        /* x = XCONV(g); */

        G_plot_where_xy(g, PS.w.north, &vx, &vy);
        x = (double)vx / 10.;
        y = (double)vy / 10.;

        if (x - PS.grid_fontsize < last_right)
            continue;
        if (x + PS.grid_fontsize > (int)PS.map_right)
            continue;
        sprintf(num_text, "%s", format_easting(g, rounded_grid));
        vy = y - 0.7 * strlen(num_text) * PS.grid_fontsize - 2 * margin;
        vx = x - (int)(0.5 * (double)PS.grid_fontsize + 0.5) - margin;
        if (vx < hx && vy < hy)
            continue;
        fprintf(PS.fp, "ZB (%s) PB 90 rotate\n", num_text);
        fprintf(PS.fp, "%d br sub bl add mg add\n", y);
        fprintf(PS.fp, "%d bt bb sub D2 add mg sub neg TR TB\n", x);
        set_rgb_color(WHITE);
        fprintf(PS.fp, "F ");
        set_ps_color(&PS.grid_numbers_color);
        fprintf(PS.fp, "TIB\n");
        last_right = x + PS.grid_fontsize;
    }

    return 0;
}

static char *format_northing(double n, int round)
{
    static char text[50];

    if (PS.w.proj == PROJECTION_LL)
        G_format_northing(n, text, PS.w.proj);
    else {
        n = floor(n / round);
        sprintf(text, "%.0f", n);
    }
    return text;
}

static char *format_easting(double e, int round)
{
    static char text[50];

    if (PS.w.proj == PROJECTION_LL)
        G_format_easting(e, text, PS.w.proj);
    else {
        e = floor(e / round);
        sprintf(text, "%.0f", e);
    }
    return text;
}
