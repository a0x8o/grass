#include <grass/gis.h>
#include <grass/vector.h>

struct value {
    int cat;   /* category */
    char used; /* update/report if used else not */
    int count1,
        count2; /* Count of found values; i1: count, coor, sides; i2: sides */
    /* for sides set to 2, if more than 1 area category was found, */
    /* including no category (cat = -1)! */
    int i1, i2; /* values; i1: query (result int), sides; i2: sides */
    double d1, d2, d3, d4; /* values (length, area, x/y/z, bbox, query) */
    char *str1;            /* string value (query) */
    int *qcat;             /* array query categories */
    int nqcats;            /* number of query cats */
    int aqcats;            /* number of allocated query cats */
    char null;             /* no records selected by query */
};

extern struct value *Values;

struct options {
    char *name;
    int field;
    char *col[4];
    char *qcol;
    int type;
    int option;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    int print; /* print only */
    int sql;   /* print only sql statements */
    int total; /* print totals */
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
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
    int print;        /* print only */
    int print_header; /* print header for print and total */
    int sql;          /* print only sql statements */
    int total;        /* print totals */
=======
    int print; /* print only */
    int sql;   /* print only sql statements */
    int total; /* print totals */
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
=======
    int print; /* print only */
    int sql;   /* print only sql statements */
    int total; /* print totals */
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
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
    int units;
    int qfield; /* query field */
    char *fs;
};

extern struct options options;

struct vstat {
    int rcat;     /* number of categories read from map */
    int select;   /* number of categories selected from DB */
    int exist;    /* number of cats existing in selection from DB */
    int notexist; /* number of cats not existing in selection from DB */
    int dupl;     /* number of cats with duplicate elements (currently
                     O_COOR only)*/
    int update;   /* number of updated rows */
    int error;    /* number of errors */
    int qtype;    /* C type of query column */
};

extern struct vstat vstat;

#define O_CAT       1
#define O_AREA      2
#define O_LENGTH    3
#define O_COUNT     4
#define O_COOR      5 /* Point coordinates */

/* Query database records linked by another field (qfield) */
#define O_QUERY     6
#define O_SIDES     7 /* Left and right area of boundary */
#define O_COMPACT   8 /* Compactness of an area. Circle = 1.0 */
#define O_PERIMETER 9

#define O_START     10 /* line/boundary starting point */
#define O_END       11 /* line/boundary end point */

#define O_SLOPE     12 /* Line slope */

#define O_FD        13 /* fractal dimension */

/* sinuousity of a line (length / <distance between end points>) */
#define O_SINUOUS   14

#define O_AZIMUTH   15 /* line azimuth */

#define O_BBOX      16 /* bounding box */

/* areas.c */
int read_areas(struct Map_info *);

/* calc.c */
double length(register int, register double *, register double *);

/* find.c */
int find_cat(int, int);

/* line.c */
int read_lines(struct Map_info *);

/* parse.c */
int parse_command_line(int, char *[]);

/* query.c */
int query(struct Map_info *);

/* report.c */
int report(void);
int print_stat(void);

/* units.c */
int conv_units(void);

/* update.c */
int update(struct Map_info *);
