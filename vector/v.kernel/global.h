#include <grass/gis.h>

#define NODE_NONE                   0
/* According Okabe 2009 */
#define NODE_SIMILAR                1
#define NODE_EQUAL_SPLIT            2
#define NODE_CONTINUOUS_EQUAL_SPLIT 3

#define KERNEL_UNIFORM              0
#define KERNEL_TRIANGULAR           1
#define KERNEL_EPANECHNIKOV         2
#define KERNEL_QUARTIC              3
#define KERNEL_TRIWEIGHT            4
#define KERNEL_GAUSSIAN             5
#define KERNEL_COSINE               6

void setKernelFunction(int function, int dimension, double bandwidth,
                       double *term);
double kernelFunction(double term, double bandwidth, double x);

double euclidean_distance(double *x, double *y, int n);
double gaussian2dBySigma(double d, double sigma);
double gaussianFunction(double x, double sigma, double dimension);
double gaussianKernel(double x, double term);

double invGaussian2d(double sigma, double prob);
double gaussian2dByTerms(double d, double term1, double term2);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
>>>>>>> osgeo-main
double brent_iterate(double (*f)(), double x_lower, double x_upper,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
double brent_iterate(double (*f)(), double x_lower, double x_upper,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
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
double brent_iterate(double (*f)(), double x_lower, double x_upper,
=======
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
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
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
double brent_iterate(double (*f)(), double x_lower, double x_upper,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
double brent_iterate(double (*f)(), double x_lower, double x_upper,
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
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
double brent_iterate(double (*f)(), double x_lower, double x_upper,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
double brent_iterate(double (*f)(), double x_lower, double x_upper,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
double brent_iterate(double (*f)(double), double x_lower, double x_upper,
=======
double brent_iterate(double (*f)(), double x_lower, double x_upper,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
double brent_iterate(double (*f)(), double x_lower, double x_upper,
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
                     int maxiter);
double kernel1(double d, double rs, double lambda);
double segno(double x);

/* main.c */
int read_points(struct Map_info *In, double ***coordinate, double dsize);
double compute_all_distances(double **coordinate, double **dists, int n,
                             double dmax);
double compute_all_net_distances(struct Map_info *In, struct Map_info *Net,
                                 double netmax, double **dists, double dmax);
void compute_distance(double N, double E, double sigma, double term,
                      double *gaussian, double dmax, struct bound_box *box,
                      struct boxlist *NList);
void compute_net_distance(double x, double y, struct Map_info *In,
                          struct Map_info *Net, double netmax, double sigma,
                          double term, double *gaussian, double dmax,
                          int node_method);
