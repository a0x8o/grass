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
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0b689384c0 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 486a1e2551 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ce58cb82a (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dd9ee76548 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 1dfda93def (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 0b689384c0 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 486a1e2551 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 7ce58cb82a (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> c75ae04d0e (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dd9ee76548 (pygrass: Add update parameters method to Module (#1712))
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
>>>>>>> c75ae04d0e (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0b689384c0 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 486a1e2551 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7ce58cb82a (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8d4a4cbf97 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11243252e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dc9007cf68 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04cce48c99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 252e8801e9 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ad14dca817 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 2ba6ea4638 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 5eabce4769 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d2deec5b99 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 799750b257 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 62d0febf95 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> b4ca4c9a56 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> e9d37a972c (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 4f7a1fd8f9 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fdbfa0cdb6 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> c428d906c4 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 18cf7b413d (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> de793b6ebf (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> f2a5fffa6c (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 7f529ced08 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> fb51144890 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 0110f9a6c3 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> 6e4511d349 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 790e05082d (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> d047b12a28 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 9db651a043 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> aa770628e6 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> dd9ee76548 (pygrass: Add update parameters method to Module (#1712))
=======
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> c0f0b4ecd0 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> ca553cee6d (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> aa257e5504 (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
>>>>>>> defcd4d416 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 1dfda93def (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> ce5b8fc2e2 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 0b689384c0 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 4d2040e836 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 486a1e2551 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 74d3fa3265 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 7ce58cb82a (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a8f46081 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> db8f3cba13 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
>>>>>>> c75ae04d0e (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
