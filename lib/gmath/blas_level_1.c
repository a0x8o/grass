/*****************************************************************************
 *
 * MODULE:       Grass numerical math interface
 * AUTHOR(S):    Soeren Gebbert, Berlin (GER) Dec 2006
 *                 soerengebbert <at> googlemail <dot> com
 *
 * PURPOSE:      grass blas implementation
 *                 part of the gmath library
 *
 * COPYRIGHT:    (C) 2010 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <math.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <grass/gis.h>
#include <grass/gmath.h>

/* **************************************************************** */
/* *************** D O U B L E ************************************ */
/* **************************************************************** */

/*!
 * \brief Compute the dot product of vector x and y
 *
 * \f[ a = {\bf x}^T  {\bf y} \f]
 *
 * The functions creates its own parallel OpenMP region.
 * It can be called within a parallel OpenMP region if nested parallelism is
 * supported by the compiler.
 *
 * \param x       (double *)
 * \param y       (double *)
 * \param value (double *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_d_x_dot_y(double *x, double *y, double *value, int rows)
{
    int i;

    double s = 0.0;

#pragma omp parallel for schedule(static) reduction(+ : s)
    for (i = rows - 1; i >= 0; i--) {
        s += x[i] * y[i];
    }
#pragma omp single
    {
        *value = s;
    }
    return;
}

/*!
 * \brief Compute the euclid norm of vector x
 *
 * \f[ a = ||{\bf x}||_2 \f]
 *
 * The functions creates its own parallel OpenMP region.
 * It can be called within a parallel OpenMP region if nested parallelism is
 * supported by the compiler.
 *
 * \param x       (double *) -- the vector
 * \param value (double *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_d_euclid_norm(double *x, double *value, int rows)
{
    int i;

    double s = 0.0;

#pragma omp parallel for schedule(static) reduction(+ : s)
    for (i = rows - 1; i >= 0; i--) {
        s += x[i] * x[i];
    }
#pragma omp single
    {
        *value = sqrt(s);
    }
    return;
}

/*!
 * \brief Compute the asum norm of vector x
 *
 * \f[ a = ||{\bf x}||_1 \f]
 *
 * The functions creates its own parallel OpenMP region.
 * It can be called within a parallel OpenMP region if nested parallelism is
 * supported by the compiler.
 *
 * \param x       (double *)-- the vector
 * \param value (double *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_d_asum_norm(double *x, double *value, int rows)
{
    int i = 0;

    double s = 0.0;

#pragma omp parallel for schedule(static) reduction(+ : s)
    for (i = rows - 1; i >= 0; i--) {
        s += fabs(x[i]);
    }
#pragma omp single
    {
        *value = s;
    }
    return;
}

/*!
 * \brief Compute the maximum norm of vector x
 *
 * \f[ a = ||{\bf x}||_\infty \f]
 *
 * This function is not multi-threaded
 *
 * \param x       (double *)-- the vector
 * \param value (double *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_d_max_norm(double *x, double *value, int rows)
{
    int i;

    double max = 0.0;

    max = fabs(x[rows - 1]);
    for (i = rows - 2; i >= 0; i--) {
        if (max < fabs(x[i]))
            max = fabs(x[i]);
    }

    *value = max;
}

/*!
 * \brief Scales vectors x and y with the scalars a and b and adds them
 *
 * \f[ {\bf z} = a{\bf x} + b{\bf y} \f]
 *
 * This function is multi-threaded with OpenMP and can be called within a
 * parallel OpenMP region.
 *
 * \param x      (double *)
 * \param y      (double *)
 * \param z      (double *)
 * \param a      (double)
 * \param b      (double)
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_d_ax_by(double *x, double *y, double *z, double a, double b,
                    int rows)
{
    int i;

    /*find specific cases */
    if (b == 0.0) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i];
        }
    }
    else if ((a == 1.0) && (b == 1.0)) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = x[i] + y[i];
        }
    }
    else if ((a == 1.0) && (b == -1.0)) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = x[i] - y[i];
        }
    }
    else if (a == b) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * (x[i] + y[i]);
        }
    }
    else if (b == -1.0) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i] - y[i];
        }
    }
    else if (b == 1.0) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i] + y[i];
        }
    }
    else {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i] + b * y[i];
        }
    }

    return;
}

/*!
 * \brief Copy the vector x to y
 *
 * \f[ {\bf y} = {\bf x} \f]
 *
 * This function is not multi-threaded
 *
 * \param x      (double *)
 * \param y      (double *)
 * \param rows (int)
 *
 * */
void G_math_d_copy(double *x, double *y, int rows)
{
    y = memcpy(y, x, rows * sizeof(double));

    return;
}

/* **************************************************************** */
/* *************** F L O A T ************************************** */
/* **************************************************************** */

/*!
 * \brief Compute the dot product of vector x and y
 *
 * \f[ a = {\bf x}^T  {\bf y} \f]
 *
 * The functions creates its own parallel OpenMP region.
 * It can be called within a parallel OpenMP region if nested parallelism is
 * supported by the compiler.
 *
 * \param x       (float *)
 * \param y       (float *)
 * \param value (float *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_f_x_dot_y(float *x, float *y, float *value, int rows)
{
    int i;

    float s = 0.0;

#pragma omp parallel for schedule(static) reduction(+ : s)
    for (i = rows - 1; i >= 0; i--) {
        s += x[i] * y[i];
    }
#pragma omp single
    {
        *value = s;
    }
    return;
}

/*!
 * \brief Compute the euclid norm of vector x
 *
 * \f[ a = ||{\bf x}||_2 \f]
 *
 * The functions creates its own parallel OpenMP region.
 * It can be called within a parallel OpenMP region if nested parallelism is
 * supported by the compiler.
 *
 * \param x       (double *) -- the vector
 * \param value (float *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_f_euclid_norm(float *x, float *value, int rows)
{
    int i;

    float s = 0.0;

#pragma omp parallel for schedule(static) reduction(+ : s)
    for (i = rows - 1; i >= 0; i--) {
        s += x[i] * x[i];
    }
#pragma omp single
    {
        *value = sqrt(s);
    }
    return;
}

/*!
 * \brief Compute the asum norm of vector x
 *
 * \f[ a = ||{\bf x}||_1 \f]
 *
 * The functions creates its own parallel OpenMP region.
 * It can be called within a parallel OpenMP region if nested parallelism is
 * supported by the compiler.
 *
 * \param x       (float *)-- the vector
 * \param value (float *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_f_asum_norm(float *x, float *value, int rows)
{
    int i;

    float s = 0.0;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
#pragma omp parallel for schedule(static) private(i) reduction(+ : s)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
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
#pragma omp parallel for schedule(static) private(i) reduction(+ : s)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
#pragma omp parallel for schedule(static) private(i) reduction(+ : s, count)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
        count++;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
#pragma omp parallel for schedule(static) private(i) reduction(+ : s, count)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
        count++;
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
#pragma omp parallel for schedule(static) private(i) reduction(+ : s)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
#pragma omp parallel for schedule(static) private(i) reduction(+ : s, count)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
        count++;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
#pragma omp parallel for schedule(static) private(i) reduction(+ : s)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
#pragma omp parallel for schedule(static) private(i) reduction(+ : s)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
#pragma omp parallel for schedule(static) private(i) reduction(+ : s, count)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
        count++;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
#pragma omp parallel for schedule(static) private(i) reduction(+ : s)
    for (i = 0; i < rows; i++) {
        s += fabs(x[i]);
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
    }
#pragma omp single
    {
        *value = s;
    }
    return;
}

/*!
 * \brief Compute the maximum norm of vector x
 *
 * \f[ a = ||{\bf x}||_\infty \f]
 *
 * This function is not multi-threaded
 *
 * \param x       (float *)-- the vector
 * \param value (float *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_f_max_norm(float *x, float *value, int rows)
{
    int i;

    float max = 0.0;

    max = fabs(x[rows - 1]);
    for (i = rows - 2; i >= 0; i--) {
        if (max < fabs(x[i]))
            max = fabs(x[i]);
    }
    *value = max;
    return;
}

/*!
 * \brief Scales vectors x and y with the scalars a and b and adds them
 *
 * \f[ {\bf z} = a{\bf x} + b{\bf y} \f]
 *
 * This function is multi-threaded with OpenMP and can be called within a
 * parallel OpenMP region.
 *
 * \param x      (float *)
 * \param y      (float *)
 * \param z      (float *)
 * \param a      (float)
 * \param b      (float)
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_f_ax_by(float *x, float *y, float *z, float a, float b, int rows)
{
    int i;

    /*find specific cases */
    if (b == 0.0) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i];
        }
    }
    else if ((a == 1.0) && (b == 1.0)) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = x[i] + y[i];
        }
    }
    else if ((a == 1.0) && (b == -1.0)) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = x[i] - y[i];
        }
    }
    else if (a == b) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * (x[i] + y[i]);
        }
    }
    else if (b == -1.0) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i] - y[i];
        }
    }
    else if (b == 1.0) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i] + y[i];
        }
    }
    else {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i] + b * y[i];
        }
    }

    return;
}

/*!
 * \brief Copy the vector x to y
 *
 * \f[ {\bf y} = {\bf x} \f]
 *
 * This function is not multi-threaded
 *
 * \param x      (float *)
 * \param y      (float *)
 * \param rows (int)
 *
 * */
void G_math_f_copy(float *x, float *y, int rows)
{
    y = memcpy(y, x, rows * sizeof(float));

    return;
}

/* **************************************************************** */
/* *************** I N T E G E R ********************************** */
/* **************************************************************** */

/*!
 * \brief Compute the dot product of vector x and y
 *
 * \f[ a = {\bf x}^T  {\bf y} \f]
 *
 * The functions creates its own parallel OpenMP region.
 * It can be called within a parallel OpenMP region if nested parallelism is
 * supported by the compiler.
 *
 * \param x       (int *)
 * \param y       (int *)
 * \param value (double *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_i_x_dot_y(int *x, int *y, double *value, int rows)
{
    int i;

    double s = 0.0;

#pragma omp parallel for schedule(static) reduction(+ : s)
    for (i = rows - 1; i >= 0; i--) {
        s += x[i] * y[i];
    }
#pragma omp single
    {
        *value = s;
    }
    return;
}

/*!
 * \brief Compute the euclid norm of vector x
 *
 * \f[ a = ||{\bf x}||_2 \f]
 *
 * The functions creates its own parallel OpenMP region.
 * It can be called within a parallel OpenMP region if nested parallelism is
 * supported by the compiler.
 *
 * \param x       (int *) -- the vector
 * \param value (double *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_i_euclid_norm(int *x, double *value, int rows)
{
    int i;

    double s = 0.0;

#pragma omp parallel for schedule(static) reduction(+ : s)
    for (i = rows - 1; i >= 0; i--) {
        s += x[i] * x[i];
    }
#pragma omp single
    {
        *value = sqrt(s);
    }
    return;
}

/*!
 * \brief Compute the asum norm of vector x
 *
 * \f[ a = ||{\bf x}||_1 \f]
 *
 * The functions creates its own parallel OpenMP region.
 * It can be called within a parallel OpenMP region if nested parallelism is
 * supported by the compiler.
 *
 * \param x       (int *)-- the vector
 * \param value (double *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_i_asum_norm(int *x, double *value, int rows)
{
    int i;

    double s = 0.0;

#pragma omp parallel for schedule(static) reduction(+ : s)
    for (i = rows - 1; i >= 0; i--) {
        s += (double)abs(x[i]);
    }
#pragma omp single
    {
        *value = s;
    }
    return;
}

/*!
 * \brief Compute the maximum norm of vector x
 *
 * \f[ a = ||{\bf x}||_\infty \f]
 *
 * This function is not multi-threaded
 *
 * \param x       (int *)-- the vector
 * \param value (int *)  -- the return value
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_i_max_norm(int *x, int *value, int rows)
{
    int i;

    int max = 0.0;

    max = abs(x[rows - 1]);
    for (i = rows - 2; i >= 0; i--) {
        if (max < abs(x[i]))
            max = abs(x[i]);
    }

    *value = max;
}

/*!
 * \brief Scales vectors x and y with the scalars a and b and adds them
 *
 * \f[ {\bf z} = a{\bf x} + b{\bf y} \f]
 *
 * This function is multi-threaded with OpenMP and can be called within a
 * parallel OpenMP region.
 *
 * \param x      (int *)
 * \param y      (int *)
 * \param z      (int *)
 * \param a      (int)
 * \param b      (int)
 * \param rows (int)
 * \return (void)
 *
 * */
void G_math_i_ax_by(int *x, int *y, int *z, int a, int b, int rows)
{
    int i;

    /*find specific cases */
    if (b == 0.0) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i];
        }
    }
    else if ((a == 1.0) && (b == 1.0)) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = x[i] + y[i];
        }
    }
    else if ((a == 1.0) && (b == -1.0)) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = x[i] - y[i];
        }
    }
    else if (a == b) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * (x[i] + y[i]);
        }
    }
    else if (b == -1.0) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i] - y[i];
        }
    }
    else if (b == 1.0) {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i] + y[i];
        }
    }
    else {
#pragma omp for schedule(static)
        for (i = rows - 1; i >= 0; i--) {
            z[i] = a * x[i] + b * y[i];
        }
    }

    return;
}

/*!
 * \brief Copy the vector x to y
 *
 * \f[ {\bf y} = {\bf x} \f]
 *
 * This function is not multi-threaded
 *
 * \param x      (int *)
 * \param y      (int *)
 * \param rows (int)
 *
 * */
void G_math_i_copy(int *x, int *y, int rows)
{
    y = memcpy(y, x, rows * sizeof(int));

    return;
}
