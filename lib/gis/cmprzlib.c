/*****************************************************************************
 *                     -- GRASS Development Team --
 *
 * MODULE:      GRASS gis library
 * FILENAME:    cmprzlib.c
 * AUTHOR(S):   Eric G. Miller <egm2@jps.net>
 *              Markus Metz
 * PURPOSE:     To provide an interface to libz for compressing and
 *              decompressing data using DEFLATE.  It's primary use is in
 *              the storage and reading of GRASS floating point rasters.
 *              It replaces the patented LZW compression interface.
 *
 * ALGORITHM:   http://www.gzip.org/zlib/feldspar.html
 * DATE CREATED: Dec 17 2015
 * COPYRIGHT:   (C) 2015 by the GRASS Development Team
 *
 *              This program is free software under the GNU General Public
 *              License (version 2 or greater). Read the file COPYING that
 *              comes with GRASS for details.
 *
 *****************************************************************************/

/********************************************************************
 * int                                                              *
 * G_zlib_compress (src, srz_sz, dst, dst_sz)                       *
 *     int src_sz, dst_sz;                                          *
 *     unsigned char *src, *dst;                                    *
 * ---------------------------------------------------------------- *
 * This function is a wrapper around the zlib deflate() function.   *
 * It uses an all or nothing call to deflate().  If you need a      *
 * continuous compression scheme, you'll have to code your own.     *
 * In order to do a single pass compression, the input src must be  *
 * copied to a buffer 1% + 12 bytes larger than the data.  This may *
 * cause performance degradation.                                   *
 *                                                                  *
 * The function either returns the number of bytes of compressed    *
 * data in dst, or an error code.                                   *
 *                                                                  *
 * Errors include:                                                  *
 *        -1 -- Compression failed.                                 *
 *        -2 -- dst is too small.                                   *
 *                                                                  *
 * ================================================================ *
 * int                                                              *
 * G_zlib_expand (src, src_sz, dst, dst_sz)                         *
 *     int src_sz, dst_sz;                                          *
 *     unsigned char *src, *dst;                                    *
 * ---------------------------------------------------------------- *
 * This function is a wrapper around the zlib inflate() function.   *
 * It uses a single pass call to inflate().  If you need a contin-  *
 * uous expansion scheme, you'll have to code your own.             *
 *                                                                  *
 * The function returns the number of bytes expanded into 'dst' or  *
 * and error code.                                                  *
 *                                                                  *
 * Errors include:                                                  *
 *        -1 -- Expansion failed.                                   *
 *                                                                  *
 ********************************************************************
 */

#include <grass/config.h>

#ifndef HAVE_ZLIB_H

#error "GRASS requires libz to compile"

#else

#include <zlib.h>
#include <grass/gis.h>
#include <grass/glocale.h>

#include "G.h"

int G_zlib_compress_bound(int src_sz)
{
    /* from zlib.h:
     * "when using compress or compress2,
     * destLen must be at least the value returned by
     * compressBound(sourceLen)"
     * no explanation for the "must be"
     */
    return compressBound(src_sz);
}

int G_zlib_compress(unsigned char *src, int src_sz, unsigned char *dst,
                    int dst_sz)
{
    uLong err, nbytes, buf_sz;
    unsigned char *buf;

    /* Catch errors early */
    if (src == NULL || dst == NULL) {
        if (src == NULL)
            G_warning(_("No source buffer"));

        if (dst == NULL)
            G_warning(_("No destination buffer"));
        return -1;
    }

    /* Don't do anything if either of these are true */
    if (src_sz <= 0 || dst_sz <= 0) {
        if (src_sz <= 0)
            G_warning(_("Invalid source buffer size %d"), src_sz);
        if (dst_sz <= 0)
            G_warning(_("Invalid destination buffer size %d"), dst_sz);
        return 0;
    }

    /* Output buffer has to be 1% + 12 bytes bigger for single pass deflate */
    /* buf_sz = (int)((double)dst_sz * 1.01 + (double)12); */

    /* Output buffer should be large enough for single pass compression */
    buf = dst;
    buf_sz = G_zlib_compress_bound(src_sz);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
    if (buf_sz > dst_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
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
    if (buf_sz > dst_sz) {
=======
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
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
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
    if (buf_sz > dst_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
    if (buf_sz > dst_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    if (dst_sz < 0 || buf_sz > (unsigned int)dst_sz) {
=======
    if (buf_sz > dst_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
        G_warning(
            "G_zlib_compress(): programmer error, destination is too small");
        if (NULL ==
            (buf = (unsigned char *)G_calloc(buf_sz, sizeof(unsigned char))))
            return -1;
    }
    else
        buf_sz = dst_sz;

    /* Valid zlib compression levels -1 - 9 */
    /* zlib default: Z_DEFAULT_COMPRESSION = -1, equivalent to 6
     * as used here, 1 gives the best compromise between speed and compression
     */

    /* Do single pass compression */
    nbytes = buf_sz;
    err = compress2((Bytef *)buf, &nbytes,      /* destination */
                    (const Bytef *)src, src_sz, /* source */
                    G__.compression_level);     /* level */

    if (err != Z_OK) {
        G_warning(_("ZLIB compression error %d: %s"), (int)err, zError(err));
        if (buf != dst)
            G_free(buf);
        return -1;
    }

    /* updated buf_sz is bytes of compressed data */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
>>>>>>> osgeo-main
    if (nbytes >= src_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
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
    if (nbytes >= src_sz) {
=======
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
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
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
    if (nbytes >= src_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
    if (nbytes >= src_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    if (src_sz < 0 || nbytes >= (unsigned int)src_sz) {
=======
    if (nbytes >= src_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
        /* compression not possible */
        if (buf != dst)
            G_free(buf);
        return -2;
    }

    if (buf != dst) {
        /* Copy the data from buf to dst */
        for (err = 0; err < nbytes; err++)
            dst[err] = buf[err];

        G_free(buf);
    }

    return nbytes;
} /* G_zlib_compress() */

int G_zlib_expand(unsigned char *src, int src_sz, unsigned char *dst,
                  int dst_sz)
{
    int err;
    uLong ss, nbytes;

    /* Catch error condition */
    if (src == NULL || dst == NULL) {
        if (src == NULL)
            G_warning(_("No source buffer"));

        if (dst == NULL)
            G_warning(_("No destination buffer"));
        return -2;
    }

    /* Don't do anything if either of these are true */
    if (src_sz <= 0 || dst_sz <= 0) {
        if (src_sz <= 0)
            G_warning(_("Invalid source buffer size %d"), src_sz);
        if (dst_sz <= 0)
            G_warning(_("Invalid destination buffer size %d"), dst_sz);
        return 0;
    }

    ss = src_sz;

    /* Do single pass decompression */
    nbytes = dst_sz;
    err = uncompress((Bytef *)dst, &nbytes,   /* destination */
                     (const Bytef *)src, ss); /* source */

    /* If not Z_OK return error -1 */
    if (err != Z_OK) {
        G_warning(_("ZLIB decompression error %d: %s"), err, zError(err));
        return -1;
    }

    /* Number of bytes inflated to output stream is
     * updated buffer size
     */

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
>>>>>>> osgeo-main
    if (nbytes != dst_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
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
    if (nbytes != dst_sz) {
=======
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
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
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
    if (nbytes != dst_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
    if (nbytes != dst_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    if (dst_sz < 0 || nbytes != (unsigned int)dst_sz) {
=======
    if (nbytes != dst_sz) {
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
        /* TODO: it is not an error if destination is larger than needed */
        G_warning(_("Got uncompressed size %d, expected %d"), (int)nbytes,
                  dst_sz);
        return -1;
    }

    return nbytes;
} /* G_zlib_expand() */

#endif /* HAVE_ZLIB_H */

/* vim: set softtabstop=4 shiftwidth=4 expandtab: */
