/*****************************************************************************
 *
 * MODULE:       Grass PDE Numerical Library
 * AUTHOR(S):    Soeren Gebbert, Berlin (GER) Dec 2006
 *                 soerengebbert <at> gmx <dot> de
 *
 * PURPOSE:      functions to manage linear equation systems
 *                 part of the gpde library
 *
 * COPYRIGHT:    (C) 2000 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <stdlib.h>
#include <grass/N_pde.h>
#include <grass/gmath.h>

/*!
 * \brief Allocate memory for a (not) quadratic linear equation system which
 * includes the Matrix A, vector x and vector b
 *
 * This function calls #N_alloc_les_param
 *
 * \param cols int
 * \param rows int
 * \param type int
 * \return N_les *
 *
 * */
N_les *N_alloc_nquad_les(int cols, int rows, int type)
{
    return N_alloc_les_param(cols, rows, type, 2);
}

/*!
 * \brief Allocate memory for a (not) quadratic linear equation system which
 * includes the Matrix A and vector x
 *
 * This function calls #N_alloc_les_param
 *
 * \param cols int
 * \param rows int
 * \param type int
 * \return N_les *
 *
 * */
N_les *N_alloc_nquad_les_Ax(int cols, int rows, int type)
{
    return N_alloc_les_param(cols, rows, type, 1);
}

/*!
 * \brief Allocate memory for a (not) quadratic linear equation system which
 * includes the Matrix A
 *
 * This function calls #N_alloc_les_param
 *
 * \param cols int
 * \param rows int
 * \param type int
 * \return N_les *
 *
 * */
N_les *N_alloc_nquad_les_A(int cols, int rows, int type)
{
    return N_alloc_les_param(cols, rows, type, 0);
}

/*!
 * \brief Allocate memory for a (not) quadratic linear equation system which
 * includes the Matrix A, vector x and vector b
 *
 * This function calls #N_alloc_les_param
 *
 * \param cols int
 * \param rows int
 * \param type int
 * \return N_les *
 *
 * */
N_les *N_alloc_nquad_les_Ax_b(int cols, int rows, int type)
{
    return N_alloc_les_param(cols, rows, type, 2);
}

/*!
 * \brief Allocate memory for a quadratic linear equation system which includes
 * the Matrix A, vector x and vector b
 *
 * This function calls #N_alloc_les_param
 *
 * \param rows int
 * \param type int
 * \return N_les *
 *
 * */
N_les *N_alloc_les(int rows, int type)
{
    return N_alloc_les_param(rows, rows, type, 2);
}

/*!
 * \brief Allocate memory for a quadratic linear equation system which includes
 * the Matrix A and vector x
 *
 * This function calls #N_alloc_les_param
 *
 * \param rows int
 * \param type int
 * \return N_les *
 *
 * */
N_les *N_alloc_les_Ax(int rows, int type)
{
    return N_alloc_les_param(rows, rows, type, 1);
}

/*!
 * \brief Allocate memory for a quadratic linear equation system which includes
 * the Matrix A
 *
 * This function calls #N_alloc_les_param
 *
 * \param rows int
 * \param type int
 * \return N_les *
 *
 * */
N_les *N_alloc_les_A(int rows, int type)
{
    return N_alloc_les_param(rows, rows, type, 0);
}

/*!
 * \brief Allocate memory for a quadratic linear equation system which includes
 * the Matrix A, vector x and vector b
 *
 * This function calls #N_alloc_les_param
 *
 * \param rows int
 * \param type int
 * \return N_les *
 *
 * */
N_les *N_alloc_les_Ax_b(int rows, int type)
{
    return N_alloc_les_param(rows, rows, type, 2);
}

/*!
 * \brief Allocate memory for a quadratic or not quadratic linear equation
 * system
 *
 * The type of the linear equation system must be N_NORMAL_LES for
 * a regular quadratic matrix or N_SPARSE_LES for a sparse matrix
 *
 * <p>
 * In case of N_NORMAL_LES
 *
 * A quadratic matrix of size rows*rows*sizeof(double) will allocated
 *
 * <p>
 * In case of N_SPARSE_LES
 *
 * a vector of size row will be allocated, ready to hold additional allocated
 * sparse vectors. each sparse vector may have a different size.
 *
 * Parameter parts defines which parts of the les should be allocated.
 * The number of columns and rows defines if the matrix is quadratic.
 *
 * \param cols int
 * \param rows int
 * \param type int
 * \param parts int -- 2 = A, x and b; 1 = A and x; 0 = A allocated
 * \return N_les *
 *
 * */
N_les *N_alloc_les_param(int cols, int rows, int type, int parts)
{
    N_les *les;

    int i;

    if (type == N_SPARSE_LES)
        G_debug(2,
                "Allocate memory for a sparse linear equation system with %i "
                "rows\n",
                rows);
    else
        G_debug(2,
                "Allocate memory for a regular linear equation system with %i "
                "rows\n",
                rows);

    les = (N_les *)G_calloc(1, sizeof(N_les));

    if (parts > 0) {
        les->x = (double *)G_calloc(cols, sizeof(double));
        for (i = 0; i < cols; i++)
            les->x[i] = 0.0;
    }

    if (parts > 1) {
        les->b = (double *)G_calloc(cols, sizeof(double));
        for (i = 0; i < cols; i++)
            les->b[i] = 0.0;
    }

    les->A = NULL;
    les->Asp = NULL;
    les->rows = rows;
    les->cols = cols;
    if (rows == cols)
        les->quad = 1;
    else
        les->quad = 0;

    if (type == N_SPARSE_LES) {
        les->Asp = G_math_alloc_spmatrix(rows);
        les->type = N_SPARSE_LES;
    }
    else {
        les->A = G_alloc_matrix(rows, cols);
        les->type = N_NORMAL_LES;
    }

    return les;
}

/*!
 *
 * \brief prints the linear equation system to stdout
 *
 * <p>
 * Format:
 * A*x = b
 *
 * <p>
 * Example
 \verbatim

 2 1 1 1 * 2 = 0.1
 1 2 0 0 * 3 = 0.2
 1 0 2 0 * 3 = 0.2
 1 0 0 2 * 2 = 0.1

 \endverbatim
 *
 * \param les N_les *
 * \return void
 *
 * */
void N_print_les(N_les *les)
{
    int i, j, k, out;

    if (les->type == N_SPARSE_LES) {
        for (i = 0; i < les->rows; i++) {
            for (j = 0; j < les->cols; j++) {
                out = 0;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
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
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
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
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
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
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
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
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> osgeo-main
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
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
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
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
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
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
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e77ca8abf8 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a2d0f35a9c (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
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
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 28bb012175 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb2a3a877f (Merge branch 'a0x8o' into stag0)
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
>>>>>>> ab7a7d8f0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 15e753e748 (r.horizon manual - fix typo (#2794))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a7fe10f0c4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 58f3ce8d6f (r.horizon manual - fix typo (#2794))
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
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c73c65622b (r.horizon manual - fix typo (#2794))
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
>>>>>>> b2351aab26 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2540536681 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 27b3d710a4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ca4e88c309 (r.horizon manual - fix typo (#2794))
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
                for (k = 0; (unsigned int)k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == (unsigned int)j) {
=======
                for (k = 0; k < les->Asp[i]->cols; k++) {
                    if (les->Asp[i]->index[k] == j) {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f345ab419f (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 75483c685f (r.horizon manual - fix typo (#2794))
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
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8f016c3797 (r.horizon manual - fix typo (#2794))
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
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
                        fprintf(stdout, "%4.5f ", les->Asp[i]->values[k]);
                        out = 1;
                    }
                }
                if (!out)
                    fprintf(stdout, "%4.5f ", 0.0);
            }
            if (les->x)
                fprintf(stdout, "  *  %4.5f", les->x[i]);
            if (les->b)
                fprintf(stdout, " =  %4.5f ", les->b[i]);

            fprintf(stdout, "\n");
        }
    }
    else {

        for (i = 0; i < les->rows; i++) {
            for (j = 0; j < les->cols; j++) {
                fprintf(stdout, "%4.5f ", les->A[i][j]);
            }
            if (les->x)
                fprintf(stdout, "  *  %4.5f", les->x[i]);
            if (les->b)
                fprintf(stdout, " =  %4.5f ", les->b[i]);

            fprintf(stdout, "\n");
        }
    }
    return;
}

/*!
 * \brief Release the memory of the linear equation system
 *
 * \param les N_les *
 * \return void
 *
 * */

void N_free_les(N_les *les)
{
    if (les->type == N_SPARSE_LES)
        G_debug(2, "Releasing memory of a sparse linear equation system\n");
    else
        G_debug(2, "Releasing memory of a regular linear equation system\n");

    if (les) {

        if (les->x)
            G_free(les->x);
        if (les->b)
            G_free(les->b);

        if (les->type == N_SPARSE_LES) {

            if (les->Asp) {
                G_math_free_spmatrix(les->Asp, les->rows);
            }
        }
        else {

            if (les->A) {
                G_free_matrix(les->A);
            }
        }

        free(les);
    }

    return;
}
