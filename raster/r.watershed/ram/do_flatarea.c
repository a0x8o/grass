/**********************************************************************
 *
 * flat area beautification after Garbrecht and Martz (1997)
 *
 * Garbrecht, J. & Martz, L. W. (1997)
 * The assignment of drainage direction over flat surfaces in raster
 * digital elevation models. J. Hydrol 193, 204-213.
 *
 * the method is modified for speed, only one pass is necessary to get
 * the gradient away from higher terrain
 *
 *********************************************************************/

#include <limits.h>
#include <assert.h>
#include <stdint.h>
#include <grass/gis.h>
#include <grass/glocale.h>
#include <grass/rbtree.h>
#include "Gwater.h"
#include "do_astar.h"

struct pq_node {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    size_t idx;
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
    size_t idx;
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    size_t idx;
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    size_t idx;
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
    int idx;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    struct pq_node *next;
};

struct pq {
    struct pq_node *first, *last;
    size_t size;
};

struct pq *pq_create(void)
{
    struct pq *q = G_malloc(sizeof(struct pq));

    q->first = G_malloc(sizeof(struct pq_node));
    q->first->next = NULL;
    q->first->idx = SIZE_MAX;
    q->last = q->first;
    q->size = 0;

    return q;
}

/* dummy end must always be allocated and empty */
int pq_add(size_t idx, struct pq *q)
{
    assert(q->last);
    assert(q->last->idx == SIZE_MAX);

    q->last->idx = idx;
    if (q->last->next != NULL) {
        G_fatal_error(_("Beautify flat areas: priority queue error"));
    }

    struct pq_node *n = (struct pq_node *)G_malloc(sizeof(struct pq_node));

    n->next = NULL;
    n->idx = SIZE_MAX;
    q->last->next = n;
    q->last = q->last->next;

    assert(q->last != q->last->next);
    assert(q->first != q->last);
    q->size++;

    return 0;
}

int pq_drop(struct pq *q)
{
    int idx = q->first->idx;
    struct pq_node *n = q->first;

    q->size--;

    q->first = q->first->next;
    assert(q->first);
    assert(q->first != q->first->next);
    assert(n != q->first);
    G_free(n);

    return idx;
}

int pq_destroy(struct pq *q)
{
    struct pq_node *delme;

    while (q->first) {
        delme = q->first;
        q->first = q->first->next;
        G_free(delme);
    }

    G_free(q);

    return 0;
}

struct orders {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    size_t index;
    int uphill, downhill;
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
    size_t index;
    int uphill, downhill;
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    size_t index;
    int uphill, downhill;
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    size_t index;
    int uphill, downhill;
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
    int index, uphill, downhill;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    char flag;
};

int cmp_orders(const void *a, const void *b)
{
    struct orders *oa = (struct orders *)a;
    struct orders *ob = (struct orders *)b;

    return (oa->index < ob->index ? -1 : (oa->index > ob->index));
}

/*
 * return 0 if nothing was modidied
 * return 1 if elevation was modified
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
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
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
int do_flatarea(size_t index, CELL ele, CELL *alt_org, CELL *alt_new)
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
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
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
int do_flatarea(int index, CELL ele, CELL *alt_org, CELL *alt_new)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
{
    int upr, upc, r, c, ct_dir;
    CELL is_in_list, is_worked, this_in_list;
    size_t index_doer, index_up;
    int n_flat_cells = 0, counter;
    CELL ele_nbr, min_ele_diff;
    int uphill_order, downhill_order, max_uphill_order, max_downhill_order;
    int last_order;

    struct pq *up_pq = pq_create();
    struct pq *down_pq = pq_create();

    struct orders inc_order, *order_found, *nbr_order_found;
    struct RB_TREE *order_tree =
        rbtree_create(cmp_orders, sizeof(struct orders));

    pq_add(index, down_pq);
    pq_add(index, up_pq);
    inc_order.downhill = -1;
    inc_order.uphill = 0;
    inc_order.index = index;
    inc_order.flag = 0;
    rbtree_insert(order_tree, &inc_order);

    n_flat_cells = 1;

    min_ele_diff = INT_MAX;
    max_uphill_order = max_downhill_order = 0;

    /* get uphill start points */
    G_debug(2, "get uphill start points");
    counter = 0;
    while (down_pq->size) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if ((index_doer = pq_drop(down_pq)) == -1)
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
        if ((index_doer = pq_drop(down_pq)) == SIZE_MAX)
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
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
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
            G_fatal_error("get start points: no more points in down queue");

        seg_index_rc(alt_seg, index_doer, &r, &c);

        FLAG_SET(flat_done, r, c);

        /* check all neighbours, breadth first search */
        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (upr, upc) for this neighbour */
            upr = r + nextdr[ct_dir];
            upc = c + nextdc[ct_dir];
            /* check if r, c are within region */
            if (upr >= 0 && upr < nrows && upc >= 0 && upc < ncols) {
                index_up = SEG_INDEX(alt_seg, upr, upc);
                is_in_list = FLAG_GET(in_list, upr, upc);
                is_worked = FLAG_GET(worked, upr, upc);
                ele_nbr = alt_org[index_up];

                if (ele_nbr == ele && !is_worked) {

                    inc_order.downhill = -1;
                    inc_order.uphill = -1;
                    inc_order.index = index_up;
                    inc_order.flag = 0;
                    /* not yet added to queue */
                    if ((order_found = rbtree_find(order_tree, &inc_order)) ==
                        NULL) {
                        n_flat_cells++;

                        /* add to down queue if not yet in there */
                        pq_add(index_up, down_pq);

                        /* add to up queue if not yet in there */
                        if (is_in_list) {
                            pq_add(index_up, up_pq);
                            /* set uphill order to 0 */
                            inc_order.uphill = 0;
                            counter++;
                        }
                        rbtree_insert(order_tree, &inc_order);
                    }
                }
            }
        }
    }
    /* flat area too small, not worth the effort */
    if (n_flat_cells < 5) {
        /* clean up */
        pq_destroy(up_pq);
        pq_destroy(down_pq);
        rbtree_destroy(order_tree);

        return 0;
    }

    G_debug(2, "%d flat cells, %d cells in tree, %d start cells", n_flat_cells,
            (int)order_tree->count, counter);

    pq_destroy(down_pq);
    down_pq = pq_create();

    /* got uphill start points, do uphill correction */
    G_debug(2, "got uphill start points, do uphill correction");
    counter = 0;
    uphill_order = 1;
    while (up_pq->size) {
        int is_in_down_queue = 0;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if ((index_doer = pq_drop(up_pq)) == -1)
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
        if ((index_doer = pq_drop(up_pq)) == SIZE_MAX)
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
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
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
            G_fatal_error("uphill order: no more points in up queue");

        seg_index_rc(alt_seg, index_doer, &r, &c);
        this_in_list = FLAG_GET(in_list, r, c);

        /* get uphill order for this point */
        inc_order.index = index_doer;
        if ((order_found = rbtree_find(order_tree, &inc_order)) == NULL)
            G_fatal_error(_("flat cell escaped for uphill correction"));

        last_order = uphill_order - 1;
        uphill_order = order_found->uphill;

        if (last_order > uphill_order)
            G_warning(_("queue error: last uphill order %d > current uphill "
                        "order %d"),
                      last_order, uphill_order);

        /* debug */
        if (uphill_order == -1)
            G_fatal_error(_("uphill order not set"));

        if (max_uphill_order < uphill_order)
            max_uphill_order = uphill_order;

        uphill_order++;
        counter++;

        /* check all neighbours, breadth first search */
        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (upr, upc) for this neighbour */
            upr = r + nextdr[ct_dir];
            upc = c + nextdc[ct_dir];
            /* check if r, c are within region */
            if (upr >= 0 && upr < nrows && upc >= 0 && upc < ncols) {
                index_up = SEG_INDEX(alt_seg, upr, upc);
                is_in_list = FLAG_GET(in_list, upr, upc);
                is_worked = FLAG_GET(worked, upr, upc);
                ele_nbr = alt_org[index_up];

                /* all cells that are in_list should have been added
                 * previously as uphill start points */
                if (ele_nbr == ele && !is_worked) {

                    inc_order.index = index_up;
                    if ((nbr_order_found =
                             rbtree_find(order_tree, &inc_order)) == NULL) {
                        G_fatal_error(
                            _("flat cell escaped in uphill correction"));
                    }

                    /* not yet added to queue */
                    if (nbr_order_found->uphill == -1) {
                        if (is_in_list)
                            G_warning("cell should be in queue");
                        /* add to up queue */
                        pq_add(index_up, up_pq);
                        /* set nbr uphill order = current uphill order + 1 */
                        nbr_order_found->uphill = uphill_order;
                    }
                }
                /* add focus cell to down queue */
                if (!this_in_list && !is_in_down_queue && ele_nbr != ele &&
                    !is_in_list && !is_worked) {
                    pq_add(index_doer, down_pq);
                    /* set downhill order to 0 */
                    order_found->downhill = 0;
                    is_in_down_queue = 1;
                }
                if (ele_nbr > ele && min_ele_diff > ele_nbr - ele)
                    min_ele_diff = ele_nbr - ele;
            }
        }
    }
    /* debug: all flags should be set to 0 */

    pq_destroy(up_pq);
    up_pq = pq_create();

    /* got downhill start points, do downhill correction */
    G_debug(2, "got downhill start points, do downhill correction");
    downhill_order = 1;
    while (down_pq->size) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if ((index_doer = pq_drop(down_pq)) == -1)
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
        if ((index_doer = pq_drop(down_pq)) == SIZE_MAX)
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
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
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(down_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
            G_fatal_error(_("downhill order: no more points in down queue"));

        seg_index_rc(alt_seg, index_doer, &r, &c);
        this_in_list = FLAG_GET(in_list, r, c);

        /* get downhill order for this point */
        inc_order.index = index_doer;
        if ((order_found = rbtree_find(order_tree, &inc_order)) == NULL)
            G_fatal_error(_("flat cell escaped for downhill correction"));

        last_order = downhill_order - 1;
        downhill_order = order_found->downhill;

        if (last_order > downhill_order)
            G_warning(_("queue error: last downhill order %d > current "
                        "downhill order %d"),
                      last_order, downhill_order);

        /* debug */
        if (downhill_order == -1)
            G_fatal_error(_("downhill order: downhill order not set"));

        if (max_downhill_order < downhill_order)
            max_downhill_order = downhill_order;

        downhill_order++;

        /* check all neighbours, breadth first search */
        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (upr, upc) for this neighbour */
            upr = r + nextdr[ct_dir];
            upc = c + nextdc[ct_dir];
            /* check if r, c are within region */
            if (upr >= 0 && upr < nrows && upc >= 0 && upc < ncols) {
                index_up = SEG_INDEX(alt_seg, upr, upc);
                is_in_list = FLAG_GET(in_list, upr, upc);
                is_worked = FLAG_GET(worked, upr, upc);
                ele_nbr = alt_org[index_up];

                if (ele_nbr == ele && !is_worked) {

                    inc_order.index = index_up;
                    if ((nbr_order_found =
                             rbtree_find(order_tree, &inc_order)) == NULL)
                        G_fatal_error(
                            _("flat cell escaped in downhill correction"));

                    /* not yet added to queue */
                    if (nbr_order_found->downhill == -1) {

                        /* add to down queue */
                        pq_add(index_up, down_pq);
                        /* set nbr downhill order = current downhill order + 1
                         */
                        nbr_order_found->downhill = downhill_order;

                        /* add to up queue */
                        if (is_in_list) {
                            pq_add(index_up, up_pq);
                            /* set flag */
                            nbr_order_found->flag = 1;
                        }
                    }
                }
            }
        }
    }

    /* got uphill and downhill order, adjust ele */

    /* increment: ele += uphill_order +  max_downhill_order - downhill_order */
    /* decrement: ele += uphill_order - max_uphill_order - downhill_order */

    G_debug(2, "adjust ele");
    while (up_pq->size) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        if ((index_doer = pq_drop(up_pq)) == -1)
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
        if ((index_doer = pq_drop(up_pq)) == SIZE_MAX)
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
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
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
        if ((index_doer = pq_drop(up_pq)) == -1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
            G_fatal_error("no more points in up queue");

        seg_index_rc(alt_seg, index_doer, &r, &c);
        this_in_list = FLAG_GET(in_list, r, c);

        /* get uphill and downhill order for this point */
        inc_order.index = index_doer;
        if ((order_found = rbtree_find(order_tree, &inc_order)) == NULL)
            G_fatal_error(_("flat cell escaped for adjustment"));

        uphill_order = order_found->uphill;
        downhill_order = order_found->downhill;

        /* debug */
        if (uphill_order == -1)
            G_fatal_error(_("adjustment: uphill order not set"));
        if (!this_in_list && downhill_order == -1)
            G_fatal_error(_("adjustment: downhill order not set"));

        /* increment */
        if (this_in_list) {
            downhill_order = max_downhill_order;
            uphill_order = 0;
        }
        alt_new[index_doer] +=
            (uphill_order +
             (double)(max_downhill_order - downhill_order) / 2.0 + 0.5) /
                2.0 +
            0.5;

        /* check all neighbours, breadth first search */
        for (ct_dir = 0; ct_dir < sides; ct_dir++) {
            /* get r, c (upr, upc) for this neighbour */
            upr = r + nextdr[ct_dir];
            upc = c + nextdc[ct_dir];
            /* check if r, c are within region */
            if (upr >= 0 && upr < nrows && upc >= 0 && upc < ncols) {
                index_up = SEG_INDEX(alt_seg, upr, upc);
                is_in_list = FLAG_GET(in_list, upr, upc);
                is_worked = FLAG_GET(worked, upr, upc);
                ele_nbr = alt_org[index_up];

                if (ele_nbr == ele && !is_worked) {

                    inc_order.index = index_up;
                    if ((nbr_order_found =
                             rbtree_find(order_tree, &inc_order)) == NULL)
                        G_fatal_error(_("flat cell escaped in adjustment"));

                    /* not yet added to queue */
                    if (nbr_order_found->flag == 0) {
                        if (is_in_list)
                            G_warning(
                                "adjustment: in_list cell should be in queue");
                        /* add to up queue */
                        pq_add(index_up, up_pq);
                        nbr_order_found->flag = 1;
                    }
                }
            }
        }
    }

    /* clean up */
    pq_destroy(up_pq);
    pq_destroy(down_pq);
    rbtree_destroy(order_tree);

    return 1;
}
