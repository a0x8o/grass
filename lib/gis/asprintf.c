/*!
 * \file lib/gis/asprintf.c
 *
 * \brief GIS Library - GRASS implementation of asprintf().
 *
 * Eric G. Miller - Thu, 2 May 2002 17:51:54 -0700
 *
 * Rewritten by Glynn Clements, Sat, 6 Feb 2010
 * Assumes that vsnprintf() is available
 *
 * (C) 2002-2014 by the GRASS Development Team
 * (C) 2010 by Glynn Clements
 *
 * This program is free software under the GNU General Public License
 * (>=v2). Read the file COPYING that comes with GRASS for details.
 */

#define _GNU_SOURCE /* enable asprintf */
#include <stdio.h>
#include <stdarg.h>
#include <string.h>
#include <grass/gis.h>

#ifndef G_asprintf

/**
 * \brief Safe replacement for <i>asprintf()</i>.
 *
 * Allocate a string large enough to hold the new output, including the
 * terminating NULL, and return the number of characters printed. The
 * pointer out is set to the output string and should be passed to
 * <i>G_free()</i> to release the allocated storage when it is no longer
 * needed.
 *
 * \param[out] out
 * \param[in] fmt
 * \param ap
 * \return number of bytes written
 */

int G_vasprintf(char **out, const char *fmt, va_list ap)
{
#ifdef HAVE_ASPRINTF
    return vasprintf(out, fmt, ap);
#else
    size_t size = strlen(fmt) + 50;
    char *buf = G_malloc(size);
    int count;

    for (;;) {
        /* BUG: according to man vsnprintf,
         * va_start() should be called immediately before vsnprintf(),
         * and va_end() immediately after vsnprintf()
         * otherwise there will be memory corruption */
        count = vsnprintf(buf, size, fmt, ap);
        if (count >= 0 && count < size)
            break;
        size *= 2;
        buf = G_realloc(buf, size);
    }

    buf = G_realloc(buf, count + 1);
    *out = buf;

    return count;
#endif /* HAVE_ASPRINTF */
}

int G_asprintf(char **out, const char *fmt, ...)
{
    va_list ap;
    int count;

    va_start(ap, fmt);
    count = G_vasprintf(out, fmt, ap);
    va_end(ap);

    return count;
}

#endif /* G_asprintf */

/**
 * \brief Reallocating version of <i>asprintf()</i>.
 *
 * Reallocate a string large enough to hold the output, including the
 * terminating NULL, and return the number of characters printed.
 * Contrary to <i>G_asprintf()</i>, any existing buffer pointed to by
 * out of size osize is used to hold the output and enlarged if
 * necessary. This is useful when <i>G_rasprintf</i> is called many
 * times in a loop.
 *
 * \param[out] out
 * \param[out] osize
 * \param[in] fmt
 * \param ap
 * \return number of bytes written
 */

int G_rasprintf(char **out, size_t *size, const char *fmt, ...)
{
    va_list ap;
    int count;
    char *buf = *out;
    size_t osize = *size;

    if (osize < strlen(fmt) + 50) {
        osize = strlen(fmt) + 50;
        buf = G_realloc(buf, osize);
    }

    for (;;) {
        va_start(ap, fmt);
        count = vsnprintf(buf, osize, fmt, ap);
        va_end(ap);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        if (count >= 0 && (size_t)count < osize)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (count >= 0 && (size_t)count < osize)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
=======
        if (count >= 0 && (size_t)count < osize)
=======
>>>>>>> osgeo-main
        if (count >= 0 && count < osize)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        if (count >= 0 && count < osize)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        if (count >= 0 && (size_t)count < osize)
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
        if (count >= 0 && count < osize)
=======
        if (count >= 0 && (size_t)count < osize)
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
        if (count >= 0 && (size_t)count < osize)
=======
        if (count >= 0 && count < osize)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (count >= 0 && count < osize)
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
        if (count >= 0 && (size_t)count < osize)
=======
        if (count >= 0 && count < osize)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (count >= 0 && count < osize)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
        if (count >= 0 && (size_t)count < osize)
=======
        if (count >= 0 && count < osize)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if (count >= 0 && count < osize)
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
            break;
        if (count > -1)
            osize = count + 1;
        else
            osize *= 2;

        buf = G_realloc(buf, osize);
    }

    *out = buf;
    *size = osize;

    return count;
}
