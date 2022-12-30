/****************************************************************************
 *
 *  MODULE:        r.terraflow
 *
 *  COPYRIGHT (C) 2007 Laura Toma
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *****************************************************************************/

#ifndef _genericwindow_H
#define _genericwindow_H

#include <stdio.h>

#include <grass/iostream/ami.h>
#include "types.h"

/* ************************************************************* *
 * class 'genericWindow' implements a 3x3 window in a grid;
 * ************************************************************* */

template <class T>
class genericWindow {
protected:
    T data[9];

public:
    /***************************************************************/
    /* initialize a window to 0 */
    genericWindow()
    {
        for (int i = 0; i < 9; i++) {
            data[i] = T();
        }
    }

    /***************************************************************/
    /* initialize a window from an array of 9 values */
    genericWindow(T *a)
    {
        assert(a);
        for (int i = 0; i < 9; i++) {
            data[i] = a[i];
        }
    }

    /***************************************************************/
    /* initialize a window from 3 arrays of 3 elements each */
    genericWindow(T *a, T *b, T *c)
    {
        int i;
        assert(a);
        assert(b);
        assert(c);
        for (i = 0; i < 3; i++) {
            data[i] = a[i];
            data[i + 3] = b[i];
            data[i + 6] = c[i];
        }
    }

    /***************************************************************/
    /* initialize a window from 3 arrays of 3 elements each */
    template <class C>
    genericWindow(C *a, C *b, C *c)
    {
        int i;
        assert(a);
        assert(b);
        assert(c);
        for (i = 0; i < 3; i++) {
            data[i] = a[i];
            data[i + 3] = b[i];
            data[i + 6] = c[i];
        }
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
    /* set specified neighbour di,dj in {-1,0,1} */
    void set(int di, int dj, T val)
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        data[4 + dj + di * 3] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
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
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
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
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
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
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
    /* set specified neighbour di,dj in {-1,0,1} */
    void set(int di, int dj, T val)
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        data[4 + dj + di * 3] = val;
    }

    /***************************************************************/
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
    /* set specified neighbour di,dj in {-1,0,1} */
    void set(int di, int dj, T val)
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        data[4 + dj + di * 3] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
    /* get specified neighbour di,dj in {-1,0,1} */
    T get(short di, short dj) const
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        return data[4 + dj + di * 3];
    }

    /***************************************************************/
    /* get specified neighbour i in 0..8 */
    T get(unsigned short i = 4) const
    {
        assert(i <= 8);
        return data[i];
    }

    /***************************************************************/
    /* set specified neighbour i in 0..8 */
    void set(unsigned short i, T val)
    {
        assert(i <= 8);
        data[i] = val;
    }

    /***************************************************************/
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
    /* set specified neighbour di,dj in {-1,0,1} */
    void set(int di, int dj, T val)
    {
        assert(di >= -1 && di <= 1);
        assert(dj >= -1 && dj <= 1);
        data[4 + dj + di * 3] = val;
    }

    /***************************************************************/
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
    /*  multiply all elements by a scalar */
    void scalarMultiply(T mult)
    {
        for (int i = 0; i < 9; i++) {
            data[i] *= mult;
        }
    }

    /***************************************************************/
    inline friend ostream &operator<<(ostream &s, const genericWindow<T> &x)
    {
        s << "[" << x.data[0] << "," << x.data[1] << "," << x.data[2] << "]\n";
        s << "[" << x.data[3] << "," << x.data[4] << "," << x.data[5] << "]\n";
        s << "[" << x.data[6] << "," << x.data[7] << "," << x.data[8] << "]\n";
        return s;
    }
};

typedef genericWindow<elevation_type> ElevationWindow;

void fillPit(ElevationWindow &win);

#endif
