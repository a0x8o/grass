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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
{
    double sigma2 = factor * factor;
>>>>>>> osgeo-main
=======
=======
=======
=======

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
=======

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
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
