/* This file and its content is not used. */
/* Could be removed at some point.       */
#if 0
/****************************************************************/
/* disp_matrix()        Function to display the contents of     */
/*                      the three matrices used in solving      */
/*                      the set of linear equations.            */
/*                      V.1.0, Jo Wood, 9th December, 1994.     */

/****************************************************************/

#include "param.h"

void disp_matrix(double **a, double *x, double *z, int n)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
                        /* Displays matrices used to solve a
                           set of linear equations in the form

                           _                        _      _  _      _  _
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 

                           _                        _      _  _      _  _ 
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form

                           _                        _      _  _      _  _
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
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> main
=======
=======
=======
=======
=======
=======
=======
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
>>>>>>> osgeo-main
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 

                           _                        _      _  _      _  _ 
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form

                           _                        _      _  _      _  _
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

=======
                        /* Displays matrices used to solve a 
                           set of linear equations in the form 
=======
                        /* Displays matrices used to solve a
                           set of linear equations in the form
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))

                           _                        _      _  _      _  _
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======

                           _                        _      _  _      _  _ 
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======

                           _                        _      _  _      _  _
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======

                           _                        _      _  _      _  _ 
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======

                           _                        _      _  _      _  _
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
                           | a(0,0) a(0,1) ... a(0,n) |    | x0 |    | z0 |
                           | a(1,0) a(1,1) ... a(1,n) |    | x1 |    | z1 |
                           |    :           :   ...   :    | .  | :  | =  | :  |
                           |    :           :   ...   :    |    | :  |    | :  |
                           | a(n,0) a(n,1) ... a(n,n) |    | xn |    | zn |
                           -                        -      -  -      -  -

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
                         */
{

    int row, col;               /* Counts through the matrix */
    char dummy[128];            /* Kewboard input (pause) */

    for (row = 0; row < n; row++) {
        fprintf(stdout, "[ ");

        for (col = 0; col < n; col++)
            fprintf(stdout, "%.3f\t", a[row][col] / 1);

        fprintf(stdout, "]\t[ %.0f\t]\t[ %.0f\t]\n", x[row], z[row]);
    }
    fprintf(stdout, "\n\n");

    fgets(dummy, 70, stdin);
}

void disp_wind(CELL * z)
{                               /* Local window */

    int row, col;               /* Count through local window. */
    char dummy[128];


    for (row = 0; row < wsize; row++) {
        for (col = 0; col < wsize; col++)
            fprintf(stdout, "%d\t", *(z + (row * wsize) + col));

        fprintf(stdout, "\n");
    }

    fgets(dummy, 70, stdin);
}
#endif
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
extern int dummy_for_iso_compilers; /* suppress -Wempty-translation-unit */
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
extern int dummy_for_iso_compilers; /* suppress -Wempty-translation-unit */
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
extern int dummy_for_iso_compilers; /* suppress -Wempty-translation-unit */
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
extern int dummy_for_iso_compilers; /* suppress -Wempty-translation-unit */
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
