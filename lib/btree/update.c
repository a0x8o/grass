#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <grass/btree.h>

static void *store(const void *, int);

int btree_update(BTREE *B, const void *key, int keylen, const void *data,
                 int datalen)
{
    int p = 0;
    int q;
    int N;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    int (*cmp)(const void *, const void *);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    int (*cmp)(const void *, const void *);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    int (*cmp)(const void *, const void *);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    int (*cmp)(const void *, const void *);
=======
>>>>>>> osgeo-main
=======
    int (*cmp)(const void *, const void *);
=======
>>>>>>> osgeo-main
=======
    int (*cmp)(const void *, const void *);
=======
>>>>>>> osgeo-main
=======
    int (*cmp)(const void *, const void *);
=======
>>>>>>> osgeo-main
=======
    int (*cmp)(const void *, const void *);
=======
>>>>>>> osgeo-main
=======
    int (*cmp)(const void *, const void *);
=======
>>>>>>> osgeo-main
=======
    int (*cmp)(const void *, const void *);
=======
>>>>>>> osgeo-main
    int (*cmp)();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    int (*cmp)();
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    int (*cmp)(const void *, const void *);
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
    int (*cmp)();
=======
    int (*cmp)(const void *, const void *);
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
    int (*cmp)(const void *, const void *);
=======
    int (*cmp)();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int (*cmp)();
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    int (*cmp)(const void *, const void *);
=======
    int (*cmp)();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int (*cmp)();
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    int (*cmp)(const void *, const void *);
=======
    int (*cmp)();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    int (*cmp)();
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    int dir;

    /* first node is special case */
    N = B->N;
    if (N == 0) {
        N = B->N = 1;
        B->node[N].key = store(key, keylen);
        B->node[N].data = store(data, datalen);
        B->node[N].left = 0;
        B->node[N].right = 0;
        if (B->node[N].key && B->node[N].data)
            return 1;
        else
            return 0;
    }

    cmp = B->cmp;

    q = 1;
    while (q > 0) {
        p = q;
        dir = (*cmp)(B->node[q].key, key);
        if (dir == 0) {
            free(B->node[q].data);
            return ((B->node[q].data = store(data, datalen))) ? 1 : 0;
        }
        if (dir > 0)
            q = B->node[q].left; /* go left */
        else
            q = B->node[q].right; /* go right */
    }

    /* new node */
    B->N++;
    N = B->N;

    /* grow the tree? */
    if (N >= B->tlen) {
        B->node = (BTREE_NODE *)realloc(B->node, sizeof(BTREE_NODE) *
                                                     (B->tlen += B->incr));
        if (B->node == NULL)
            return 0;
    }

    /* add node to tree */
    B->node[N].key = store(key, keylen);
    B->node[N].data = store(data, datalen);
    B->node[N].left = 0;

    if (dir > 0) {
        B->node[N].right = -p; /* create thread */
        B->node[p].left = N;   /* insert left */
    }
    else {
        B->node[N].right = B->node[p].right; /* copy right link/thread */
        B->node[p].right = N;                /* add right */
    }
    return 1;
}

static void *store(const void *s, int n)
{
    void *b;

    if (n <= 0)
        return NULL;

    b = malloc(n);
    if (b == NULL)
        return b;

    memcpy(b, s, n);

    return b;
}
