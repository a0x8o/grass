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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
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
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
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
<<<<<<< HEAD
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
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
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
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
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
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
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
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
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
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
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
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
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
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
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
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
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
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
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
=======
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
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
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
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
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
    genericWindow(const genericWindow<T> &win)
    {
        for (int i = 0; i < 9; i++) {
            data[i] = win.data[i];
        }
    }

    /***************************************************************/
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
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
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
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
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
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
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
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
<<<<<<< HEAD
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
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
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
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
