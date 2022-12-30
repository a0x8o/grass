/****************************************************************************
 *
 *  MODULE:        r.terraflow
 *
 *  COPYRIGHT (C) 2007 Laura Toma
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *****************************************************************************/

#ifndef NODATA_H
#define NODATA_H

#include <assert.h>

#include <grass/iostream/ami.h>
#include "types.h"
#include "option.h"

/* somewhat of a hack. should read the GRASS nodata value instead
   (which normally is MAX_INT), but, is it worth it? */
#define TERRAFLOW_INTERNAL_NODATA_VALUE -9999

int is_nodata(elevation_type el);
int is_nodata(int x);
int is_nodata(float x);
int is_void(elevation_type el);

class nodataType : public ijBaseType {
public: /* struct, so members public */
    cclabel_type label;
    bool valid;
    static elevation_type ELEVATION_BOUNDARY; /* means this cell is on
                                               * the grid boundary,
                                               * directly, or via
                                               * connect nodata cells */

    static elevation_type ELEVATION_NODATA; /* means we have no data for
                                             * this cell */
public:
    nodataType(dimension_type gi, dimension_type gj, cclabel_type glab)
<<<<<<< HEAD
        : ijBaseType(gi, gj), label(glab), valid(true) {};
    nodataType() : valid(false) {};
=======
        : ijBaseType(gi, gj), label(glab), valid(true){};
    nodataType() : valid(false){};
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    void invalidate() { valid = false; }
    elevation_type getElevation()
    {
        return (label == LABEL_BOUNDARY ? ELEVATION_BOUNDARY
                                        : ELEVATION_NODATA);
    }

    static char *printLabel(const nodataType &p)
    {
        static char buf[8];
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
>>>>>>> osgeo-main
        sprintf(buf, CCLABEL_FMT, p.label);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        sprintf(buf, CCLABEL_FMT, p.label);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
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
        sprintf(buf, CCLABEL_FMT, p.label);
=======
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
        sprintf(buf, CCLABEL_FMT, p.label);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        sprintf(buf, CCLABEL_FMT, p.label);
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
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
        sprintf(buf, CCLABEL_FMT, p.label);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        sprintf(buf, CCLABEL_FMT, p.label);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
        sprintf(buf, CCLABEL_FMT, p.label);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        sprintf(buf, CCLABEL_FMT, p.label);
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
        snprintf(buf, sizeof(buf), CCLABEL_FMT, p.label);
=======
        sprintf(buf, CCLABEL_FMT, p.label);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        sprintf(buf, CCLABEL_FMT, p.label);
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
        sprintf(buf, CCLABEL_FMT, p.label);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
        return buf;
    }

    static void init(elevation_type nodata)
    {
        /*  somewhat of a hack... */
        ELEVATION_NODATA = nodata;
        ELEVATION_BOUNDARY = nodata + 1;
        /* ELEVATION_BOUNDARY = ELEVATION_MIN; */
        /* assert(ELEVATION_NODATA != ELEVATION_MIN); */
    }

    /* LAURA: i added this polymorph because Terraflow has now a FIXED
       internal value for nodata; it does not read GRASS nodata value */
    static void init()
    {
        /* somewhat of a hack... */
        ELEVATION_NODATA = TERRAFLOW_INTERNAL_NODATA_VALUE;
        ELEVATION_BOUNDARY = TERRAFLOW_INTERNAL_NODATA_VALUE + 1;
        /* ELEVATION_BOUNDARY = ELEVATION_MIN; */
        /* assert(ELEVATION_NODATA != ELEVATION_MIN); */
    }

    friend ostream &operator<<(ostream &s, const nodataType &p)
    {
        if (p.valid) {
            return s << "[" << p.i << "," << p.j << "; lbl=" << p.label << "]";
        }
        else {
            return s << "[invalid]";
        }
    }
};

class nodataType2elevation_type {
public:
    elevation_type operator()(nodataType n) { return n.getElevation(); }
    elevation_type operator()(elevation_type n) { return n; }
};

class labelCmpNodataType {
public:
    static int compare(const nodataType &a, const nodataType &b)
    {
        if (a.label < b.label)
            return -1;
        if (a.label > b.label)
            return 1;
        return 0;
    }
};

class ijCmpNodataType {
public:
    static int compare(const nodataType &a, const nodataType &b)
    {
        return ijBaseType::compare(a, b);
    }
};

AMI_STREAM<elevation_type> *classifyNodata(AMI_STREAM<elevation_type> *elstr);

#endif
