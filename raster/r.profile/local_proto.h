#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <grass/parson.h>
#include <grass/gis.h>
#include <grass/raster.h>

enum OutputFormat { PLAIN, JSON };

/* main.c */
int do_profile(double, double, double, double, int, double, int, int, FILE *,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
               char *, const char *, double, enum OutputFormat, char *,
               JSON_Array *);

/* read_rast.c */
int read_rast(double, double, double, int, int, RASTER_MAP_TYPE, FILE *, char *,
              enum OutputFormat, char *, JSON_Array *);
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
               char *, const char *, double);

/* read_rast.c */
int read_rast(double, double, double, int, int, RASTER_MAP_TYPE, FILE *,
              char *);
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
               char *, const char *, double, enum OutputFormat, char *,
               JSON_Array *);

/* read_rast.c */
int read_rast(double, double, double, int, int, RASTER_MAP_TYPE, FILE *, char *,
              enum OutputFormat, char *, JSON_Array *);
>>>>>>> 525ec3793d (r.profile: add JSON support (#3872))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)

/* input.c */
int input(char *, char *, char *, char *, char *, FILE *);

extern int clr;
extern struct Colors colors;
