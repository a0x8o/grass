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

#include <sys/types.h>
#ifdef USE_LARGEMEM
#include <sys/mman.h>
#endif
#include <ctype.h>

#if __GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 1)
#include <ostream>
#else
#include <ostream.h>
#endif

#include <iostream>

#include "common.h"

/* globals */

statsRecorder *stats = NULL;
userOptions *opt = NULL;
struct Cell_head *region = NULL;
dimension_type nrows = 0, ncols = 0;

size_t parse_number(const char *s)
{
    size_t n, mult = 1;
    int len = strlen(s);
    if (isalpha(s[len - 1])) {
        switch (s[len - 1]) {
        case 'M':
            mult = 1 << 20;
            break;
        case 'K':
            mult = 1 << 10;
            break;
        default:
            cerr << "bad number format: " << s << endl;
            exit(-1);
            break;
        }
        /* s[len-1] = '\0'; not needed, as it will stop at first invalid char */
    }
    n = atol(s);
    return n * mult;
}

/* ---------------------------------------------------------------------- */
/* is anybody using this?? DELETE ! */

#ifdef USE_LARGEMEM

void *LargeMemory::ptr[LM_HIST];
size_t LargeMemory::len[LM_HIST];
int LargeMemory::next = 0;

#ifndef MAP_ANON
#define MAP_ANON 0
#endif

#ifdef __alpha
#undef MAP_FAILED
#define MAP_FAILED (caddr_t) - 1L
#endif

void *LargeMemory::alloc(size_t leng)
{
    assert(next < LM_HIST);
    void *p = mmap(0, leng, PROT_READ | PROT_WRITE, MAP_ANON, -1, 0);
    if (p == MAP_FAILED) {
        perror("mmap");
        exit(1);
    }
    len[next] = leng;
    ptr[next] = p;
    next++;
    if (stats) {
        char buf[BUFSIZ], buf2[32];
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> osgeo-main
        sprintf(buf, "allocated large memory: %s 0x%lX",
                formatNumber(buf2, leng), (unsigned long)p);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        sprintf(buf, "allocated large memory: %s 0x%lX",
                formatNumber(buf2, leng), (unsigned long)p);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
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
        sprintf(buf, "allocated large memory: %s 0x%lX",
                formatNumber(buf2, leng), (unsigned long)p);
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
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
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
        sprintf(buf, "allocated large memory: %s 0x%lX",
                formatNumber(buf2, leng), (unsigned long)p);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
        sprintf(buf, "allocated large memory: %s 0x%lX",
                formatNumber(buf2, leng), (unsigned long)p);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
        sprintf(buf, "allocated large memory: %s 0x%lX",
                formatNumber(buf2, leng), (unsigned long)p);
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
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
        sprintf(buf, "allocated large memory: %s 0x%lX",
                formatNumber(buf2, leng), (unsigned long)p);
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
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "allocated large memory: %s 0x%lX",
                 formatNumber(buf2, leng), (unsigned long)p);
=======
        sprintf(buf, "allocated large memory: %s 0x%lX",
                formatNumber(buf2, leng), (unsigned long)p);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
        stats->comment(buf);
    }
    return p;
}

void LargeMemory::free(void *p)
{
    int z;
    int i;
    for (i = next - 1; i >= 0; i--) {
        if (ptr[i] == p)
            break;
    }
    assert(i < next && i >= 0); /* must have been allocated before */

#if (defined sun && defined sparc)
    z = munmap((caddr_t)p, len[i]);
#else
    z = munmap(p, len[i]);
#endif
    if (z < 0) {
        perror("munmap");
    }

    if (stats) {
        char buf[BUFSIZ], buf2[32];
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> osgeo-main
        sprintf(buf, "freed large memory: %s 0x%lX", formatNumber(buf2, len[i]),
                (unsigned long)p);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        sprintf(buf, "freed large memory: %s 0x%lX", formatNumber(buf2, len[i]),
                (unsigned long)p);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
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
        sprintf(buf, "freed large memory: %s 0x%lX", formatNumber(buf2, len[i]),
                (unsigned long)p);
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
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
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
        sprintf(buf, "freed large memory: %s 0x%lX", formatNumber(buf2, len[i]),
                (unsigned long)p);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
        sprintf(buf, "freed large memory: %s 0x%lX", formatNumber(buf2, len[i]),
                (unsigned long)p);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
        sprintf(buf, "freed large memory: %s 0x%lX", formatNumber(buf2, len[i]),
                (unsigned long)p);
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
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
        sprintf(buf, "freed large memory: %s 0x%lX", formatNumber(buf2, len[i]),
                (unsigned long)p);
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
=======
>>>>>>> osgeo-main
=======
        snprintf(buf, BUFSIZ, "freed large memory: %s 0x%lX",
                 formatNumber(buf2, len[i]), (unsigned long)p);
=======
        sprintf(buf, "freed large memory: %s 0x%lX", formatNumber(buf2, len[i]),
                (unsigned long)p);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
        stats->comment(buf);
    }

    next--;
    if (next) {
        ptr[i] = ptr[next];
        len[i] = len[next];
    }
}

#endif /*  USE_LARGEMEM */
