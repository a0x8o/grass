<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
/* h_measure.c */
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
=======
/* h_measure.c */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
/****************************************************************************
 *
 * MODULE:       r.texture
 * AUTHOR(S):    Carmine Basco - basco@unisannio.it
 *               with hints from:
 *                         prof. Giulio Antoniol - antoniol@ieee.org
 *                         prof. Michele Ceccarelli - ceccarelli@unisannio.it

 * PURPOSE:      Intended to explain GRASS raster programming.
 *               Create map raster with textural features.
 *
 * COPYRIGHT:    (C) 2002 by University of Sannio (BN) - Italy
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 * Permission to use, copy, modify, and distribute this software and its
 * documentation for any purpose and without fee is hereby granted. This
 * software is provided "as is" without express or implied warranty.
 *
 *****************************************************************************/

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
#include "matvec.h"

typedef struct menu {
    char *name;   /* measure name */
    char *desc;   /* menu display - full description */
    char *suffix; /* output suffix */
    char useme;   /* calculate this measure if set */
    int idx;      /* measure index */
} menu;

float h_measure(int t_m, struct matvec *mv);

float f1_asm(struct matvec *mv);
float f2_contrast(struct matvec *mv);
float f3_corr(struct matvec *mv);
float f4_var(struct matvec *mv);
float f5_idm(struct matvec *mv);
float f6_savg(struct matvec *mv);
float f7_svar(struct matvec *mv);
float f8_sentropy(struct matvec *mv);
float f9_entropy(struct matvec *mv);
float f10_dvar(struct matvec *mv);
float f11_dentropy(struct matvec *mv);
float f12_icorr(struct matvec *mv);
float f13_icorr(struct matvec *mv);
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
float h_measure(int);
void alloc_vars(int);
int set_vars(int **grays, int curr_rrow, int curr_col, int size, int offset,
             int t_d, int with_nulls);
int set_angle_vars(int angle, int have_px, int have_py, int have_pxpys,
                   int have_pxpyd);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
