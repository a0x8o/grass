/************************** MEMORY MANAGEMENT ***************************/

#include <grass/gis.h>
#define KB        1024
#define MB        (KB * KB)
#define SEGSINMEM 9
#define SEGCOLS   ((int)(region.cols / 3) + 1)
#define SEGROWS \
    ((int)(MB / region.cols / 3) <= 1 ? 1 : (int)(MB / region.cols / 3))

extern CELL v;

/*
 * allocate_heap: allocate and initialize matrices, cell buffers, headers
 * globals r: parm, region
 * globals w: fl, density, ew_dist, el, as, ds
 */

void allocate_heap(void);

/*
 * deallocate_heap: frees space for other processes, closes cts output files
 * globals r: parm, bitbar, lgfd, el, as, ew_dist
 */

void deallocate_heap(void);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
void put_row_seg(layer, int /* l, row */);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void put_row_seg(layer, int /* l, row */);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
=======
void put_row_seg(layer, int /* l, row */);
=======
>>>>>>> osgeo-main
void put_row_seg(/* l, row */);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
void put_row_seg(/* l, row */);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
void put_row_seg(layer, int /* l, row */);
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
void put_row_seg(/* l, row */);
=======
void put_row_seg(layer, int /* l, row */);
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
void put_row_seg(layer, int /* l, row */);
=======
void put_row_seg(/* l, row */);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void put_row_seg(/* l, row */);
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
void put_row_seg(layer, int /* l, row */);
=======
void put_row_seg(/* l, row */);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void put_row_seg(/* l, row */);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
void put_row_seg(layer, int /* l, row */);
=======
void put_row_seg(/* l, row */);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void put_row_seg(/* l, row */);
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
void put_row_seg(layer, int /* l, row */);
=======
void put_row_seg(/* l, row */);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void put_row_seg(/* l, row */);
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
void put_row_seg(/* l, row */);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
void put_row_seg(/* l, row */);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void put_row_seg(layer, int /* l, row */);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
void put_row_seg(/* l, row */);
=======
void put_row_seg(layer, int /* l, row */);
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
void put_row_seg(/* l, row */);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))

#define get_row(l, row)                                                 \
    ((parm.seg && (Segment_flush(l.seg) < 1 ||                          \
                   Segment_get_row(l.seg, l.buf[row] - l.col_offset,    \
                                   row + l.row_offset) < 1))            \
         ? (sprintf(string, "r.flow: cannot write segment file for %s", \
                    l.name),                                            \
            G_fatal_error("%s", string), (DCELL *)NULL)                 \
         : l.buf[row])

/*   This was is Astley's version 12...
   > #define get_cell_row(l, row) \
   >     ((parm.seg && (Segment_flush(l.seg) < 1 || \
   >                  Segment_get_row(l.seg, l.buf[row] - l.col_offset, \
   >                                         row + l.row_offset) < 1)) ? \
   >       (sprintf(string, "r.flow: cannot write segment file for %s",
   l.name),\
   >        G_fatal_error(string), (CELL *) NULL) : \
   >       (CELL *)l.buf[row])
   >
 */

#define aspect(row, col)                                                      \
    (parm.seg                                                                 \
         ? (Segment_get(as.seg, &v, row + as.row_offset,                      \
                        col + as.col_offset) < 1                              \
                ? (sprintf(string, "r.flow: cannot read segment file for %s", \
                           as.name),                                          \
                   G_fatal_error("%s", string), 0)                            \
                : v)                                                          \
         : (parm.mem ? aspect_fly(el.buf[row - 1] + col, el.buf[row] + col,   \
                                  el.buf[row + 1] + col, ew_dist[row])        \
                     : as.buf[row][col]))

#define get(l, row, col)                                                       \
    (parm.seg                                                                  \
         ? (Segment_get(l.seg, &v, row + l.row_offset, col + l.col_offset) < 1 \
                ? (sprintf(string, "r.flow: cannot read segment file for %s",  \
                           l.name),                                            \
                   G_fatal_error("%s", string), 0)                             \
                : v)                                                           \
         : l.buf[row][col])

#define put(l, row, col, w)                                                    \
    (parm.seg                                                                  \
         ? (v = w,                                                             \
            Segment_put(l.seg, &v, row + l.row_offset, col + l.col_offset) < 1 \
                ? (sprintf(string, "r.flow: cannot write segment file for %s", \
                           l.name),                                            \
                   G_fatal_error("%s", string), 0)                             \
                : 0)                                                           \
         : (l.buf[row][col] = w))
