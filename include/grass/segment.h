#ifndef GRASS_SEGMENT_H
#define GRASS_SEGMENT_H

#include <grass/gis.h>

#ifdef HAVE_UNISTD_H
#include <unistd.h>
#endif

#ifdef HAVE_SYS_TYPES_H
#include <sys/types.h>
#endif

struct aq {                     /* age queue */
    int cur;                    /* segment number */
    struct aq *younger, *older; /* pointer to next younger and next older */
};

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
typedef struct SEGMENT {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
typedef struct SEGMENT {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
=======
typedef struct SEGMENT {
=======
>>>>>>> osgeo-main
typedef struct {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
typedef struct {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
typedef struct SEGMENT {
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
typedef struct {
=======
typedef struct SEGMENT {
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
typedef struct SEGMENT {
=======
typedef struct {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
typedef struct {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
typedef struct SEGMENT {
=======
typedef struct {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
typedef struct {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
typedef struct SEGMENT {
=======
typedef struct {
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
typedef struct {
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
    int open;      /* open flag */
    off_t nrows;   /* rows in original data */
    off_t ncols;   /* cols in original data */
    int len;       /* bytes per data value */
    int srows;     /* rows in segments */
    int scols;     /* cols in segments */
    int srowscols; /* rows x cols in segments */
    int size;      /* size in bytes of a segment */
    int spr;       /* segments per row */
    int spill;     /* cols in last segment in row */

    /* fast mode */
    int fast_adrs;  /* toggles fast address mode */
    off_t scolbits; /* column bitshift */
    off_t srowbits; /* row bitshift */
    off_t segbits;  /* segment bitshift */
    int fast_seek;  /* toggles fast seek mode */
    int lenbits;    /* data size bitshift */
    int sizebits;   /* segment size bitshift */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
>>>>>>> osgeo-main
    int (*address)();
    int (*seek)();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    int (*address)();
    int (*seek)();
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
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
    int (*address)();
    int (*seek)();
=======
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
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
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
    int (*address)();
    int (*seek)();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
    int (*address)();
    int (*seek)();
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
    int (*address)();
    int (*seek)();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    int (*address)(const struct SEGMENT *, off_t, off_t, int *, int *);
    int (*seek)(const struct SEGMENT *S, int, int);
=======
    int (*address)();
    int (*seek)();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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

    char *fname; /* segment file name */
    int fd;      /* file descriptor to read/write segment */
    struct scb   /* control blocks */
    {
        char *buf;      /* data buffer */
        char dirty;     /* dirty flag */
        struct aq *age; /* pointer to position in age queue */
        int n;          /* segment number */
    } *scb;
    int *load_idx;       /* index of loaded segments */
    int nfreeslots;      /* number of free slots */
    int *freeslot;       /* array of free slots */
    struct aq *agequeue, /* queue of age for order of access */
        *youngest,       /* youngest in age queue */
        *oldest;         /* oldest in age queue */
    int nseg;            /* number of segments in memory */
    int cur;             /* last accessed segment */
    int offset;          /* offset of data past header */

    char *cache; /* all in memory cache */
} SEGMENT;

#include <grass/defs/segment.h>

#endif /* GRASS_SEGMENT_H */
