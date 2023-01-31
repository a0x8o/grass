#if defined(_OPENMP)
#include <omp.h>
#endif

#include <unistd.h>
#include <grass/rowio.h>
#include <grass/raster.h>
#include "glob.h"
#include "filter.h"

int execute_filter(ROWIO *r, int *out, FILTER *filter, DCELL **cell)
{
    int i;
    int t;
    int count;
    int size;
    int row, rcount;
    int col, ccount;
    int startx, starty;
    int dx, dy;
    int mid;
    int old_nprocs = 0;
    DCELL ***bufs, ***box, *cp;

    if (nprocs > 1 && filter->type == SEQUENTIAL) {
        /* disable parallel temporarily */
        old_nprocs = nprocs;
        nprocs = 1;
    }

    size = filter->size;
    mid = size / 2;
    bufs = (DCELL ***)G_malloc(nprocs * sizeof(DCELL **));
    box = (DCELL ***)G_malloc(nprocs * sizeof(DCELL **));

    for (t = 0; t < nprocs; t++) {
        bufs[t] = (DCELL **)G_malloc(size * sizeof(DCELL *));
        box[t] = (DCELL **)G_malloc(size * sizeof(DCELL *));
    }

    switch (filter->start) {
    case UR:
        startx = ncols - size;
        starty = 0;
        dx = -1;
        dy = 1;
        break;
    case LL:
        startx = 0;
        starty = nrows - size;
        dx = 1;
        dy = -1;
        break;
    case LR:
        startx = ncols - size;
        starty = nrows - size;
        dx = -1;
        dy = -1;
        break;
    case UL:
    default:
        startx = 0;
        starty = 0;
        dx = 1;
        dy = 1;
        break;
    }
    direction = dy;

    G_debug(3, "direction %d, dx=%d, dy=%d", direction, dx, dy);

    rcount = nrows - (size - 1);
    ccount = ncols - (size - 1);

    /* rewind output */
    lseek(out[MASTER], 0L, SEEK_SET);

    /* copy border rows to output */
    row = starty;
    for (i = 0; i < mid; i++) {
        cp = (DCELL *)Rowio_get(&r[MASTER], row);
        if (write(out[MASTER], cp, buflen) < 0)
            G_fatal_error("Error writing temporary file");
        row += dy;
    }

    /* for each row */
    int id = MASTER;
    int start = 0;
    int end = rcount;
    int work = 0;
    DCELL *cellp = cell[MASTER];

#pragma omp parallel firstprivate(starty, id, start, end, cellp) private( \
<<<<<<< HEAD
<<<<<<< HEAD
        i, count, row, col, cp) if (nprocs > 1)
=======
    i, count, row, col, cp) if (nprocs > 1)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    i, count, row, col, cp) if (nprocs > 1)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    {
#if defined(_OPENMP)
        if (nprocs > 1) {
            id = omp_get_thread_num();
            start = rcount * id / nprocs;
            end = rcount * (id + 1) / nprocs;
            cellp = cell[id];
            starty += start * dy;
            lseek(out[id], (off_t)buflen * (mid + start), SEEK_SET);
        }
#endif

        for (count = start; count < end; count++) {
            G_percent(work, rcount, 2);
            row = starty;
            starty += dy;
            /* get "size" rows */
            for (i = 0; i < size; i++) {
                bufs[id][i] = (DCELL *)Rowio_get(&r[id], row);
                box[id][i] = bufs[id][i] + startx;
                row += dy;
            }
            if (filter->type == SEQUENTIAL)
                cellp = bufs[id][mid];
            /* copy border */
            cp = cellp;
            for (i = 0; i < mid; i++)
                *cp++ = bufs[id][mid][i];

            /* filter row */
            col = ccount;
            while (col--) {
                if (null_only && !Rast_is_d_null_value(&box[id][mid][mid])) {
                    *cp++ = box[id][mid][mid];
                }
                else {
                    *cp++ = apply_filter(filter, box[id]);
                }
                for (i = 0; i < size; i++)
                    box[id][i] += dx;
            }

            /* copy border */
            for (i = ncols - mid; i < ncols; i++)
                *cp++ = bufs[id][mid][i];

            /* write row */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
>>>>>>> osgeo-main
            write(out[id], cellp, buflen);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            write(out[id], cellp, buflen);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
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
            write(out[id], cellp, buflen);
=======
            write(out[id], cellp, buflen);
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
            write(out[id], cellp, buflen);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            write(out[id], cellp, buflen);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
            write(out[id], cellp, buflen);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            write(out[id], cellp, buflen);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
            write(out[id], cellp, buflen);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            write(out[id], cellp, buflen);
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
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
=======
            write(out[id], cellp, buflen);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            write(out[id], cellp, buflen);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
            write(out[id], cellp, buflen);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
            write(out[id], cellp, buflen);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            if (write(out[id], cellp, buflen) < 0)
                G_fatal_error("Error writing temporary file");
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
#pragma omp atomic update
            work++;
        }
    }
    G_percent(work, rcount, 2);
    starty = rcount * dy;
    lseek(out[MASTER], (off_t)buflen * (mid + rcount), SEEK_SET);

    /* copy border rows to output */
    row = starty + mid * dy;
    for (i = 0; i < mid; i++) {
        cp = (DCELL *)Rowio_get(&r[MASTER], row);
        if (write(out[MASTER], cp, buflen) < 0)
            G_fatal_error("Error writing temporary file");
        row += dy;
    }

    if (old_nprocs != 0) {
        /* restore parallel execution */
        nprocs = old_nprocs;
        old_nprocs = 0;
    }

    return 0;
}
