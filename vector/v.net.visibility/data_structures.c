/****************************************************************
 * MODULE:     v.path.obstacles
 *
 * AUTHOR(S):  Maximilian Maldacker
 *
 *
 * COPYRIGHT:  (C) 2002-2005 by the GRASS Development Team
 *
 *             This program is free software under the
 *             GNU General Public License (>=v2).
 *             Read the file COPYING that comes with GRASS
 *             for details.
 *
 ****************************************************************/
#include "data_structures.h"

/* stack variables */
static int stack_index = 0;
static struct Point **stack = NULL;

struct Point *pop(void)
{
    stack_index--;

    return stack[stack_index + 1];
}

struct Point *top(void)
{
    if (stack_index > -1)
        return stack[stack_index];
    else
        return NULL;
}

void push(struct Point *p)
{
    stack_index++;
    stack[stack_index] = p;
}

int empty_stack(void)
{
    return stack_index == -1;
}

void init_stack(int size)
{
    stack_index = -1;
    stack = G_malloc(size * sizeof(struct Point));
}

/** compare the points along the x axis
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
int cmp_points(const void *v1, const void *v2, void *param UNUSED)
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
int cmp_points(const void *v1, const void *v2, void *param UNUSED)
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int cmp_points(const void *v1, const void *v2, void *param UNUSED)
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
int cmp_points(const void *v1, const void *v2, void *param UNUSED)
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
int cmp_points(const void *v1, const void *v2, void *param)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
{
    struct Point *p1 = (struct Point *)v1;
    struct Point *p2 = (struct Point *)v2;

    if (p1->x < p2->x)
        return 1;
    else if (p1->x > p2->x)
        return -1;
    else if (p1->y < p2->y)
        return 1;
    else if (p1->y > p2->y)
        return -1;
    else
        return 0;
}

void quickSort(struct Point a[], int l, int r)
{
    int j;

    if (l < r) {
        /* divide and conquer */
        j = partition(a, l, r);
        quickSort(a, l, j - 1);
        quickSort(a, j + 1, r);
    }
}

int partition(struct Point a[], int l, int r)
{
    int i, j;

    struct Point t, pivot;

    pivot = a[l];
    i = l;
    j = r + 1;

    while (1) {
        do
            ++i;
        while (cmp_points(&a[i], &pivot, NULL) < 1 && i <= r);
        do
            --j;
        while (cmp_points(&a[j], &pivot, NULL) == 1);

        if (i >= j)
            break;

        if (a[i].line1 != NULL) {
            if (a[i].line1->p1 == &a[i])
                a[i].line1->p1 = &a[j];
            else
                a[i].line1->p2 = &a[j];
        }

        if (a[j].line1 != NULL) {
            if (a[j].line1->p1 == &a[j])
                a[j].line1->p1 = &a[i];
            else
                a[j].line1->p2 = &a[i];
        }

        if (a[i].line2 != NULL) {
            if (a[i].line2->p1 == &a[i])
                a[i].line2->p1 = &a[j];
            else
                a[i].line2->p2 = &a[j];
        }

        if (a[j].line2 != NULL) {
            if (a[j].line2->p1 == &a[j])
                a[j].line2->p1 = &a[i];
            else
                a[j].line2->p2 = &a[i];
        }

        t = a[i];
        a[i] = a[j];
        a[j] = t;
    }

    if (a[l].line1 != NULL) {
        if (a[l].line1->p1 == &a[l])
            a[l].line1->p1 = &a[j];
        else
            a[l].line1->p2 = &a[j];
    }

    if (a[j].line1 != NULL) {
        if (a[j].line1->p1 == &a[j])
            a[j].line1->p1 = &a[l];
        else
            a[j].line1->p2 = &a[l];
    }

    if (a[l].line2 != NULL) {
        if (a[l].line2->p1 == &a[l])
            a[l].line2->p1 = &a[j];
        else
            a[l].line2->p2 = &a[j];
    }

    if (a[j].line2 != NULL) {
        if (a[j].line2->p1 == &a[j])
            a[j].line2->p1 = &a[l];
        else
            a[j].line2->p2 = &a[l];
    }

    t = a[l];
    a[l] = a[j];
    a[j] = t;

    return j;
}
