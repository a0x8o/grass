#ifndef GRASS_IMAGEDEFS_H
#define GRASS_IMAGEDEFS_H

/* alloc.c */
void *I_malloc(size_t);
void *I_realloc(void *, size_t);
int I_free(void *);
double **I_alloc_double2(int, int);
int *I_alloc_int(int);
int **I_alloc_int2(int, int);
int I_free_int2(int **);
int I_free_double2(double **);
double ***I_alloc_double3(int, int, int);
int I_free_double3(double ***);

/* eol.c */
int I_get_to_eol(char *, int, FILE *);

/* find.c */
int I_find_group(const char *);
int I_find_group2(const char *, const char *);
int I_find_group_file(const char *, const char *);
int I_find_group_file2(const char *, const char *, const char *);
int I_find_subgroup(const char *, const char *);
int I_find_subgroup2(const char *, const char *, const char *);
int I_find_subgroup_file(const char *, const char *, const char *);
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
>>>>>>> osgeo-main
int I_find_subgroup_file2(const char *, const char *, const char *, const char *);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
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
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
int I_find_subgroup_file2(const char *, const char *, const char *, const char *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
int I_find_subgroup_file2(const char *, const char *, const char *, const char *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
int I_find_subgroup_file2(const char *, const char *, const char *, const char *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
int I_find_subgroup_file2(const char *, const char *, const char *, const char *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
int I_find_subgroup_file2(const char *, const char *, const char *, const char *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
int I_find_subgroup_file2(const char *, const char *, const char *, const char *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
int I_find_subgroup_file2(const char *, const char *, const char *,
                          const char *);
=======
int I_find_subgroup_file2(const char *, const char *, const char *, const char *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
const char *I_find_signature(I_SIGFILE_TYPE, char *, const char *);
const char *I_find_signature2(I_SIGFILE_TYPE, const char *, const char *);

/* fopen.c */
FILE *I_fopen_group_file_new(const char *, const char *);
FILE *I_fopen_group_file_append(const char *, const char *);
FILE *I_fopen_group_file_old(const char *, const char *);
FILE *I_fopen_group_file_old2(const char *, const char *, const char *);
FILE *I_fopen_subgroup_file_new(const char *, const char *, const char *);
FILE *I_fopen_subgroup_file_append(const char *, const char *, const char *);
FILE *I_fopen_subgroup_file_old(const char *, const char *, const char *);
FILE *I_fopen_subgroup_file_old2(const char *, const char *, const char *,
                                 const char *);

/* georef.c */
int I_compute_georef_equations(struct Control_Points *, double *, double *,
                               double *, double *, int);
int I_georef(double, double, double *, double *, double *, double *, int);

/* georef_tps.c */
int I_compute_georef_equations_tps(struct Control_Points *, double **,
                                   double **, double **, double **);
int I_georef_tps(double, double, double *, double *, double *, double *,
                 struct Control_Points *, int);

/* group.c */
int I_get_group(char *);
int I_put_group(const char *);
int I_get_subgroup(const char *, char *);
int I_put_subgroup(const char *, const char *);
int I_get_group_ref(const char *, struct Ref *);
int I_get_group_ref2(const char *, const char *, struct Ref *);
int I_get_subgroup_ref(const char *, const char *, struct Ref *);
int I_get_subgroup_ref2(const char *, const char *, const char *, struct Ref *);
int I_init_ref_color_nums(struct Ref *);
int I_put_group_ref(const char *, const struct Ref *);
int I_put_subgroup_ref(const char *, const char *, const struct Ref *);
int I_add_file_to_group_ref(const char *, const char *, struct Ref *);
int I_transfer_group_ref_file(const struct Ref *, int, struct Ref *);
int I_init_group_ref(struct Ref *);
int I_free_group_ref(struct Ref *);

/* iclass.c */
struct Map_info;
int I_iclass_analysis(IClass_statistics *, struct Ref *, struct Map_info *,
                      const char *, const char *, const char *);
int I_iclass_init_group(const char *, const char *, struct Ref *);
void I_iclass_create_raster(IClass_statistics *, struct Ref *, const char *);

/* iclass_statistics.c */
void I_iclass_statistics_get_nbands(IClass_statistics *, int *);
void I_iclass_statistics_get_cat(IClass_statistics *, int *);
void I_iclass_statistics_get_name(IClass_statistics *, const char **);
void I_iclass_statistics_get_color(IClass_statistics *, const char **);
void I_iclass_statistics_get_ncells(IClass_statistics *, int *);
int I_iclass_statistics_get_max(IClass_statistics *, int, int *);
int I_iclass_statistics_get_range_max(IClass_statistics *, int, int *);
int I_iclass_statistics_get_min(IClass_statistics *, int, int *);
int I_iclass_statistics_get_range_min(IClass_statistics *, int, int *);
int I_iclass_statistics_get_sum(IClass_statistics *, int, float *);
int I_iclass_statistics_get_mean(IClass_statistics *, int, float *);
int I_iclass_statistics_get_stddev(IClass_statistics *, int, float *);
void I_iclass_statistics_get_nstd(IClass_statistics *, float *);
void I_iclass_statistics_set_nstd(IClass_statistics *, float);
int I_iclass_statistics_get_histo(IClass_statistics *, int, int, int *);
int I_iclass_statistics_get_product(IClass_statistics *, int, int, float *);
void I_iclass_init_statistics(IClass_statistics *, int, const char *,
                              const char *, float);
void I_iclass_free_statistics(IClass_statistics *);

/* iclass_signatures.c */
int I_iclass_init_signatures(struct Signature *, struct Ref *);
void I_iclass_add_signature(struct Signature *, IClass_statistics *);
int I_iclass_write_signatures(struct Signature *, const char *);

/* list_gp.c */
int I_list_group(const char *, const struct Ref *, FILE *);
int I_list_group_simple(const struct Ref *, FILE *);
void I__list_group_name_fit(char *, const char *, const char *);

/* list_subgp.c */
char **I_list_subgroups(const char *, int *);
char **I_list_subgroups2(const char *, const char *, int *);
int I_list_subgroup(const char *, const char *, const struct Ref *, FILE *);
int I_list_subgroup_simple(const struct Ref *, FILE *);

/* loc_info.c */
char *I_location_info(const char *);

/* points.c */
int I_new_control_point(struct Control_Points *, double, double, double, double,
                        int);
int I_get_control_points(const char *, struct Control_Points *);
int I_put_control_points(const char *, const struct Control_Points *);

/* ref.c */
FILE *I_fopen_group_ref_new(const char *);
FILE *I_fopen_group_ref_old(const char *);
FILE *I_fopen_group_ref_old2(const char *, const char *);
FILE *I_fopen_subgroup_ref_new(const char *, const char *);
FILE *I_fopen_subgroup_ref_old(const char *, const char *);
FILE *I_fopen_subgroup_ref_old2(const char *, const char *, const char *);

/* iscatt_structs.c */
void I_sc_init_cats(struct scCats *, int, int);
void I_sc_free_cats(struct scCats *);
int I_sc_add_cat(struct scCats *);
int I_sc_insert_scatt_data(struct scCats *, struct scdScattData *, int, int);

void I_scd_init_scatt_data(struct scdScattData *, int, int, void *);

/* iscatt_core.c */
int I_compute_scatts(struct Cell_head *, struct scCats *, const char **,
                     const char **, int, struct scCats *, const char **);

int I_create_cat_rast(struct Cell_head *, const char *);
int I_insert_patch_to_cat_rast(const char *, struct Cell_head *, const char *);

int I_id_scatt_to_bands(const int, const int, int *, int *);
int I_bands_to_id_scatt(const int, const int, const int, int *);

int I_merge_arrays(unsigned char *, unsigned char *, unsigned, unsigned,
                   double);
int I_apply_colormap(unsigned char *, unsigned char *, unsigned,
                     unsigned char *, unsigned char *);
int I_rasterize(double *, int, unsigned char, struct Cell_head *,
                unsigned char *);
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

/* manage_signatures.c */
void I_get_signatures_dir(char *, I_SIGFILE_TYPE);
void I_make_signatures_dir(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);

/* manage_signatures.c */
void I__get_signatures_element(char *, I_SIGFILE_TYPE);
void I__make_signatures_element(I_SIGFILE_TYPE);
int I_signatures_remove(I_SIGFILE_TYPE, const char *);
int I_signatures_copy(I_SIGFILE_TYPE, const char *, const char *, const char *);
int I_signatures_rename(I_SIGFILE_TYPE, const char *, const char *);
int I_signatures_list_by_type(I_SIGFILE_TYPE, const char *, char ***);
void I_free_signatures_list(int, char ***);

/* sig.c */
int I_init_signatures(struct Signature *, int);
int I_new_signature(struct Signature *);
int I_free_signatures(struct Signature *);
int I_read_one_signature(FILE *, struct Signature *);
int I_read_signatures(FILE *, struct Signature *);
int I_write_signatures(FILE *, struct Signature *);
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
>>>>>>> osgeo-main
char **I_sort_signatures_by_bandref(struct Signature *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
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
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
char **I_sort_signatures_by_bandref(struct Signature *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
char **I_sort_signatures_by_bandref(struct Signature *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
char **I_sort_signatures_by_bandref(struct Signature *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
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
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
char **I_sort_signatures_by_bandref(struct Signature *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
char **I_sort_signatures_by_bandref(struct Signature *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
char **I_sort_signatures_by_bandref(struct Signature *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
char **I_sort_signatures_by_bandref(struct Signature *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
char **I_sort_signatures_by_semantic_label(struct Signature *,
                                           const struct Ref *);
=======
char **I_sort_signatures_by_bandref(struct Signature *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))

/* sigfile.c */
FILE *I_fopen_signature_file_new(const char *);
FILE *I_fopen_signature_file_old(const char *);

/* sigset.c */
int I_SigSetNClasses(struct SigSet *);
struct ClassData *I_AllocClassData(struct SigSet *, struct ClassSig *, int);
int I_InitSigSet(struct SigSet *, int);
struct ClassSig *I_NewClassSig(struct SigSet *);
struct SubSig *I_NewSubSig(struct SigSet *, struct ClassSig *);
int I_ReadSigSet(FILE *, struct SigSet *) WARN_UNUSED_RESULT;
int I_SetSigTitle(struct SigSet *, const char *);
const char *I_GetSigTitle(const struct SigSet *);
int I_SetClassTitle(struct ClassSig *, const char *);
const char *I_GetClassTitle(const struct ClassSig *);
int I_WriteSigSet(FILE *, const struct SigSet *);
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
>>>>>>> osgeo-main
char **I_SortSigSetByBandref(struct SigSet *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
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
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
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
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
char **I_SortSigSetByBandref(struct SigSet *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
char **I_SortSigSetByBandref(struct SigSet *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
char **I_SortSigSetByBandref(struct SigSet *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
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
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
char **I_SortSigSetByBandref(struct SigSet *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 48610916ed (ci: Ignore paths in CodeQL (#1778))
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
char **I_SortSigSetByBandref(struct SigSet *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> e74e6d91fb (ci: Ignore paths in CodeQL (#1778))
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 786079f5cb (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> f288517075 (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2aafbe628a (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 71c4313a63 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b12e9b488c (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c9edfa5984 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
char **I_SortSigSetByBandref(struct SigSet *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> be9d3e98f7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> ae360d0d05 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12a69d7f45 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c167de6248 (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 07dc2b7084 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> c489ae4cfb (ci: Ignore paths in CodeQL (#1778))
=======
=======
<<<<<<< HEAD
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
char **I_SortSigSetByBandref(struct SigSet *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 3df9e1b372 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 616e0cbcd7 (ci: Ignore paths in CodeQL (#1778))
<<<<<<< HEAD
>>>>>>> 6791e7c62b (ci: Ignore paths in CodeQL (#1778))
=======
=======
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
char **I_SortSigSetBySemanticLabel(struct SigSet *, const struct Ref *);
=======
char **I_SortSigSetByBandref(struct SigSet *, const struct Ref *);
>>>>>>> 268d757b7d (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 4d7f752c19 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> 1cda25dd26 (ci: Ignore paths in CodeQL (#1778))
>>>>>>> fac1ae18f5 (ci: Ignore paths in CodeQL (#1778))

/* sigsetfile.c */
FILE *I_fopen_sigset_file_new(const char *);
FILE *I_fopen_sigset_file_old(const char *);

/* target.c */
int I_get_target(const char *, char *, char *);
int I_put_target(const char *, const char *, const char *);

/* title.c */
int I_get_group_title(const char *, char *, int);
int I_put_group_title(const char *, const char *);

/* var.c */
double I_variance(double, double, int);
double I_stddev(double, double, int);

#endif
