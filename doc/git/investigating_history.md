# Investigating Code History

## Plain git blame

In command line, to investigate commits which introduced a certain
piece of code, you can use `git blame`:

```sh
git blame scripts/r.mask/r.mask.py
```

This will give you current content of the file with commit hash and author
associated with each line.

## Ignore some commits with git blame

Over the course of time, there was a lot of code reformatting
changes which you typically want to ignore. These, often whitespace-only
changes, can be filtered out using a _ignore-revs_ file in the source code
root directory:

```sh
git blame scripts/r.mask/r.mask.py --ignore-revs-file .git-blame-ignore-revs
```

In some cases, ignoring formatting changes may not be appropriate, for example
when investigating automated checks of formatting.
If you think the _ignore-revs_ file contains commits which should be never
ignored with `git blame`, please open an issue.
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 92d65cd4a6 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f75642e9e3 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))

## On GitHub

GitHub interface does not allow to use the ignore-revs file. However, it is
easy to move over a revision by pressing "View blame prior to this change"
which is the icon between commit info and line numbers.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> f75642e9e3 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 92d65cd4a6 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 7b6920a07b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> c68c553712 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 979d695cf4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 92d65cd4a6 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 84b0de4a0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f75642e9e3 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
