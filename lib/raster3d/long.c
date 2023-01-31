#include "raster3d_intern.h"

/*---------------------------------------------------------------------------*/

int Rast3d_long_encode(long *source, unsigned char *dst, int nofNums)
{
    long *src, d;
    int eltLength, nBytes;
    unsigned char *dstStop, tmp;

    eltLength = RASTER3D_LONG_LENGTH;
    nBytes = 8;

    d = 1;

    while (eltLength--) {
        dstStop = dst + nofNums;
        src = source;

        while (dst != dstStop) {
            tmp = ((*src++ / d) % 256);
            if (tmp != 0)
                nBytes = RASTER3D_MIN(nBytes, eltLength);
            *dst++ = tmp;
        }

        d *= 256;
    }

    return RASTER3D_LONG_LENGTH - nBytes;
}

/*---------------------------------------------------------------------------*/

void Rast3d_long_decode(unsigned char *source, long *dst, int nofNums,
                        int longNbytes)
{
    long *dest;
    int eltLength;
    unsigned char *srcStop;

    eltLength = longNbytes;

    source += nofNums * eltLength - 1;

    eltLength--;
    srcStop = source - nofNums;
    dest = dst;
    dest += nofNums - 1;
    while (source != srcStop) {
        *dest = *source--;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
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
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
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
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
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
=======
>>>>>>> osgeo-main
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
        if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
            Rast3d_fatal_error("Rast3d_long_decode: decoded long too long");
        dest--;
    }

    while (eltLength--) {
        srcStop = source - nofNums;
        dest = dst;
        dest += nofNums - 1;
        while (source != srcStop) {
            *dest *= 256;
            *dest += *source--;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
>>>>>>> osgeo-main
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
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
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
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
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
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
=======
>>>>>>> osgeo-main
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
            if ((eltLength >= RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if ((eltLength >= (int)RASTER3D_LONG_LENGTH) && (*dest != 0))
>>>>>>> 7f32ec0a8d (r.horizon manual - fix typo (#2794))
>>>>>>> e632f0f0bb (r.horizon manual - fix typo (#2794))
                Rast3d_fatal_error("Rast3d_long_decode: decoded long too long");
            dest--;
        }
    }
}
