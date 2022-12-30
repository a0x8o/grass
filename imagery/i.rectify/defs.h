/* cache for raster data, code taken from r.proj */

/* These next defines determine the size of the sub-window that will
 * be held in memory.  Larger values will require
 * more memory (but less i/o) If you increase these values, keep  in
 * mind that although you think the i/o will decrease, system paging
 * (which goes on behind the scenes) may actual increase the i/o.
 */

#define L2BDIM  6
#define BDIM    (1 << (L2BDIM))
#define L2BSIZE (2 * (L2BDIM))
#define BSIZE   (1 << (L2BSIZE))
#define HI(i)   ((i) >> (L2BDIM))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
#define LO(i)   ((i) & ((BDIM) - 1))
=======
#define LO(i)   ((i) & ((BDIM)-1))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
#define LO(i)   ((i) & ((BDIM)-1))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)

typedef DCELL block[BDIM][BDIM]; /* FCELL sufficient ? */

struct cache {
    int fd;
    int stride;
    int nblocks;
    block **grid;
    block *blocks;
    int *refs;
};

typedef void (*func)(struct cache *, void *, int, double *, double *,
                     struct Cell_head *);

#define BKIDX(c, y, x) ((y) * (c)->stride + (x))
#define BKPTR(c, y, x) ((c)->grid[BKIDX((c), (y), (x))])
#define BLOCK(c, y, x)                           \
    (BKPTR((c), (y), (x)) ? BKPTR((c), (y), (x)) \
                          : get_block((c), BKIDX((c), (y), (x))))
#define CPTR(c, y, x) (&(*BLOCK((c), HI((y)), HI((x))))[LO((y))][LO((x))])

struct menu {
    func method; /* routine to interpolate new value      */
    char *name;  /* method name                           */
    char *text;  /* menu display - full description       */
};
