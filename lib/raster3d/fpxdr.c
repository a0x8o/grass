#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

#include <grass/raster.h>

#include "raster3d_intern.h"

/*---------------------------------------------------------------------------*/

int Rast3d_is_xdr_null_num(const void *num, int isFloat)
{
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    static const char null_bytes[8] = {0xFF, 0xFF, 0xFF, 0xFF,
                                       0xFF, 0xFF, 0xFF, 0xFF};
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
    static const char null_bytes[8] = {(char)0xFF, (char)0xFF, (char)0xFF,
                                       (char)0xFF, (char)0xFF, (char)0xFF,
                                       (char)0xFF, (char)0xFF};
=======
    static const char null_bytes[8] = {0xFF, 0xFF, 0xFF, 0xFF,
                                       0xFF, 0xFF, 0xFF, 0xFF};
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
    static const char null_bytes[8] = {0xFF, 0xFF, 0xFF, 0xFF,
                                       0xFF, 0xFF, 0xFF, 0xFF};
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

    return memcmp(num, null_bytes, isFloat ? 4 : 8) == 0;
}

/*---------------------------------------------------------------------------*/

int Rast3d_is_xdr_null_float(const float *f)
{
    return Rast3d_is_xdr_null_num(f, 1);
}

/*---------------------------------------------------------------------------*/

int Rast3d_is_xdr_null_double(const double *d)
{
    return Rast3d_is_xdr_null_num(d, 0);
}

/*---------------------------------------------------------------------------*/

void Rast3d_set_xdr_null_num(void *num, int isFloat)
{
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    static const char null_bytes[8] = {0xFF, 0xFF, 0xFF, 0xFF,
                                       0xFF, 0xFF, 0xFF, 0xFF};
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
    static const char null_bytes[8] = {(char)0xFF, (char)0xFF, (char)0xFF,
                                       (char)0xFF, (char)0xFF, (char)0xFF,
                                       (char)0xFF, (char)0xFF};
=======
    static const char null_bytes[8] = {0xFF, 0xFF, 0xFF, 0xFF,
                                       0xFF, 0xFF, 0xFF, 0xFF};
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
    static const char null_bytes[8] = {0xFF, 0xFF, 0xFF, 0xFF,
                                       0xFF, 0xFF, 0xFF, 0xFF};
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

    memcpy(num, null_bytes, isFloat ? 4 : 8);
}

/*---------------------------------------------------------------------------*/

void Rast3d_set_xdr_null_double(double *d)
{
    Rast3d_set_xdr_null_num(d, 0);
}

/*---------------------------------------------------------------------------*/

void Rast3d_set_xdr_null_float(float *f)
{
    Rast3d_set_xdr_null_num(f, 1);
}

/*---------------------------------------------------------------------------*/

static size_t xdr_off;

int Rast3d_init_fp_xdr(RASTER3D_Map *map, int misuseBytes)
/* nof addtl bytes allocated for the xdr array so that */
/* the array can also be (mis)used for other purposes */
{
    if (xdr == NULL) {
        xdrLength = map->tileSize * RASTER3D_MAX(map->numLengthExtern,
                                                 map->numLengthIntern) +
                    misuseBytes;
        xdr = Rast3d_malloc(xdrLength);
        if (xdr == NULL) {
            Rast3d_error("Rast3d_init_fp_xdr: error in Rast3d_malloc");
            return 0;
        }
    }
    else if (map->tileSize *
                     RASTER3D_MAX(map->numLengthExtern, map->numLengthIntern) +
                 misuseBytes >
             xdrLength) {
        xdrLength = map->tileSize * RASTER3D_MAX(map->numLengthExtern,
                                                 map->numLengthIntern) +
                    misuseBytes;
        xdr = Rast3d_realloc(xdr, xdrLength);
        if (xdr == NULL) {
            Rast3d_error("Rast3d_init_fp_xdr: error in Rast3d_realloc");
            return 0;
        }
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

static void *xdrTmp;
static int dstType, srcType, type, externLength, eltLength, isFloat, useXdr;
static double tmpValue, *tmp;

int Rast3d_init_copy_to_xdr(RASTER3D_Map *map, int sType)
{
    xdrTmp = xdr;
    useXdr = map->useXdr;
    srcType = sType;

    if (map->useXdr == RASTER3D_USE_XDR)
        xdr_off = 0;

    type = map->type;
    isFloat = (type == FCELL_TYPE);
    externLength = Rast3d_extern_length(type);
    eltLength = Rast3d_length(srcType);
    tmp = &tmpValue;

    return 1;
}

/*---------------------------------------------------------------------------*/

static int xdr_put(const void *src)
{
    if (isFloat) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
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
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
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
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
            return 0;
        G_xdr_put_float((char *)xdr + xdr_off, src);
        xdr_off += RASTER3D_XDR_FLOAT_LENGTH;
    }
    else {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
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
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
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
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
            return 0;
        G_xdr_put_double((char *)xdr + xdr_off, src);
        xdr_off += RASTER3D_XDR_DOUBLE_LENGTH;
    }
    return 1;
}

/*---------------------------------------------------------------------------*/

int Rast3d_copy_to_xdr(const void *src, int nofNum)
{
    int i;

    if (useXdr == RASTER3D_NO_XDR) {
        Rast3d_copy_values(src, 0, srcType, xdrTmp, 0, type, nofNum);
        xdrTmp = G_incr_void_ptr(xdrTmp, nofNum * Rast3d_extern_length(type));
        return 1;
    }

    for (i = 0; i < nofNum; i++, src = G_incr_void_ptr(src, eltLength)) {

        if (Rast3d_is_null_value_num(src, srcType)) {
            Rast3d_set_xdr_null_num(xdrTmp, isFloat);
            xdr_off += externLength;
        }
        else {
            if (type == srcType) {
                if (!xdr_put(src)) {
                    Rast3d_error("Rast3d_copy_to_xdr: writing xdr failed");
                    return 0;
                }
            }
            else {
                if (type == FCELL_TYPE)
                    *((float *)tmp) = (float)*((double *)src);
                else
                    *((double *)tmp) = (double)*((float *)src);
                if (!xdr_put(tmp)) {
                    Rast3d_error("Rast3d_copy_to_xdr: writing xdr failed");
                    return 0;
                }
            }
        }

        xdrTmp = G_incr_void_ptr(xdrTmp, externLength);
    }

    return 1;
}

/*---------------------------------------------------------------------------*/

int Rast3d_init_copy_from_xdr(RASTER3D_Map *map, int dType)
{
    xdrTmp = xdr;
    useXdr = map->useXdr;
    dstType = dType;

    if (useXdr == RASTER3D_USE_XDR)
        xdr_off = 0;

    type = map->type;
    isFloat = (type == FCELL_TYPE);
    externLength = Rast3d_extern_length(type);
    eltLength = Rast3d_length(dstType);
    tmp = &tmpValue;

    return 1;
}

/*---------------------------------------------------------------------------*/

static int xdr_get(void *src)
{
    if (isFloat) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
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
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
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
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_FLOAT_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
            return 0;
        G_xdr_get_float(src, (char *)xdr + xdr_off);
        xdr_off += RASTER3D_XDR_FLOAT_LENGTH;
    }
    else {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
>>>>>>> osgeo-main
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
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
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
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
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > (size_t)xdrLength)
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (xdr_off + RASTER3D_XDR_DOUBLE_LENGTH > xdrLength)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
            return 0;
        G_xdr_get_double(src, (char *)xdr + xdr_off);
        xdr_off += RASTER3D_XDR_DOUBLE_LENGTH;
    }
    return 1;
}

/*---------------------------------------------------------------------------*/

int Rast3d_copy_from_xdr(int nofNum, void *dst)
{
    int i;

    if (useXdr == RASTER3D_NO_XDR) {
        Rast3d_copy_values(xdrTmp, 0, type, dst, 0, dstType, nofNum);
        xdrTmp = G_incr_void_ptr(xdrTmp, nofNum * Rast3d_extern_length(type));
        return 1;
    }

    for (i = 0; i < nofNum; i++, dst = G_incr_void_ptr(dst, eltLength)) {

        if (Rast3d_is_xdr_null_num(xdrTmp, isFloat)) {
            Rast3d_set_null_value(dst, 1, dstType);
            xdr_off += externLength;
        }
        else {
            if (type == dstType) {
                if (!xdr_get(dst)) {
                    Rast3d_error("Rast3d_copy_from_xdr: reading xdr failed");
                    return 0;
                }
            }
            else {
                if (!xdr_get(tmp)) {
                    Rast3d_error("Rast3d_copy_from_xdr: reading xdr failed");
                    return 0;
                }
                if (type == FCELL_TYPE)
                    *((double *)dst) = (double)*((float *)tmp);
                else
                    *((float *)dst) = (float)*((double *)tmp);
            }
        }

        xdrTmp = G_incr_void_ptr(xdrTmp, externLength);
    }

    return 1;
}
