/***************************************************************
 *
 * MODULE:       v.delaunay
 *
 * AUTHOR(S):    Martin Pavlovsky (Google SoC 2008, Paul Kelly mentor)
 *               Based on "dct" by Geoff Leach, Department of Computer
 *               Science, RMIT.
 *
 * PURPOSE:      Creates a Delaunay triangulation vector map
 *
 * COPYRIGHT:    (C) RMIT 1993
 *               (C) 2008-2009 by the GRASS Development Team
 *
 *               This program is free software under the GNU General
 *               Public License (>=v2).  Read the file COPYING that
 *               comes with GRASS for details.
 *
 * The following notices apply to portions of the code originally
 * derived from work by Geoff Leach of RMIT:
 *
 *   Author: Geoff Leach, Department of Computer Science, RMIT.
 *   email: gl@cs.rmit.edu.au
 *
 *   Date: 6/10/93
 *
 *   Version 1.0
 *
 *   Copyright (c) RMIT 1993. All rights reserved.
 *
 *   License to copy and use this software purposes is granted provided
 *   that appropriate credit is given to both RMIT and the author.
 *
 *   License is also granted to make and use derivative works provided
 *   that appropriate credit is given to both RMIT and the author.
 *
 *   RMIT makes no representations concerning either the merchantability
 *   of this software or the suitability of this software for any particular
 *   purpose.  It is provided "as is" without express or implied warranty
 *   of any kind.
 *
 *   These notices must be retained in any copies of any part of this software.
 *
 **************************************************************/

#include <stdlib.h>
#include <grass/gis.h>
#include <grass/glocale.h>
#include "defs.h"
#include "data_types.h"

static struct edge *edges;
static struct edge **free_list_e;

static unsigned int n_free_e;

void alloc_memory(unsigned int n)
{
    struct edge *e;
    unsigned int i;

    /* Sites storage. */
    sites = (struct vertex *)G_calloc(n, sizeof(struct vertex));
    if (sites == NULL)
        G_fatal_error(_("Not enough memory."));

    /* Edges. Euler's formula - at most 3n edges on a set of n sites */
    n_free_e = 3 * n;
    edges = e = (struct edge *)G_calloc(n_free_e, sizeof(struct edge));
    if (edges == NULL)
        G_fatal_error(_("Not enough memory."));

    free_list_e = (struct edge **)G_calloc(n_free_e, sizeof(struct edge *));
    if (free_list_e == NULL)
        G_fatal_error(_("Not enough memory."));
    for (i = 0; i < n_free_e; i++, e++)
        free_list_e[i] = e;
}

void alloc_sites(unsigned int n)
{
    /* Sites storage. */
    sites = (struct vertex *)G_calloc(n, sizeof(struct vertex));
    if (sites == NULL)
        G_fatal_error(_("Not enough memory."));
}

void realloc_sites(unsigned int n)
{
    /* Sites storage. */
    sites = (struct vertex *)G_realloc(sites, n * sizeof(struct vertex));
    if (sites == NULL)
        G_fatal_error(_("Not enough memory."));
}

void alloc_edges(unsigned int n)
{
    struct edge *e;
    unsigned int i;

    /* Edges. Euler's formula - at most 3n edges on a set of n sites */
    n_free_e = 3 * n;
    edges = e = (struct edge *)G_calloc(n_free_e, sizeof(struct edge));
    if (edges == NULL)
        G_fatal_error(_("Not enough memory."));

    free_list_e = (struct edge **)G_calloc(n_free_e, sizeof(struct edge *));
    if (free_list_e == NULL)
        G_fatal_error(_("Not enough memory."));
    for (i = 0; i < n_free_e; i++, e++)
        free_list_e[i] = e;
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
void free_memory(void)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void free_memory(void)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
void free_memory(void)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
void free_memory()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
void free_memory(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
void free_memory()
=======
void free_memory(void)
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
void free_memory(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
void free_memory()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void free_memory(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
void free_memory(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
void free_memory()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void free_memory(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
void free_memory(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
void free_memory()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void free_memory(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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
{
    G_free(sites);
    G_free(edges);
    G_free(free_list_e);
}

struct edge *get_edge(void)
{
    if (n_free_e < 1)
        G_fatal_error(_("All allocated edges have been used."));
    return (free_list_e[--n_free_e]);
}

void free_edge(struct edge *e)
{
    free_list_e[n_free_e++] = e;
}
