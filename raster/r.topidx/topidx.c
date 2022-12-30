#include <math.h>
#include <grass/gis.h>
#include <grass/raster.h>
#include <grass/glocale.h>
#include "global.h"

int natb;

void initialize(void)
{
    int i, j;

    natb = 0;
    for (i = 0; i < window.rows; i++) {
        for (j = 0; j < window.cols; j++) {
            av(i, j) = window.ns_res * window.ew_res;
            if (is_cv_null(i, j)) {
                natb++;
                Rast_set_d_null_value(&atbv(i, j), 1);
            }
            else {
                atbv(i, j) = UNPROCESSED;
            }
        }
    }
}

void calculate_atanb(void)
{
    int i, j, k, snatb;
    int ncells, nroute, nslp;
    double sum, route[9], tanB[9], dx, dx1, dx2, sumtb, C;
    int nsink;

    dx = window.ew_res;
    dx1 = 1 / dx;
    dx2 = 1 / (1.414 * dx);
    ncells = window.rows * window.cols;
    snatb = natb;

    G_important_message(_("Calculating..."));

    nsink = 0;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
    for (; natb < ncells;) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    for (; natb < ncells;) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
>>>>>>> osgeo-main
    for (iter = 1; natb < ncells; iter++) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    for (; natb < ncells;) {
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
    for (iter = 1; natb < ncells; iter++) {
=======
    for (; natb < ncells;) {
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    for (; natb < ncells;) {
=======
    for (iter = 1; natb < ncells; iter++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
    for (; natb < ncells;) {
=======
    for (iter = 1; natb < ncells; iter++) {
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
    for (; natb < ncells;) {
=======
    for (iter = 1; natb < ncells; iter++) {
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
    for (; natb < ncells;) {
=======
    for (iter = 1; natb < ncells; iter++) {
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
=======
    for (; natb < ncells;) {
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
    for (iter = 1; natb < ncells; iter++) {
=======
    for (; natb < ncells;) {
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
    for (; natb < ncells;) {
=======
    for (iter = 1; natb < ncells; iter++) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
        /*
           for(i=0;i<80;i++)
           fprintf(stderr,"\b");
           fprintf(stderr,"Iteration: %d",iter);
         */
        G_percent(natb - snatb, ncells - snatb, 1);
        for (i = 0; i < window.rows; i++) {
            for (j = 0; j < window.cols; j++) {
                /* skip null values */
                if (is_cv_null(i, j))
                    continue;

                /* skip squares already done */
                if (is_atbv_null(i, j) || !is_atbv_unprocessed(i, j))
                    continue;

                /* check the 8 possible flow directions for
                 * upslope elements without an atb value
                 */
                if (i > 0) {
                    if (j > 0 &&
                        (is_cv_null(i - 1, j - 1) ||
                         cv(i - 1, j - 1) > cv(i, j)) &&
                        !is_atbv_null(i - 1, j - 1) &&
                        is_atbv_unprocessed(i - 1, j - 1))
                        continue;

                    if ((is_cv_null(i - 1, j) || cv(i - 1, j) > cv(i, j)) &&
                        !is_atbv_null(i - 1, j) &&
                        is_atbv_unprocessed(i - 1, j))
                        continue;

                    if (j + 1 < window.cols &&
                        (is_cv_null(i - 1, j + 1) ||
                         cv(i - 1, j + 1) > cv(i, j)) &&
                        !is_atbv_null(i - 1, j + 1) &&
                        is_atbv_unprocessed(i - 1, j + 1))
                        continue;
                }
                if (j > 0 &&
                    (is_cv_null(i, j - 1) || cv(i, j - 1) > cv(i, j)) &&
                    !is_atbv_null(i, j - 1) && is_atbv_unprocessed(i, j - 1))
                    continue;
                if (j + 1 < window.cols &&
                    (is_cv_null(i, j + 1) || cv(i, j + 1) > cv(i, j)) &&
                    !is_atbv_null(i, j + 1) && is_atbv_unprocessed(i, j + 1))
                    continue;
                if (i + 1 < window.rows) {
                    if (j > 0 &&
                        (is_cv_null(i + 1, j - 1) ||
                         cv(i + 1, j - 1) > cv(i, j)) &&
                        !is_atbv_null(i + 1, j - 1) &&
                        is_atbv_unprocessed(i + 1, j - 1))
                        continue;
                    if ((is_cv_null(i + 1, j) || cv(i + 1, j) > cv(i, j)) &&
                        !is_atbv_null(i + 1, j) &&
                        is_atbv_unprocessed(i + 1, j))
                        continue;
                    if (j + 1 < window.cols &&
                        (is_cv_null(i + 1, j + 1) ||
                         cv(i + 1, j + 1) > cv(i, j)) &&
                        !is_atbv_null(i + 1, j + 1) &&
                        is_atbv_unprocessed(i + 1, j + 1))
                        continue;
                }
                /* find the outflow directions and calculate
                 * the sum of weights
                 */
                sum = 0.0;
                for (k = 0; k < 9; k++)
                    route[k] = 0.0;
                nroute = 0;
                if (i > 0) {
                    if (j > 0 && !is_cv_null(i - 1, j - 1) &&
                        cv(i, j) - cv(i - 1, j - 1) > ZERO) {
                        tanB[0] = (cv(i, j) - cv(i - 1, j - 1)) * dx2;
                        route[0] = 0.354 * dx * tanB[0];
                        sum += route[0];
                        nroute++;
                    }
                    if (!is_cv_null(i - 1, j) &&
                        cv(i, j) - cv(i - 1, j) > ZERO) {
                        tanB[1] = (cv(i, j) - cv(i - 1, j)) * dx1;
                        route[1] = 0.5 * dx * tanB[1];
                        sum += route[1];
                        nroute++;
                    }
                    if (j + 1 < window.cols && !is_cv_null(i - 1, j + 1) &&
                        cv(i, j) - cv(i - 1, j + 1) > ZERO) {
                        tanB[2] = (cv(i, j) - cv(i - 1, j + 1)) * dx2;
                        route[2] = 0.354 * dx * tanB[2];
                        sum += route[2];
                        nroute++;
                    }
                }
                if (j > 0 && !is_cv_null(i, j - 1) &&
                    cv(i, j) - cv(i, j - 1) > ZERO) {
                    tanB[3] = (cv(i, j) - cv(i, j - 1)) * dx1;
                    route[3] = 0.5 * dx * tanB[3];
                    sum += route[3];
                    nroute++;
                }
                if (j + 1 < window.cols) {
                    if (!is_cv_null(i, j + 1) &&
                        cv(i, j) - cv(i, j + 1) > ZERO) {
                        tanB[5] = (cv(i, j) - cv(i, j + 1)) * dx1;
                        route[5] = 0.5 * dx * tanB[5];
                        sum += route[5];
                        nroute++;
                    }
                }
                if (i + 1 < window.rows) {
                    if (j > 0 && !is_cv_null(i + 1, j - 1) &&
                        cv(i, j) - cv(i + 1, j - 1) > ZERO) {
                        tanB[6] = (cv(i, j) - cv(i + 1, j - 1)) * dx2;
                        route[6] = 0.354 * dx * tanB[6];
                        sum += route[6];
                        nroute++;
                    }
                    if (!is_cv_null(i + 1, j) &&
                        cv(i, j) - cv(i + 1, j) > ZERO) {
                        tanB[7] = (cv(i, j) - cv(i + 1, j)) * dx1;
                        route[7] = 0.5 * dx * tanB[7];
                        sum += route[7];
                        nroute++;
                    }
                    if (j + 1 < window.cols && !is_cv_null(i + 1, j + 1) &&
                        cv(i, j) - cv(i + 1, j + 1) > ZERO) {
                        tanB[8] = (cv(i, j) - cv(i + 1, j + 1)) * dx2;
                        route[8] = 0.354 * dx * tanB[8];
                        sum += route[8];
                        nroute++;
                    }
                }

                if (!nroute) {
                    G_debug(1, "Sink or boundary node at %d, %d\n", i, j);
                    nsink++;
                    sumtb = 0.0;
                    nslp = 0;
                    if (i > 0) {
                        if (j > 0 && !is_cv_null(i - 1, j - 1)) {
                            sumtb += (cv(i - 1, j - 1) - cv(i, j)) * dx2;
                            nslp++;
                        }
                        if (!is_cv_null(i - 1, j)) {
                            sumtb += (cv(i - 1, j) - cv(i, j)) * dx1;
                            nslp++;
                        }
                        if (j + 1 < window.cols && !is_cv_null(i - 1, j + 1)) {
                            sumtb += (cv(i - 1, j + 1) - cv(i, j)) * dx2;
                            nslp++;
                        }
                    }

                    if (j > 0 && !is_cv_null(i, j - 1)) {
                        sumtb += (cv(i, j - 1) - cv(i, j)) * dx1;
                        nslp++;
                    }
                    if (j + 1 < window.cols && !is_cv_null(i, j + 1)) {
                        sumtb += (cv(i, j + 1) - cv(i, j)) * dx1;
                        nslp++;
                    }
                    if (i + 1 < window.rows) {
                        if (j > 0 && !is_cv_null(i + 1, j - 1)) {
                            sumtb += (cv(i + 1, j - 1) - cv(i, j)) * dx2;
                            nslp++;
                        }
                        if (!is_cv_null(i + 1, j)) {
                            sumtb += (cv(i + 1, j) - cv(i, j)) * dx1;
                            nslp++;
                        }
                        if (j + 1 < window.cols && !is_cv_null(i + 1, j + 1)) {
                            sumtb += (cv(i + 1, j + 1) - cv(i, j)) * dx2;
                            nslp++;
                        }
                    }

                    sumtb /= nslp;
                    if (sumtb > ZERO) {
                        atbv(i, j) = log((av(i, j) / (2 * dx * sumtb)));
                    }
                    else {
                        Rast_set_d_null_value(&atbv(i, j), 1);
                    }
                    natb++;
                    continue;
                }

                C = av(i, j) / sum;
                atbv(i, j) = log(C);
                natb++;

                if (i > 0) {
                    if (j > 0) {
                        av(i - 1, j - 1) += C * route[0];
                    }
                    av(i - 1, j) += C * route[1];
                    if (j + 1 < window.cols) {
                        av(i - 1, j + 1) += C * route[2];
                    }
                }
                if (j > 0) {
                    av(i, j - 1) += C * route[3];
                }
                if (j + 1 < window.cols) {
                    av(i, j + 1) += C * route[5];
                }
                if (i + 1 < window.rows) {
                    if (j > 0) {
                        av(i + 1, j - 1) += C * route[6];
                    }
                    av(i + 1, j) += C * route[7];
                    if (j + 1 < window.cols) {
                        av(i + 1, j + 1) += C * route[8];
                    }
                }
            }
        }
    }
    G_percent(natb - snatb, ncells - snatb, 1);
    G_important_message(_("Number of sinks or boundaries: %d"), nsink);
}
