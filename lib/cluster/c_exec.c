/*!
   \file cluster/c_exec.c

   \brief Cluster library - Exectute clusterring

   (C) 2001-2009 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Original author CERL
 */

#include <grass/cluster.h>
#include <grass/glocale.h>

/*!
   \param C pointer to Cluster structure
   \param maxclass maximum number of classes
   \param iterations maximum number of iterations
   \param convergence percentage of points stable
   \param separation minimum distance between class centroids
   \param min_class_size minimum size of class
   \param checkpoint routine to be called at various steps
   \param interrupted boolean to check for interrupt

   \return 0 ok
   \return -1 out of memory
   \return -2 interrupted
   \return 1 not enough data points
 */
int I_cluster_exec(struct Cluster *C, int maxclass, int iterations,
                   double convergence, double separation, int min_class_size,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
>>>>>>> osgeo-main
                   int (*checkpoint)(), int *interrupted)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                   int (*checkpoint)(), int *interrupted)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
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
                   int (*checkpoint)(), int *interrupted)
=======
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
                   int (*checkpoint)(), int *interrupted)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                   int (*checkpoint)(), int *interrupted)
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
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
                   int (*checkpoint)(), int *interrupted)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                   int (*checkpoint)(), int *interrupted)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
                   int (*checkpoint)(struct Cluster *, int), int *interrupted)
=======
                   int (*checkpoint)(), int *interrupted)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                   int (*checkpoint)(), int *interrupted)
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
{
    int changes;

    /* set interrupted to false */
    *interrupted = 0;

    /* check for valid inputs */
    if (C->npoints < 2) {
        G_warning(_("Not enough data points (%d) in cluster"), C->npoints);
        return 1;
    }

    /* check other parms */
    if (maxclass < 0)
        maxclass = 1;
    C->nclasses = maxclass;

    if (min_class_size <= 0)
        min_class_size = 17;
    if (min_class_size < 2)
        min_class_size = 2;

    if (iterations <= 0)
        iterations = 20;
    if (convergence <= 0.0)
        convergence = 98.0;
    if (separation < 0.0)
        separation = 0.5;

    /* allocate memory */
    if (!I_cluster_exec_allocate(C))
        return -1;

    /* generate class means */
    I_cluster_means(C);
    if (checkpoint)
        (*checkpoint)(C, 1);

    /* now assign points to nearest class */
    I_cluster_assign(C, interrupted);
    if (*interrupted)
        return -2;
    I_cluster_sum2(C);
    if (checkpoint)
        (*checkpoint)(C, 2);

    /* get rid of empty classes now */
    I_cluster_reclass(C, 1);

    for (C->iteration = 1;; C->iteration++) {
        if (*interrupted)
            return -2;

        changes = 0;

        /* re-assign points to nearest class */

        changes = I_cluster_reassign(C, interrupted);
        if (*interrupted)
            return -2;

        /* if too many points have changed class, re-assign points */
        C->percent_stable = (C->npoints - changes) * 100.0;
        C->percent_stable /= (double)C->npoints;

        if (checkpoint)
            (*checkpoint)(C, 3);

        if (C->iteration >= iterations)
            break;

        if (C->percent_stable < convergence)
            continue;

        /* otherwise merge non-distinct classes */

        if (I_cluster_distinct(C, separation))
            break;

        if (checkpoint)
            (*checkpoint)(C, 4);

        I_cluster_merge(C);
    }

    /* get rid of small classes */
    I_cluster_reclass(C, min_class_size);
    I_cluster_sum2(C);

    /* compute the resulting signatures */
    I_cluster_signatures(C);

    return 0;
}
