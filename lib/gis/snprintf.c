/*!
 * \file lib/gis/snprintf.c
 *
 * \brief GIS Library - snprintf() clone functions.
 *
 *
 * \todo if needed, implement alternative versions for portability.
 *  potential code source:
 *   - http://www.ijs.si/software/snprintf/
 *   - openssh's snprintf() implementation: bsd-snprintf.c
 *
 * (C) 2001-2014 by the GRASS Development Team
 *
 * This program is free software under the GNU General Public License
 * (>=v2). Read the file COPYING that comes with GRASS for details.
 *
 * \author Markus Neteler
 *
 * \date 2006-2008
 */

#include <stdarg.h>
#include <stdio.h>

#include <grass/gis.h>

/**
 * \brief snprintf() clone.
 *
 * <b>Note:</b> The use of <i>snprintf()</i>/<i>G_snprintf()</i> is
 * discouraged in favour of calculating how long the string will be and
 * allocating enough memory!
 *
 * \deprecated Use C99 standard function snprintf() instead.
 *
 * \param[in] str input string
 * \param[in] size length of string
 * \param[in] fmt
 * \return number of chars written
 */

int G_snprintf(char *str, size_t size, const char *fmt, ...)
{
    va_list ap;
    int count;

    va_start(ap, fmt);
    count = vsnprintf(str, size, fmt, ap);
    va_end(ap);

<<<<<<< HEAD
=======
    /* Windows' vsnprintf() doesn't always NUL-terminate the buffer */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    if (count >= 0 && (unsigned int)count == size)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    if (count >= 0 && (unsigned int)count == size)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
>>>>>>> osgeo-main
    if (count == size)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    if (count >= 0 && (unsigned int)count == size)
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
    if (count == size)
=======
    if (count >= 0 && (unsigned int)count == size)
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
    if (count == size)
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
    if (count >= 0 && (unsigned int)count == size)
=======
    if (count == size)
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
    if (count >= 0 && (unsigned int)count == size)
=======
    if (count == size)
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
=======
>>>>>>> osgeo-main
=======
    if (count >= 0 && (unsigned int)count == size)
=======
    if (count == size)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
        str[--count] = '\0';

>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
    return count;
}
