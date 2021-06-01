R"""Setup, initialization, and clean-up functions

Functions can be used in Python scripts to setup a GRASS environment
and session without using grassXY.

Usage::

    import os
    import sys
    import subprocess

    # define GRASS Database
    # add your path to grassdata (GRASS GIS database) directory
    gisdb = "~/grassdata"
    # the following path is the default path on MS Windows
    # gisdb = "~/Documents/grassdata"

    # specify (existing) Location and Mapset
    location = "nc_spm_08"
    mapset = "user1"

    # path to the GRASS GIS launch script
    # we assume that the GRASS GIS start script is available and on PATH
    # query GRASS itself for its GISBASE
    # (with fixes for specific platforms)
    # needs to be edited by the user
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> faaa995e8d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e3f80cd27d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1dd78f2660 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cede709cae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5b921dce64 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
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
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
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
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1602cb9170 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> faaa995e8d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bf5f36a3d4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e3f80cd27d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5b921dce64 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1dd78f2660 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cede709cae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 810790e7dc (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b9c7d40d9b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> c67d5651fd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
    executable = "grass"
    if sys.platform.startswith("win"):
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
<<<<<<< HEAD
<<<<<<< HEAD
        # TODO: this have to be checked, maybe unix way is good enough
        grass8bin = '/Applications/GRASS/GRASS-8.0.app/'
<<<<<<< HEAD
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
<<<<<<< HEAD
<<<<<<< HEAD
        # TODO: this have to be checked, maybe unix way is good enough
        grass8bin = '/Applications/GRASS/GRASS-8.0.app/'
<<<<<<< HEAD
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b9c7d40d9b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    # query GRASS GIS itself for its Python package path
    grass_cmd = [executable, "--config", "python_path"]
    process = subprocess.run(grass_cmd, check=True, text=True, stdout=subprocess.PIPE)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
>>>>>>> 810790e7dc (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    executable = "grass"
    if sys.platform.startswith("win"):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # MS Windows
        executable = r"C:\OSGeo4W\bin\grass.bat"
        # uncomment when using standalone WinGRASS installer
        # executable = r'C:\Program Files (x86)\GRASS GIS <version>\grass.bat'
        # this can be skipped if GRASS executable is added to PATH
    elif sys.platform == "darwin":
        # Mac OS X
        version = "@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@"
        executable = f"/Applications/GRASS-{version}.app/Contents/Resources/bin/grass"

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
    grass8bin = 'grass'
    if sys.platform.startswith('win'):
        # MS Windows
        grass8bin = r'C:\OSGeo4W\bin\grass.bat'
        # uncomment when using standalone WinGRASS installer
        # grass8bin = r'C:\Program Files (x86)\GRASS GIS 8.0.0\grass.bat'
        # this can be avoided if GRASS executable is added to PATH
    elif sys.platform == 'darwin':
        # Mac OS X
        # TODO: this have to be checked, maybe unix way is good enough
        grass8bin = '/Applications/GRASS/GRASS-8.0.app/'

>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
    # query GRASS GIS itself for its GISBASE
    startcmd = [grass8bin, '--config', 'path']
    try:
        p = subprocess.Popen(startcmd, shell=False,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
    except OSError as error:
        sys.exit("ERROR: Cannot find GRASS GIS start script"
                 " {cmd}: {error}".format(cmd=startcmd[0], error=error))
    if p.returncode != 0:
        sys.exit("ERROR: Issues running GRASS GIS start script"
                 " {cmd}: {error}"
                 .format(cmd=' '.join(startcmd), error=err))
    gisbase = out.strip(os.linesep)

    # set GISBASE environment variable
    os.environ['GISBASE'] = gisbase
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
    # query GRASS GIS itself for its Python package path
    grass_cmd = [executable, "--config", "python_path"]
    process = subprocess.run(grass_cmd, check=True, text=True, stdout=subprocess.PIPE)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
    # query GRASS GIS itself for its Python package path
    grass_cmd = [executable, "--config", "python_path"]
    process = subprocess.run(grass_cmd, check=True, text=True, stdout=subprocess.PIPE)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
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
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 810790e7dc (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))

    # define GRASS-Python environment
    sys.path.append(process.stdout.strip())

    # import (some) GRASS Python bindings
    import grass.script as gs

    # launch session
    session = gs.setup.init(gisdb, location, mapset)

    # example calls
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> faaa995e8d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e3f80cd27d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1dd78f2660 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cede709cae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5b921dce64 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b9c7d40d9b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
    gs.message("Current GRASS GIS 8 environment:")
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    gs.message("Current GRASS GIS 8 environment:")
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
>>>>>>> osgeo-main
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> c67d5651fd (Programmer's manual: update GRASS GIS arch drawing (#1610))
    gs.message("Current GRASS GIS 8 environment:")
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> c67d5651fd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1602cb9170 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> bf5f36a3d4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    gs.message("Current GRASS GIS 8 environment:")
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
    gs.message("Current GRASS GIS 8 environment:")
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1602cb9170 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> faaa995e8d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> bf5f36a3d4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e3f80cd27d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5b921dce64 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1dd78f2660 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cede709cae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
    gs.message("Current GRASS GIS 8 environment:")
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 810790e7dc (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b9c7d40d9b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
    gs.message("Current GRASS GIS 8 environment:")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    gs.message('Current GRASS GIS 8 environment:')
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> c67d5651fd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
    print(gs.gisenv())

    gs.message("Available raster maps:")
    for rast in gs.list_strings(type="raster"):
        print(rast)

    gs.message("Available vector maps:")
    for vect in gs.list_strings(type="vector"):
        print(vect)

    # clean up at the end
    session.finish()


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
(C) 2010-2023 by the GRASS Development Team
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
(C) 2010-2023 by the GRASS Development Team
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4255a3409f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
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
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 506d884519 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 5a6c7b69e7 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
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
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> d0c4af5f80 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 099850264f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 3df1af6046 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 984f2e4b5f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 8f9937d00a (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> fa8258f7da (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c4ee228391 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> f3d76d90e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> d88b10832d (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 4c14c5377c (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 385c333a86 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> b13ee245c1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a7da23483e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> f59448a530 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> fb8e87c2a1 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 115d1c2b17 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> e0fc7e2fee (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 8da59835e3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1602cb9170 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> faaa995e8d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> fc4d6dbb1b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 1ac37540a5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bf5f36a3d4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e3f80cd27d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 3662b58228 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 40ae4b13c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5b921dce64 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 21a39e2108 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1dd78f2660 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 7c58471b8e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cede709cae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c1fe2d6941 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c745556f47 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 810790e7dc (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b9c7d40d9b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2788a5026e (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c67d5651fd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 506d884519 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 5a6c7b69e7 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
(C) 2010-2024 by the GRASS Development Team
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
=======
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> faaa995e8d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e3f80cd27d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1dd78f2660 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cede709cae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5b921dce64 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c67d5651fd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> 984f2e4b5f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> fa8258f7da (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> f3d76d90e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 4c14c5377c (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> b13ee245c1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> f59448a530 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 115d1c2b17 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 8da59835e3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 1ac37540a5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 40ae4b13c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> c745556f47 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4255a3409f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d0c4af5f80 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> c67d5651fd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 506d884519 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 5a6c7b69e7 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
<<<<<<< HEAD
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> d0c4af5f80 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 099850264f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 3df1af6046 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 984f2e4b5f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 8f9937d00a (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> fa8258f7da (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c4ee228391 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> f3d76d90e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> d88b10832d (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 4c14c5377c (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 385c333a86 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> b13ee245c1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> a7da23483e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> f59448a530 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> fb8e87c2a1 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 115d1c2b17 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> e0fc7e2fee (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 8da59835e3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1602cb9170 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> faaa995e8d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> fc4d6dbb1b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 1ac37540a5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> bf5f36a3d4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e3f80cd27d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 3662b58228 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 40ae4b13c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5b921dce64 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 21a39e2108 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1dd78f2660 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 7c58471b8e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cede709cae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c1fe2d6941 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c745556f47 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 810790e7dc (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b9c7d40d9b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
(C) 2010-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
(C) 2010-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 2788a5026e (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a344872c74 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c67d5651fd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5de9e271af (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a13c234f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> db147411fe (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b3ae6fbd5e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.

@author Martin Landa <landa.martin gmail.com>
@author Vaclav Petras <wenzeslaus gmail.com>
@author Markus Metz
"""

# TODO: this should share code from lib/init/grass.py
# perhaps grass.py can import without much trouble once GISBASE
# is known, this would allow moving things from there, here
# then this could even do locking

from pathlib import Path
import datetime
import os
import shutil
import subprocess
import sys
import tempfile as tmpfile

WINDOWS = sys.platform.startswith("win")
MACOS = sys.platform.startswith("darwin")

VERSION_MAJOR = "@GRASS_VERSION_MAJOR@"
VERSION_MINOR = "@GRASS_VERSION_MINOR@"


def write_gisrc(dbase, location, mapset):
    """Write the ``gisrc`` file and return its path."""
    with tmpfile.NamedTemporaryFile(mode="w", delete=False) as rc:
        gisrc = rc.name
        rc.write("GISDBASE: %s\n" % dbase)
        rc.write("LOCATION_NAME: %s\n" % location)
        rc.write("MAPSET: %s\n" % mapset)
    return gisrc


def set_gui_path():
    """Insert wxPython GRASS path to sys.path."""
    gui_path = os.path.join(os.environ["GISBASE"], "gui", "wxpython")
    if gui_path and gui_path not in sys.path:
        sys.path.insert(0, gui_path)


def get_install_path(path=None):
    """Get path to GRASS installation usable for setup of environmental variables.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
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
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS executable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Executable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase=None, *, env=None):
    """Setup the runtime environment.

    Modifies environment so that GRASS modules can run. It does not setup a session,
    but only the system environment to execute commands.

    Modifies the environment provided with _env_. If _env_ is not
    provided, modifies the global environment (os.environ). Pass a copy of the
    environment if you don't want the source environment modified.

    If _gisbase_ is not provided, a heuristic is used to find the path to GRASS
    installation (see the :func:`get_install_path` function for details).
    """
    if not gisbase:
        gisbase = get_install_path()

    # Accept Path objects.
    gisbase = os.fspath(gisbase)

    # If environment is not provided, use the global one.
    if not env:
        env = os.environ

    from grass.app.runtime import (
        get_grass_config_dir,
        set_dynamic_library_path,
        set_executable_paths,
        set_path_to_python_executable,
        set_python_path_variable,
    )

    # Set GISBASE
    env["GISBASE"] = gisbase
    set_executable_paths(
        install_path=gisbase,
        grass_config_dir=get_grass_config_dir(VERSION_MAJOR, VERSION_MINOR, env=env),
        env=env,
    )
    set_dynamic_library_path(
        variable_name="@LD_LIBRARY_PATH_VAR@", install_path=gisbase, env=env
    )
    set_python_path_variable(install_path=gisbase, env=env)
    set_path_to_python_executable(env=env)


def init(path, location=None, mapset=None, *, grass_path=None, env=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1602cb9170 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> bf5f36a3d4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b9c7d40d9b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
=======
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1602cb9170 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> bf5f36a3d4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b9c7d40d9b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    # The path heuristic always uses the global environment.
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
<<<<<<< HEAD
=======
=======
=======
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

<<<<<<< HEAD
    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
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
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

<<<<<<< HEAD
    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
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

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
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
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))

    # If environment is not provided, use the global one.
    if not env:
        env = os.environ
    setup_runtime_env(grass_path, env=env)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======
<<<<<<< HEAD
<<<<<<< HEAD

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
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

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
=======
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
>>>>>>> osgeo-main


<<<<<<< HEAD

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
<<<<<<< HEAD
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

<<<<<<< HEAD
    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======
<<<<<<< HEAD

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
<<<<<<< HEAD
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
=======
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
<<<<<<< HEAD
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

<<<<<<< HEAD
    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
<<<<<<< HEAD
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
=======
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

<<<<<<< HEAD
        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.
=======

    The function tries to determine path tp GRASS GIS installation so that the
    returned path can be used for setup of environmental variable for GRASS runtime.
    If the search fails, None is returned.

    By default, the resulting path is derived relatively from the location of the
    Python package (specifically this module) in the file system. This derived path
    is returned only if it has subdirectories called ``bin`` and ``lib``.
    If the parameter or certain environmental variables are set, the following
    attempts are made to find the path.

    If *path* is provided and it is an existing executable, the executable is queried
    for the path. Otherwise, provided *path* is returned as is.

    If *path* is not provided, the GISBASE environmental variable is used as the path
    if it exists. If GRASSBIN environmental variable exists and it is an existing
    executable, the executable is queried for the path.

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

    If *path* is not provided and no relevant environmental variables are set, the
    default relative path search is performed.
    If that fails and executable called ``grass`` exists, it is queried for the path.
    None is returned if all the attempts failed.

    If an existing executable is called as a subprocess is called during the search
    and it fails, the CalledProcessError exception is propagated from the subprocess
    call.
    """

    def ask_executable(arg):
        """Query the GRASS exectable for the path"""
        return subprocess.run(
            [arg, "--config", "path"], text=True, check=True, capture_output=True
        ).stdout.strip()

    # Exectable was provided as parameter.
    if path and shutil.which(path):
        # The path was provided by the user and it is an executable
        # (on path or provided with full path), so raise exception on failure.
        return ask_executable(path)

    # Presumably directory was provided.
    if path:
        return path

    # GISBASE is already set.
    env_gisbase = os.environ.get("GISBASE")
    if env_gisbase:
        return env_gisbase

    # Executable provided in environment (name is from grass-session).
    # The variable is supported (here), documented, but not widely promoted
    # at this point (to be re-evaluated).
    grass_bin = os.environ.get("GRASSBIN")
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    # Derive the path from path to this file (Python module).
    # This is the standard way when there is no user-provided settings.
    # Uses relative path to find the right parent and then tests presence of lib
    # and bin. Removing 5 parts from the path works for
    # .../grass_install_prefix/etc/python/grass and also .../python3/dist-packages/.
    install_path = Path(*Path(__file__).parts[:-5])
    bin_path = install_path / "bin"
    lib_path = install_path / "lib"
    if bin_path.is_dir() and lib_path.is_dir():
        return install_path

    # As a last resort, try running grass command if it exists.
    # This is less likely give the right result than the relative path on systems
    # with multiple installations (where an explicit setup is likely required).
    # However, it allows for non-standard installations with standard command.
    grass_bin = "grass"
    if grass_bin and shutil.which(grass_bin):
        return ask_executable(grass_bin)

    return None


def setup_runtime_env(gisbase):
    """Setup the runtime environment.

    Modifies the global environment (os.environ) so that GRASS modules can run.
    """
    # Accept Path objects.
    gisbase = os.fspath(gisbase)
    # Set GISBASE
    os.environ["GISBASE"] = gisbase

    # define PATH
    path_addition = os.pathsep + os.path.join(gisbase, "bin")
    path_addition += os.pathsep + os.path.join(gisbase, "scripts")
    if WINDOWS:
        path_addition += os.pathsep + os.path.join(gisbase, "extrabin")

    # add addons to the PATH, use GRASS_ADDON_BASE if set
    # copied and simplified from lib/init/grass.py
    addon_base = os.getenv("GRASS_ADDON_BASE")
    if not addon_base:
        if WINDOWS:
            config_dirname = f"GRASS{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("APPDATA"), config_dirname, "addons")
        elif MACOS:
            version = f"{VERSION_MAJOR}.{VERSION_MINOR}"
            addon_base = os.path.join(
                os.getenv("HOME"), "Library", "GRASS", version, "Addons"
            )
        else:
            config_dirname = f".grass{VERSION_MAJOR}"
            addon_base = os.path.join(os.getenv("HOME"), config_dirname, "addons")
        os.environ["GRASS_ADDON_BASE"] = addon_base

    if not WINDOWS:
        path_addition += os.pathsep + os.path.join(addon_base, "scripts")
    path_addition += os.pathsep + os.path.join(addon_base, "bin")

    os.environ["PATH"] = path_addition + os.pathsep + os.getenv("PATH")
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

    setup_runtime_env(grass_path)

<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )

    setup_runtime_env(grass_path)

<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
<<<<<<< HEAD
<<<<<<< HEAD
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
=======
=======
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
        gisrc = gs.setup.init("/usr/bin/grass8",
                              "/home/john/grassdata",
                              "nc_spm_08", "user1")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

<<<<<<< HEAD
    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )
=======
    # add addons to the PATH
    # copied and simplified from lib/init/grass.py
    if mswin:
        config_dirname = "GRASS8"
        config_dir = os.path.join(os.getenv("APPDATA"), config_dirname)
    else:
        config_dirname = ".grass8"
        config_dir = os.path.join(os.getenv("HOME"), config_dirname)
    addon_base = os.path.join(config_dir, "addons")
    os.environ["GRASS_ADDON_BASE"] = addon_base
    if not mswin:
        os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "scripts")
    os.environ["PATH"] += os.pathsep + os.path.join(addon_base, "bin")
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))

    setup_runtime_env(grass_path)

>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
<<<<<<< HEAD
<<<<<<< HEAD
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )

    setup_runtime_env(grass_path)

>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )

    setup_runtime_env(grass_path)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )

    setup_runtime_env(grass_path)

<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )

    setup_runtime_env(grass_path)

<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    # TODO: lock the mapset?
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
=======
    # Set GRASS_PYTHON and PYTHONPATH to find GRASS Python modules
    if not os.getenv("GRASS_PYTHON"):
        if WINDOWS:
            os.environ["GRASS_PYTHON"] = "python3.exe"
        else:
            os.environ["GRASS_PYTHON"] = "python3"
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))


<<<<<<< HEAD
class SessionHandle:
    """Object used to manage GRASS sessions.

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======

def init(path, location=None, mapset=None, grass_path=None):
    """Initialize system variables to run GRASS modules

    This function is for running GRASS GIS without starting it with the
    standard main executable grass. No GRASS modules shall be called before
    call of this function but any module or user script can be called
    afterwards because a GRASS session has been set up. GRASS Python
    libraries are usable as well in general but the ones using C
    libraries through ``ctypes`` are not (which is caused by library
    path not being updated for the current process which is a common
    operating system limitation).

    When the path or specified mapset does not exist, ValueError is raised.

    The :func:`get_install_path` function is used to determine where
    the rest of GRASS files is installed. The *grass_path* parameter is
    passed to it if provided. If the path cannot be determined,
    ValueError is raised. Exceptions from the underlying function are propagated.

    To create a GRASS session a session file (aka gisrc file) is created.
    The session object returned by this function will take care of deleting it
    as long as the object is used as a context manager or the *finish* method
    of the object is called explicitly. Using methods of the session object is
    preferred over calling the function :func:`finish`.

    Basic usage::

        # ... setup GISBASE and sys.path before import
        import grass.script as gs
        session = gs.setup.init(
            "~/grassdata/nc_spm_08/user1",
            grass_path="/usr/lib/grass",
        )
        # ... use GRASS modules here
        # end the session
        session.finish()

    The returned object is a context manager, so the ``with`` statement can be used to
    ensure that the session is finished (closed) at the end::

        # ... setup sys.path before import
        import grass.script as gs
        with gs.setup.init("~/grassdata/nc_spm_08/user1")
            # ... use GRASS modules here

    :param path: path to GRASS database
    :param location: location name
    :param mapset: mapset within given location (default: 'PERMANENT')
    :param grass_path: path to GRASS installation or executable

    :returns: reference to a session handle object which is a context manager
    """
    grass_path = get_install_path(grass_path)
    if not grass_path:
        raise ValueError(
            _("Parameter grass_path or GISBASE environmental variable must be set")
        )
    # We reduce the top-level imports because this is initialization code.
    # pylint: disable=import-outside-toplevel
    from grass.grassdb.checks import get_mapset_invalid_reason, is_mapset_valid
    from grass.grassdb.manage import resolve_mapset_path

    # Support ~ in the path for user home directory.
    path = Path(path).expanduser()
    # A simple existence test. The directory, whatever it is, should exist.
    if not path.exists():
        raise ValueError(_("Path '{path}' does not exist").format(path=path))
    # A specific message when it exists, but it is a file.
    if path.is_file():
        raise ValueError(
            _("Path '{path}' is a file, but a directory is needed").format(path=path)
        )
    mapset_path = resolve_mapset_path(path=path, location=location, mapset=mapset)
    if not is_mapset_valid(mapset_path):
        raise ValueError(
            _("Mapset {path} is not valid: {reason}").format(
                path=mapset_path.path,
                reason=get_mapset_invalid_reason(
                    mapset_path.directory, mapset_path.location, mapset_path.mapset
                ),
            )
        )

    setup_runtime_env(grass_path)

>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
    # TODO: lock the mapset?
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
    env["GIS_LOCK"] = str(os.getpid())

    env["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle(env=env)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    os.environ["GIS_LOCK"] = str(os.getpid())

    os.environ["GISRC"] = write_gisrc(
        mapset_path.directory, mapset_path.location, mapset_path.mapset
    )
    return SessionHandle()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))


class SessionHandle:
    """Object used to manage GRASS sessions.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
class SessionHandle:
    """Object used to manage GRASS sessions.

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
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
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
    Do not create objects of this class directly. Use the *init* function
    to get a session object.

    Basic usage::

        # ... setup sys.path before import as needed

        import grass.script as gs

        session = gs.setup.init("~/grassdata/nc_spm_08/user1")

        # ... use GRASS modules here

        # end the session
        session.finish()

    Context manager usage::

        # ... setup sys.path before import as needed

        import grass.script as gs

        with gs.setup.init("~/grassdata/nc_spm_08/user1"):
            # ... use GRASS modules here
        # session ends automatically here
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    The example above is modifying the global, process environment (`os.environ`).
    If you don't want to modify the global environment, use the _env_ parameter
    for the _init_ function to modify the provided environment instead.
    This environment is then available as an attribute of the session object.
    The attribute then needs to be passed to all calls of GRASS
    tools and functions that wrap them.
    Context manager usage with custom environment::

        # ... setup sys.path before import as needed

        import grass.script as gs

        with gs.setup.init("~/grassdata/nc_spm_08/user1", env=os.environ.copy()):
            # ... use GRASS modules here with env parameter
            gs.run_command("g.region", flags="p", env=session.env)
        # session ends automatically here, global environment was never modifed
    """

    def __init__(self, *, env, active=True):
        self._env = env
=======
    """

    def __init__(self, active=True):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    """

    def __init__(self, active=True):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
        self._active = active
        self._start_time = datetime.datetime.now(datetime.timezone.utc)

    @property
    def active(self):
        """True if session is active (not finished)"""
        return self._active

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
    @property
    def env(self):
        return self._env

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
    def __enter__(self):
        """Enter the context manager context.

        Notably, the session is activated using the *init* function.

        :returns: reference to the object (self)
        """
        if not self.active:
            raise ValueError(
                "Attempt to use inactive (finished) session as a context manager"
            )
        return self

    def __exit__(self, type, value, traceback):
        """Exit the context manager context.

        Finishes the existing session.
        """
        self.finish()

    def finish(self):
        """Finish the session.

        If not used as a context manager, call explicitly to clean and close the mapset
        and finish the session. No GRASS modules can be called afterwards.
        """
        if not self.active:
            raise ValueError("Attempt to finish an already finished session")
        self._active = False
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
        finish(env=self._env, start_time=self._start_time)
=======
        finish(start_time=self._start_time)
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
        finish(start_time=self._start_time)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
        finish(start_time=self._start_time)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))


# clean-up functions when terminating a GRASS session
# these fns can only be called within a valid GRASS session


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
def clean_default_db(*, modified_after=None, env=None):
=======
def clean_default_db(*, modified_after=None):
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
def clean_default_db(*, modified_after=None):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
def clean_default_db(*, modified_after=None):
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    """Clean (vacuum) the default db if it is SQLite

    When *modified_after* is set, database is cleaned only when it was modified
    since the *modified_after* time.
    """
    # Limiting usage of in other function by lazy-imports.
    # pylint: disable=import-outside-toplevel
    import grass.script as gs

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    conn = gs.db_connection(env=env)
    if not conn or conn["driver"] != "sqlite":
        return
    # check if db exists
    gis_env = gs.gisenv(env=env)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    conn = gs.db_connection()
    if not conn or conn["driver"] != "sqlite":
        return
    # check if db exists
    gis_env = gs.gisenv()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    database = conn["database"]
    database = database.replace("$GISDBASE", gis_env["GISDBASE"])
    database = database.replace("$LOCATION_NAME", gis_env["LOCATION_NAME"])
    database = database.replace("$MAPSET", gis_env["MAPSET"])
    database = Path(database)
    if not database.is_file():
        return
    file_stat = database.stat()
    # Small size based on MEMORYMB (MiB) or its default.
    small_db_size = int(gis_env.get("MEMORYMB", 300)) * (1 << 20)
    if file_stat.st_size <= small_db_size:
        return
    if modified_after:
        modified_time = datetime.datetime.fromtimestamp(
            file_stat.st_mtime, tz=datetime.timezone.utc
        )
        if modified_after >= modified_time:
            return
    # Start the vacuum process, then show the message in parallel while
    # the vacuum is running. Finally, wait for the vacuum process to finish.
    # Error handling is the same as errors="ignore".
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    process = gs.start_command("db.execute", sql="VACUUM", env=env)
    gs.verbose(_("Cleaning up SQLite attribute database..."), env=env)
=======
    process = gs.start_command("db.execute", sql="VACUUM")
    gs.verbose(_("Cleaning up default SQLite database..."))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    process = gs.start_command("db.execute", sql="VACUUM")
    gs.verbose(_("Cleaning up default SQLite database..."))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    process.wait()


def call(cmd, **kwargs):
    """Wrapper for subprocess.call to deal with platform-specific issues"""
    if WINDOWS:
        kwargs["shell"] = True
    return subprocess.call(cmd, **kwargs)


<<<<<<< HEAD
def clean_temp(env=None):
=======
def clean_temp():
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    """Clean mapset temporary directory"""
    # Lazy-importing to reduce dependencies (this can be eventually removed).
    # pylint: disable=import-outside-toplevel
    import grass.script as gs

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    if not env:
        env = os.environ

    gs.verbose(_("Cleaning up temporary files..."), env=env)
    gisbase = env["GISBASE"]
    call(
        [os.path.join(gisbase, "etc", "clean_temp")], stdout=subprocess.DEVNULL, env=env
    )


def finish(*, env=None, start_time=None):
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    gs.verbose(_("Cleaning up temporary files..."))
    gisbase = os.environ["GISBASE"]
    call([os.path.join(gisbase, "etc", "clean_temp")], stdout=subprocess.DEVNULL)


def finish(*, start_time=None):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    """Terminate the GRASS session and clean up

    GRASS commands can no longer be used after this function has been
    called

    Basic usage::
        import grass.script as gs

        gs.setup.finish()

    The function is not completely symmetrical with :func:`init` because it only
    closes the mapset, but doesn't undo the runtime environment setup.

    When *start_time* is set, it might be used to determine cleaning procedures.
    Currently, it is used to do SQLite database vacuum only when database was modified
    since the session started.
    """
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    if not env:
        env = os.environ

    clean_default_db(modified_after=start_time, env=env)
    clean_temp(env=env)
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    clean_default_db(modified_after=start_time)
    clean_temp()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    # TODO: unlock the mapset?
    # unset the GISRC and delete the file
    from grass.script import utils as gutils

    gutils.try_remove(env["GISRC"])
    del env["GISRC"]
    # remove gislock env var (not the gislock itself
    del env["GIS_LOCK"]
