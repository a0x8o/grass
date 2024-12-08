/*
 *  Calculates univariate statistics from the non-null cells
 *
 *   Copyright (C) 2004-2010 by the GRASS Development Team
 *   Author(s): Soeren Gebbert
 *              Based on r.univar from Hamish Bowman, University of Otago, New
 *              Zealand and Martin Landa zonal loop by Markus Metz
 *
 *      This program is free software under the GNU General Public
 *      License (>=v2). Read the file COPYING that comes with GRASS
 *      for details.
 *
 */

#ifndef _GLOBALS_H_
#define _GLOBALS_H_

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <grass/gis.h>
#include <grass/raster3d.h>
#include <grass/raster.h>
#include <grass/glocale.h>

/*- Parameters and global variables -----------------------------------------*/
typedef struct {
    double sum;
    double sumsq;
    double min;
    double max;
    unsigned int n_perc;
    double *perc;
    double sum_abs;
    size_t n;
    size_t size;
    DCELL *dcell_array;
    FCELL *fcell_array;
    CELL *cell_array;
    int map_type;
    void *nextp;
    size_t n_alloc;
    int first;
} univar_stat;

typedef struct {
    CELL min, max, n_zones;
    struct Categories cats;
    char *sep;
} zone_type;

/* command line options are the same for raster and raster3d maps */
typedef struct {
    struct Option *inputfile, *zonefile, *percentile, *output_file, *separator,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cbd32f6608 (r.univar: add JSON support (#3783))
        *nprocs, *format;
=======
        *nprocs;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        *nprocs;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        *nprocs, *format;
>>>>>>> 4fd6484bbb (r.univar: add JSON support (#3783))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        *nprocs;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cbd32f6608 (r.univar: add JSON support (#3783))
    struct Flag *shell_style, *extended, *table, *use_rast_region;
} param_type;

extern param_type param;
extern zone_type zone_info;

enum OutputFormat { PLAIN, JSON };

/* fn prototypes */
void heapsort_double(double *data, size_t n);
void heapsort_float(float *data, size_t n);
void heapsort_int(int *data, size_t n);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cbd32f6608 (r.univar: add JSON support (#3783))
int print_stats(univar_stat *stats, enum OutputFormat format);
=======
int print_stats(univar_stat *stats);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
int print_stats(univar_stat *stats);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
int print_stats(univar_stat *stats, enum OutputFormat format);
>>>>>>> 4fd6484bbb (r.univar: add JSON support (#3783))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
int print_stats(univar_stat *stats);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cbd32f6608 (r.univar: add JSON support (#3783))
int print_stats_table(univar_stat *stats);
univar_stat *create_univar_stat_struct(int map_type, int n_perc);
void free_univar_stat_struct(univar_stat *stats);

#endif
