#include <string.h>
#include <stdio.h>
#include <math.h>
#include <grass/gis.h>
#include <grass/glocale.h>
#include "ncb.h"
#include "local_proto.h"

void read_weights(const char *filename)
{
    FILE *fp = fopen(filename, "r");
    int i, j;

    ncb.weights = G_malloc(ncb.nsize * sizeof(DCELL *));
    for (i = 0; i < ncb.nsize; i++)
        ncb.weights[i] = G_malloc(ncb.nsize * sizeof(DCELL));

    if (!fp)
        G_fatal_error(_("Unable to open weights file %s"), filename);

    for (i = 0; i < ncb.nsize; i++)
        for (j = 0; j < ncb.nsize; j++)
            if (fscanf(fp, "%lf", &ncb.weights[i][j]) != 1)
                G_fatal_error(_("Error reading weights file %s"), filename);

    fclose(fp);
}

double gaussian(double factor, double squared_distance)
<<<<<<< HEAD
<<<<<<< HEAD
{
    double sigma2 = factor * factor;
=======
{
    double sigma2 = factor * factor;
=======
{
    double sigma2 = factor * factor;

    return exp(-squared_distance / (2 * sigma2)) / (2 * M_PI * sigma2);
}

double exponential(double factor, double squared_distance)
{
    return exp(factor * sqrt(squared_distance));
}

void compute_weights(const char *function_type, double factor)
{
    int i, j;
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
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f3162d6aeb (r.report: add default units, change to full unit names (#1666))
    double (*weight)(double, double);
=======
    double (*weight) (double, double);
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
=======
    double (*weight) (double, double);
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
=======
    double (*weight)(double, double);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    double (*weight)(double, double);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
=======
=======
    double (*weight) (double, double);
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3162d6aeb (r.report: add default units, change to full unit names (#1666))

    if (!strcmp(function_type, "gaussian")) {
        weight = gaussian;
    }
    else if (!strcmp(function_type, "exponential")) {
        weight = exponential;
    }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 48db7d0390 (r.report: add default units, change to full unit names (#1666))
=======
=======

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======

>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3162d6aeb (r.report: add default units, change to full unit names (#1666))

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======

>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))

    return exp(-squared_distance / (2 * sigma2)) / (2 * M_PI * sigma2);
}

double exponential(double factor, double squared_distance)
{
    return exp(factor * sqrt(squared_distance));
}

void compute_weights(const char *function_type, double factor)
{
    int i, j;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))
    double (*weight)(double, double);
=======
    double (*weight) (double, double);
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
=======
    double (*weight) (double, double);
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
=======
    double (*weight)(double, double);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
    double (*weight)(double, double);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    double (*weight)(double, double);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))

    if (!strcmp(function_type, "gaussian")) {
        weight = gaussian;
    }
    else if (!strcmp(function_type, "exponential")) {
        weight = exponential;
    }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======

>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
{
    double sigma2 = factor * factor;
>>>>>>> osgeo-main
=======
=======

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 7c50c23a6b (r.report: add default units, change to full unit names (#1666))

    return exp(-squared_distance / (2 * sigma2)) / (2 * M_PI * sigma2);
}

double exponential(double factor, double squared_distance)
{
    return exp(factor * sqrt(squared_distance));
}

void compute_weights(const char *function_type, double factor)
{
    int i, j;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    double (*weight)(double, double);
=======
    double (*weight) (double, double);
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    double (*weight) (double, double);
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
=======
    double (*weight)(double, double);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    double (*weight)(double, double);
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
=======
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
=======
=======
    double (*weight) (double, double);
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
=======
=======
    double (*weight) (double, double);
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))
=======
<<<<<<< HEAD
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
=======
=======
    double (*weight) (double, double);
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))
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
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
=======
=======
    double (*weight) (double, double);
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

    if (!strcmp(function_type, "gaussian")) {
        weight = gaussian;
    }
    else if (!strcmp(function_type, "exponential")) {
        weight = exponential;
    }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
{
    double sigma2 = factor * factor;
>>>>>>> osgeo-main
=======
=======
=======
=======
=======
=======
=======
=======

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9f5f54c7c3 (r.report: add default units, change to full unit names (#1666))
=======
=======

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======

>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 29da11ce98 (r.report: add default units, change to full unit names (#1666))

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> ff88ef2b50 (r.report: add default units, change to full unit names (#1666))
=======
=======

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======

>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> f3a6d92ee7 (r.report: add default units, change to full unit names (#1666))

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 9e11460799 (r.report: add default units, change to full unit names (#1666))
=======
=======

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======

>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 85cdcccc73 (r.report: add default units, change to full unit names (#1666))

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
>>>>>>> 88558f8037 (r.report: add default units, change to full unit names (#1666))
=======
=======

>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======

>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
>>>>>>> 894e4068d0 (r.report: add default units, change to full unit names (#1666))

    return exp(-squared_distance / (2 * sigma2)) / (2 * M_PI * sigma2);
}

double exponential(double factor, double squared_distance)
{
    return exp(factor * sqrt(squared_distance));
}

void compute_weights(const char *function_type, double factor)
{
    int i, j;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
    double (*weight)(double, double);
=======
    double (*weight) (double, double);
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======
    double (*weight) (double, double);
>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))
=======
    double (*weight)(double, double);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    double (*weight)(double, double);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    double (*weight)(double, double);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    double (*weight)(double, double);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    double (*weight)(double, double);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    double (*weight)(double, double);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))

    if (!strcmp(function_type, "gaussian")) {
        weight = gaussian;
    }
    else if (!strcmp(function_type, "exponential")) {
        weight = exponential;
    }
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
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======

>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a025896dba (r.report: add default units, change to full unit names (#1666))
=======

>>>>>>> 1dffc5dfd4 (r.report: add default units, change to full unit names (#1666))

=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    ncb.weights = G_malloc(ncb.nsize * sizeof(DCELL *));
    for (i = 0; i < ncb.nsize; i++)
        ncb.weights[i] = G_malloc(ncb.nsize * sizeof(DCELL));

    for (i = 0; i < ncb.nsize; i++) {
        double y = i - ncb.dist;

        for (j = 0; j < ncb.nsize; j++) {
            double x = j - ncb.dist;

            ncb.weights[i][j] = weight(factor, x * x + y * y);
        }
    }
}
