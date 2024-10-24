/*!
   \file lib/vector/diglib/struct_alloc.c

   \brief Vector library - allocate and zero array space (lower level functions)

   Lower level functions for reading/writing/manipulating vectors.

   These routines all eventually call calloc() to allocate and zero the
   new space. BUT It is not necessarily safe to assume that the memory
   will be zero. The next memory location asked for could have been
   previously used and not zeroed. (e.g. compress()).

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author CERL (probably Dave Gerdes)
   \author Radim Blazek
 */

#include <stdlib.h>
#include <grass/vector.h>
#include <grass/glocale.h>

/*!
   \brief Allocate new node structure

   \return pointer to allocated P_node struct
   \return NULL on error
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
struct P_node *dig_alloc_node(void)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
struct P_node *dig_alloc_node(void)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
struct P_node *dig_alloc_node(void)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_node *dig_alloc_node()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
struct P_node *dig_alloc_node(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
struct P_node *dig_alloc_node()
=======
struct P_node *dig_alloc_node(void)
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
struct P_node *dig_alloc_node(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_node *dig_alloc_node()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_node *dig_alloc_node(void)
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
struct P_node *dig_alloc_node(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_node *dig_alloc_node()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_node *dig_alloc_node(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
struct P_node *dig_alloc_node(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_node *dig_alloc_node()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_node *dig_alloc_node(void)
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
    struct P_node *Node;

    Node = (struct P_node *)G_malloc(sizeof(struct P_node));
    if (Node == NULL)
        return NULL;

    G_zero(Node, sizeof(struct P_node));

    return Node;
}

/*!
   \brief Free node structure

   \param Node pointer to P_node struct to be freed
 */
void dig_free_node(struct P_node *Node)
{
    if (Node->alloc_lines > 0) {
        G_free(Node->lines);
        G_free(Node->angles);
    }

    G_free(Node);
}

/*!
   \brief Allocate space in P_node struct

   Lines and angles arrays to add 'add' more lines

   \param node pointer to P_node struct
   \param add number lines to be added

   \return 0 on success
   \return -1 on error
 */
int dig_node_alloc_line(struct P_node *node, int add)
{
    int num;
    char *p;

    G_debug(5, "dig_node_alloc_line(): add = %d", add);

    if (node->n_lines + add <= node->alloc_lines)
        return 0;

    num = node->alloc_lines + add;

    p = G_realloc(node->lines, num * sizeof(plus_t));
    if (p == NULL)
        return -1;
    node->lines = (plus_t *)p;

    p = G_realloc(node->angles, num * sizeof(float));
    if (p == NULL)
        return -1;
    node->angles = (float *)p;

    node->alloc_lines = num;

    return 0;
}

/*!
   \brief Reallocate array of pointers to nodes

   \param Plus pointer to Plus_head structure
   \param add number of nodes to be added

   \return 0 on success
   \return -1 on error
 */
int dig_alloc_nodes(struct Plus_head *Plus, int add)
{
    int size;
    char *p;

    size = Plus->alloc_nodes + 1 + add;
    p = G_realloc(Plus->Node, size * sizeof(struct P_node *));
    if (p == NULL)
        return -1;

    Plus->Node = (struct P_node **)p;
    Plus->alloc_nodes = size - 1;

    return 0;
}

/*!
   \brief Allocate new line structure

   \return pointer to allocated P_node struct
   \return NULL on error
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
struct P_line *dig_alloc_line(void)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
struct P_line *dig_alloc_line(void)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
struct P_line *dig_alloc_line(void)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_line *dig_alloc_line()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
struct P_line *dig_alloc_line(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
struct P_line *dig_alloc_line()
=======
struct P_line *dig_alloc_line(void)
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
struct P_line *dig_alloc_line(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_line *dig_alloc_line()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_line *dig_alloc_line(void)
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
struct P_line *dig_alloc_line(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_line *dig_alloc_line()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_line *dig_alloc_line(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
struct P_line *dig_alloc_line(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_line *dig_alloc_line()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_line *dig_alloc_line(void)
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
    struct P_line *Line;

    Line = (struct P_line *)G_malloc(sizeof(struct P_line));
    if (Line == NULL)
        return NULL;

    G_zero(Line, sizeof(struct P_line));

    return Line;
}

/*!
   \brief Allocate new topo struct

   \param type to of struct to allocate
 */
void *dig_alloc_topo(char type)
{
    void *Topo = NULL;

    switch (type) {
    case GV_LINE:
        Topo = G_malloc(sizeof(struct P_topo_l));
        break;
    case GV_BOUNDARY:
        Topo = G_malloc(sizeof(struct P_topo_b));
        break;
    case GV_CENTROID:
        Topo = G_malloc(sizeof(struct P_topo_c));
        break;
    case GV_FACE:
        Topo = G_malloc(sizeof(struct P_topo_f));
        break;
    case GV_KERNEL:
        Topo = G_malloc(sizeof(struct P_topo_k));
        break;
    default:
        return NULL;
    }

    return Topo;
}

/*!
   \brief Free line structure

   \param pointer to P_line struct to be freed
 */
void dig_free_line(struct P_line *Line)
{
    if (Line->topo)
        G_free(Line->topo);
    G_free(Line);
}

/*!
   \brief Reallocate array of pointers to lines.

   \param Plus pointer to Plus_head structure
   \param add space for 'add' number of lines is added.

   \return 0 on success
   \return -1 on error
 */
int dig_alloc_lines(struct Plus_head *Plus, int add)
{
    int size;
    char *p;

    size = Plus->alloc_lines + 1 + add;
    p = G_realloc(Plus->Line, size * sizeof(struct P_line *));
    if (p == NULL)
        return -1;

    Plus->Line = (struct P_line **)p;
    Plus->alloc_lines = size - 1;

    return 0;
}

/*!
   \brief Reallocate array of pointers to areas.

   \param Plus pointer to Plus_head structure
   \param add space for 'add' number of areas is added

   \return 0 on success
   \return -1 on error
 */
int dig_alloc_areas(struct Plus_head *Plus, int add)
{
    int size;
    char *p;

    size = Plus->alloc_areas + 1 + add;
    p = G_realloc(Plus->Area, size * sizeof(struct P_area *));
    if (p == NULL)
        return -1;

    Plus->Area = (struct P_area **)p;
    Plus->alloc_areas = size - 1;

    return 0;
}

/*!
   \brief Reallocate array of pointers to isles

   \param Plus pointer to Plus_head structure
   \param add space for 'add' number of isles is added.

   \return 0 on success
   \return -1 on error
 */
int dig_alloc_isles(struct Plus_head *Plus, int add)
{
    int size;
    char *p;

    G_debug(5, "dig_alloc_isle():");
    size = Plus->alloc_isles + 1 + add;
    p = G_realloc(Plus->Isle, size * sizeof(struct P_isle *));
    if (p == NULL)
        return -1;

    Plus->Isle = (struct P_isle **)p;
    Plus->alloc_isles = size - 1;

    return 0;
}

/*!
   \brief Allocate new area structure

   \return pointer to allocated P_area struct
   \return NULL on error
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
struct P_area *dig_alloc_area(void)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
struct P_area *dig_alloc_area(void)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
struct P_area *dig_alloc_area(void)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_area *dig_alloc_area()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
struct P_area *dig_alloc_area(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
struct P_area *dig_alloc_area()
=======
struct P_area *dig_alloc_area(void)
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
struct P_area *dig_alloc_area(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_area *dig_alloc_area()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_area *dig_alloc_area(void)
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
struct P_area *dig_alloc_area(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_area *dig_alloc_area()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_area *dig_alloc_area(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
struct P_area *dig_alloc_area(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_area *dig_alloc_area()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_area *dig_alloc_area(void)
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
    struct P_area *Area;

    Area = (struct P_area *)G_malloc(sizeof(struct P_area));
    if (Area == NULL)
        return NULL;

    G_zero(Area, sizeof(struct P_area));

    return Area;
}

/*!
   \brief Free area structure

   \param Area pointer to P_area struct to be freed
 */
void dig_free_area(struct P_area *Area)
{
    if (Area->alloc_lines > 0)
        free(Area->lines);

    if (Area->alloc_isles > 0)
        free(Area->isles);

    G_free(Area);
}

/*!
   \brief Allocate new isle structure

   \return pointer to allocated P_isle struct
   \return NULL on error
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
struct P_isle *dig_alloc_isle(void)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
struct P_isle *dig_alloc_isle(void)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
struct P_isle *dig_alloc_isle(void)
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_isle *dig_alloc_isle()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
struct P_isle *dig_alloc_isle(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
struct P_isle *dig_alloc_isle()
=======
struct P_isle *dig_alloc_isle(void)
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
struct P_isle *dig_alloc_isle(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_isle *dig_alloc_isle()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_isle *dig_alloc_isle(void)
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
struct P_isle *dig_alloc_isle(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_isle *dig_alloc_isle()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_isle *dig_alloc_isle(void)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
struct P_isle *dig_alloc_isle(void)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
struct P_isle *dig_alloc_isle()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
struct P_isle *dig_alloc_isle(void)
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
    struct P_isle *Isle;

    Isle = (struct P_isle *)G_malloc(sizeof(struct P_isle));
    if (Isle == NULL)
        return NULL;

    G_zero(Isle, sizeof(struct P_isle));

    return Isle;
}

/*!
   \brief Free isle structure

   \param Isle pointer to P_isle struct to be freed
 */
void dig_free_isle(struct P_isle *Isle)
{
    if (Isle->alloc_lines > 0)
        G_free(Isle->lines);

    G_free(Isle);
}

/*!
   \brief allocate room for 'num' X and Y  arrays in struct line_pnts

   \param points pointer to line_pnts struct
   \param num number of points

   \return 0 on success
   \return returns -1 on out of memory
 */
int dig_alloc_points(struct line_pnts *points, int num)
{
    int alloced;
    char *p;

    alloced = points->alloc_points;
    /* alloc_space will just return if no space is needed */
    if (!(p = dig__alloc_space(num, &alloced, 50, (char *)points->x,
                               sizeof(double)))) {
        return (dig_out_of_memory());
    }
    points->x = (double *)p;

    alloced = points->alloc_points;
    /* alloc_space will just return if no space is needed */
    if (!(p = dig__alloc_space(num, &alloced, 50, (char *)points->y,
                               sizeof(double)))) {
        return (dig_out_of_memory());
    }
    points->y = (double *)p;

    alloced = points->alloc_points;
    /* alloc_space will just return if no space is needed */
    if (!(p = dig__alloc_space(num, &alloced, 50, (char *)points->z,
                               sizeof(double)))) {
        return (dig_out_of_memory());
    }
    points->z = (double *)p;

    points->alloc_points = alloced;

    return 0;
}

/*!
   \brief Allocate room for 'num' fields and category arrays
   in struct line_cats

   \param cats pointer to line_cats struct
   \param num number of cats

   \return 0 on success
   \return returns -1 on out of memory
 */
int dig_alloc_cats(struct line_cats *cats, int num)
{
    int alloced;
    char *p;

    /* alloc_space will just return if no space is needed */
    alloced = cats->alloc_cats;
    if (!(p = dig__alloc_space(num, &alloced, 1, (int *)cats->field,
                               sizeof(int)))) {
        return dig_out_of_memory();
    }
    cats->field = (int *)p;

    alloced = cats->alloc_cats;
    if (!(p = dig__alloc_space(num, &alloced, 1, (int *)cats->cat,
                               sizeof(int)))) {
        return dig_out_of_memory();
    }
    cats->cat = (int *)p;

    cats->alloc_cats = alloced;

    return 0;
}

/*!
   \brief allocate space in  P_area for add new lines

   \param area pointer to P_area struct
   \param add number of lines to be added

   \return 0 on success
   \return -1 on error
 */
int dig_area_alloc_line(struct P_area *area, int add)
{
    int num;
    char *p;

    num = area->alloc_lines + add;

    p = G_realloc(area->lines, num * sizeof(plus_t));
    if (p == NULL)
        return -1;
    area->lines = (plus_t *)p;

    area->alloc_lines = num;

    return (0);
}

/*!
   \brief Allocate space in  P_area for add new isles

   \param area pointer to P_area struct
   \param add number of isle to be added

   \return 0 on success
   \return -1 on error
 */
int dig_area_alloc_isle(struct P_area *area, int add)
{
    int num;
    char *p;

    G_debug(5, "dig_area_alloc_isle(): add = %d", add);
    num = area->alloc_isles + add;

    p = G_realloc(area->isles, num * sizeof(plus_t));
    if (p == NULL)
        return -1;
    area->isles = (plus_t *)p;

    area->alloc_isles = num;
    return (0);
}

/*!
   \brief Allocate space in  P_isle for add new lines

   \param isle pointer to P_area struct
   \param add number of isle to be added

   \return 0 on success
   \return -1 on error
 */
int dig_isle_alloc_line(struct P_isle *isle, int add)
{
    int num;
    char *p;

    G_debug(5, "dig_isle_alloc_line():");
    num = isle->alloc_lines + add;

    p = G_realloc(isle->lines, num * sizeof(plus_t));
    if (p == NULL)
        return -1;
    isle->lines = (plus_t *)p;

    isle->alloc_lines = num;

    return (0);
}

/*!
   \brief For now just print message and return error code
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
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
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
int dig_out_of_memory(void)
=======
=======
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
int dig_out_of_memory(void)
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int dig_out_of_memory(void)
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
int dig_out_of_memory(void)
=======
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
int dig_out_of_memory()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
{
    G_warning(_("Out of memory"));
    return -1;
}
