#include <time.h>
#include <grass/imagery.h>
#include <grass/cluster.h>

extern struct Cluster C;
extern struct Signature in_sig;

extern int maxclass;
extern double conv;
extern double sep;
extern int iters;
extern int mcs;
extern char *group;
extern char *subgroup;
extern struct Ref ref;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
extern char **semantic_labels;
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
extern char **semantic_labels;
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
>>>>>>> osgeo-main
extern char **bandrefs;
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
extern char **semantic_labels;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
extern char **semantic_labels;
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
extern char **semantic_labels;
=======
extern char **bandrefs;
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
extern char **semantic_labels;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
extern char **semantic_labels;
=======
extern char **bandrefs;
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
=======
extern char **semantic_labels;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
extern char **semantic_labels;
=======
extern char **bandrefs;
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
=======
extern char **semantic_labels;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
extern char outsigfile[GNAME_MAX + GMAPSET_MAX];
extern char *insigfile;
extern char *reportfile;
extern DCELL **cell;
extern int *cellfd;
extern FILE *report;
extern int sample_rows, sample_cols;
extern int verbose;
extern time_t start_time;
