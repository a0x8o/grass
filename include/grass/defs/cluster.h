#ifndef GRASS_CLUSTERDEFS_H
#define GRASS_CLUSTERDEFS_H

/* c_assign.c */
int I_cluster_assign(struct Cluster *, int *);

/* c_begin.c */
int I_cluster_begin(struct Cluster *, int);

/* c_clear.c */
int I_cluster_clear(struct Cluster *);

/* c_distinct.c */
int I_cluster_distinct(struct Cluster *, double);

/* c_exec.c */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
>>>>>>> osgeo-main
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
>>>>>>> osgeo-main
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
>>>>>>> osgeo-main
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
>>>>>>> osgeo-main
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
>>>>>>> osgeo-main
int I_cluster_exec(struct Cluster *, int, int, double, double, int, int (*)(),
                   int *);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int, int (*)(),
                   int *);
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int, int (*)(),
                   int *);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int, int (*)(),
                   int *);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
int I_cluster_exec(struct Cluster *, int, int, double, double, int,
                   int (*)(struct Cluster *, int), int *);
=======
int I_cluster_exec(struct Cluster *, int, int, double, double, int, int (*)(),
                   int *);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
/* c_execmem.c */
int I_cluster_exec_allocate(struct Cluster *);
int I_cluster_exec_free(struct Cluster *);

/* c_means.c */
int I_cluster_means(struct Cluster *);

/* c_merge.c */
int I_cluster_merge(struct Cluster *);

/* c_nclasses.c */
int I_cluster_nclasses(struct Cluster *, int);

/* c_point.c */
int I_cluster_point(struct Cluster *, DCELL *);
int I_cluster_begin_point_set(struct Cluster *, int);
int I_cluster_point_part(struct Cluster *, DCELL, int, int);
int I_cluster_end_point_set(struct Cluster *, int);

/* c_reassign.c */
int I_cluster_reassign(struct Cluster *, int *);

/* c_reclass.c */
int I_cluster_reclass(struct Cluster *, int);

/* c_sep.c */
double I_cluster_separation(struct Cluster *, int, int);

/* c_sig.c */
int I_cluster_signatures(struct Cluster *);

/* c_sum2.c */
int I_cluster_sum2(struct Cluster *);

#endif
