/****************************************************************************
 *
 * MODULE:       r.coin
 *
 * AUTHOR(S):    Michael O'Shea - CERL
 *               Michael Shapiro - CERL
 *
 * PURPOSE:      Calculates the coincidence of two raster map layers.
 *
 * COPYRIGHT:    (C) 2006 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *

***************************************************************************/

#include <stdio.h>
#include <string.h>

int format_double(double v, char *buf, int n)
{
    char fmt[15];
    int k;

    sprintf(fmt, "%%%d.2lf", n);
    sprintf(buf, fmt, v);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
>>>>>>> osgeo-main
    for (k = n; strlen(buf) > n; k--) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
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
    for (k = n; strlen(buf) > n; k--) {
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
    for (k = n; strlen(buf) > n; k--) {
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
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
    for (k = n; strlen(buf) > n; k--) {
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
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
    for (k = n; strlen(buf) > n; k--) {
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
=======
>>>>>>> osgeo-main
=======
    for (k = n; (ssize_t)strlen(buf) > n; k--) {
=======
    for (k = n; strlen(buf) > n; k--) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
        sprintf(fmt, "%%%d.%dg", n, k);
        sprintf(buf, fmt, v);
    }

    return 0;
}
