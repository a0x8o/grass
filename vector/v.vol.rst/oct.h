#ifndef __OCT_H__
#define __OCT_H__

#include "dataoct.h"

struct octfunc {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
    int (*compare)(struct quadruple *, struct octdata *);
    struct octdata **(*divide_data)(struct octdata *);
    int (*add_data)(struct quadruple *, struct octdata *);
    int (*intersect)(double, double, double, double, double, double,
                     struct octdata *);
    int (*division_check)(struct octdata *);
    int (*get_points)(struct quadruple *, struct octdata *, double, double,
                      double, double, double, double, int);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
};

struct octtree {
    struct octdata *data;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
    int (*compare)();
    VOID_T **(*divide_data)();
    int (*add_data)();
    int (*intersect)();
    int (*division_check)();
    int (*get_points)();
};

struct octtree {
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
    int (*compare)();
    VOID_T **(*divide_data)();
    int (*add_data)();
    int (*intersect)();
    int (*division_check)();
    int (*get_points)();
};

struct octtree {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    VOID_T *data;
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    int (*compare)(struct quadruple *, struct octdata *);
    struct octdata **(*divide_data)(struct octdata *);
    int (*add_data)(struct quadruple *, struct octdata *);
    int (*intersect)(double, double, double, double, double, double,
                     struct octdata *);
    int (*division_check)(struct octdata *);
    int (*get_points)(struct quadruple *, struct octdata *, double, double,
                      double, double, double, double, int);
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
};

struct octtree {
    struct octdata *data;
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    int (*compare)();
    VOID_T **(*divide_data)();
    int (*add_data)();
    int (*intersect)();
    int (*division_check)();
    int (*get_points)();
};

struct octtree {
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
    VOID_T *data;
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    int (*compare)(struct quadruple *, struct octdata *);
    struct octdata **(*divide_data)(struct octdata *);
    int (*add_data)(struct quadruple *, struct octdata *);
    int (*intersect)(double, double, double, double, double, double,
                     struct octdata *);
    int (*division_check)(struct octdata *);
    int (*get_points)(struct quadruple *, struct octdata *, double, double,
                      double, double, double, double, int);
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
};

struct octtree {
    struct octdata *data;
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    int (*compare)();
    VOID_T **(*divide_data)();
    int (*add_data)();
    int (*intersect)();
    int (*division_check)();
    int (*get_points)();
};

struct octtree {
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
    VOID_T *data;
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    int (*compare)(struct quadruple *, struct octdata *);
    struct octdata **(*divide_data)(struct octdata *);
    int (*add_data)(struct quadruple *, struct octdata *);
    int (*intersect)(double, double, double, double, double, double,
                     struct octdata *);
    int (*division_check)(struct octdata *);
    int (*get_points)(struct quadruple *, struct octdata *, double, double,
                      double, double, double, double, int);
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
};

struct octtree {
    struct octdata *data;
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
=======
    int (*compare)();
    VOID_T **(*divide_data)();
    int (*add_data)();
    int (*intersect)();
    int (*division_check)();
    int (*get_points)();
};

struct octtree {
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    VOID_T *data;
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    int (*compare)(struct quadruple *, struct octdata *);
    struct octdata **(*divide_data)(struct octdata *);
    int (*add_data)(struct quadruple *, struct octdata *);
    int (*intersect)(double, double, double, double, double, double,
                     struct octdata *);
    int (*division_check)(struct octdata *);
    int (*get_points)(struct quadruple *, struct octdata *, double, double,
                      double, double, double, double, int);
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
};

struct octtree {
    struct octdata *data;
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
    struct octtree **leafs;
    struct octtree *parent;
    struct octfunc *functions;
    int octant;
};

struct octfunc *OT_functions_new(
    int (*compare)(struct quadruple *, struct octdata *),
    struct octdata **(*divide_data)(struct octdata *),
    int (*add_data)(struct quadruple *, struct octdata *),
    int (*intersect)(double, double, double, double, double, double,
                     struct octdata *),
    int (*division_check)(struct octdata *),
    int (*get_points)(struct quadruple *, struct octdata *, double, double,
                      double, double, double, double, int));
struct octtree *OT_tree_new(struct octdata *, struct octtree **,
                            struct octtree *, struct octfunc *, int octant);
int OT_insert_oct(struct quadruple *, struct octtree *);
int OT_region_data(struct octtree *, double, double, double, double, double,
                   double, struct quadruple *, int);

#endif
