/******************************************************************************
 *
 * MODULE:      Grass Include Files
 * AUTHOR(S):   Original author unknown - probably CERL
 *              Justin Hickey - Thailand - jhickey@hpcc.nectec.or.th
 * PURPOSE:     This file contains definitions of variables and data types
 *              for use with most, if not all, Grass programs. This file is
 *              usually included in every Grass program.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
<<<<<<< HEAD
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 795aee5c6f (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d0c4af5f80 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 795aee5c6f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 21a39e2108 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1dd78f2660 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 7c58471b8e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cede709cae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
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
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 9948fbb36e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> ac7f228232 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8e2515c338 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> b0df4259cb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a48c908497 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8fa2e934ed (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bea6abbdbb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2c59b4c8e3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 32ab3d616a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> a40d5515e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 795aee5c6f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 9f9fbb1a9f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 91916b041f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> bb4f048d28 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c7c43ef8e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> ae631bd878 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8d33ff1f0a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cbdc95a863 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> e93342de07 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cef7c42a97 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> fd0bbace5c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 8f9937d00a (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 6a32c1731d (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 540a6bdb38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ce8d959206 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c4ee228391 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 4061759949 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 55237d751f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 203bdcfaf9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> d88b10832d (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 824abbc8d7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 0d6a6602db (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8adb120ce5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 385c333a86 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> c92112410b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 987a3940c6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 99eee3faab (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> a7da23483e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 0ce7d7b652 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> eeefe6e622 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7fca389202 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> fb8e87c2a1 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> d635888aa1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> f7a3476eb7 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 830456eca9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> e0fc7e2fee (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 899ab996ca (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 91926d3c70 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 1602cb9170 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c51ce64d3e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> fc4d6dbb1b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> db7c12aef8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 6905d5ab06 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bf5f36a3d4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 33f84048ae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 3662b58228 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 6ea7e101f9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b2fc7618a1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> c06b25ffae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> e8701b182a (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9b7ec184c4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a8edd4b153 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c23f495b50 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 7c58471b8e (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> d29537714a (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> f44c9d2be9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 152a82497c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> df02c52711 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c1fe2d6941 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> ba5db0e234 (i.maxlik: fix crash when classification result is NULL (#2724))
 * COPYRIGHT:   (C) 2000-2024 by the GRASS Development Team
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 9b7ec184c4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a8edd4b153 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> f44c9d2be9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 152a82497c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5b921dce64 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> c06b25ffae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8d33ff1f0a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cbdc95a863 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cef7c42a97 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fd0bbace5c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 540a6bdb38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ce8d959206 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 55237d751f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 203bdcfaf9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0d6a6602db (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8adb120ce5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 987a3940c6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 99eee3faab (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> eeefe6e622 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7fca389202 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> f7a3476eb7 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 830456eca9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 91926d3c70 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c51ce64d3e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6905d5ab06 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 33f84048ae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b2fc7618a1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8c7c43ef8e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> bb4f048d28 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f9fbb1a9f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8e2515c338 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a48c908497 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8fa2e934ed (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2c59b4c8e3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 32ab3d616a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 795aee5c6f (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> ac7f228232 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
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
=======
=======
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
>>>>>>> b0df4259cb (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
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
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ac7f228232 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c23f495b50 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> df02c52711 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ba5db0e234 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d29537714a (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 6ea7e101f9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> db7c12aef8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 899ab996ca (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d635888aa1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 0ce7d7b652 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> c92112410b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 824abbc8d7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 4061759949 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 6a32c1731d (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> e93342de07 (i.maxlik: fix crash when classification result is NULL (#2724))
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
=======
=======
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
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
<<<<<<< HEAD
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
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> bea6abbdbb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> a40d5515e7 (i.maxlik: fix crash when classification result is NULL (#2724))
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
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ac7f228232 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8e2515c338 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
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
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6eb93fb226 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 8fa2e934ed (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 82d088b867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3df1af6046 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b40f45f8a4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> cbdc95a863 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> e93342de07 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 984f2e4b5f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f67335359e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> fd0bbace5c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 816281ce6b (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 6a32c1731d (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 8f9937d00a (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fa8258f7da (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b425480f72 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ce8d959206 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> a0ce5c372a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 4061759949 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c4ee228391 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f3d76d90e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7df781f836 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 203bdcfaf9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5bd99675a5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 14bf5d86fb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9e655d2081 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 824abbc8d7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> d88b10832d (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c14c5377c (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f7cb2bbf2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 8adb120ce5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1e537538ac (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e421dd047f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 614639d14c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> c92112410b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 385c333a86 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b13ee245c1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e49b9ba256 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 99eee3faab (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 52df9f3ae3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fa1324421c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 0ce7d7b652 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> a7da23483e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f59448a530 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebf35028aa (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7fca389202 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1f45827248 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b0b0c9640 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 27caa3526a (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> d635888aa1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> fb8e87c2a1 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 115d1c2b17 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a9c8ff66a0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 830456eca9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 6d53e5e968 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 961f30fb7c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 75205cb772 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 899ab996ca (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> e0fc7e2fee (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8da59835e3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 26d1969f01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> c51ce64d3e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1602cb9170 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> faaa995e8d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 6caabc686d (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> db7c12aef8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> fc4d6dbb1b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1ac37540a5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 14f59e9b25 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 33f84048ae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> bf5f36a3d4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e3f80cd27d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> f04c2ba007 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 6ea7e101f9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3662b58228 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 40ae4b13c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 3662b58228 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> b2fc7618a1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c7457226a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> c06b25ffae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
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
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
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
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 21a39e2108 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dca52defdd (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a8edd4b153 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 7589c3e701 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1dd78f2660 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c23f495b50 (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 480ff97f17 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> d29537714a (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 7c58471b8e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 69dd884040 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 152a82497c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 84a2937271 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cede709cae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> df02c52711 (r.terrafow: explicit use of default constructors (#2660))
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 98158c2867 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> ba5db0e234 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c1fe2d6941 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> c745556f47 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 810790e7dc (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b9c7d40d9b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a2602d8078 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
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
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f7b8bdee1e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> ac7f228232 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8e2515c338 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> b0df4259cb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> a48c908497 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8fa2e934ed (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 3baa5ce440 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> bea6abbdbb (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5168f3664a (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 2c59b4c8e3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 32ab3d616a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40375e6e48 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
<<<<<<< HEAD
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> a40d5515e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 795aee5c6f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 9f9fbb1a9f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> e24e5f484d (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 91916b041f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> bb4f048d28 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 8c7c43ef8e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
<<<<<<< HEAD
>>>>>>> 3c42aaaec5 (Merge branch 'a0x8o' into stag0)
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> ae631bd878 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8d33ff1f0a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cbdc95a863 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5208c5ec0d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> e93342de07 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 9f5464914c (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> cef7c42a97 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fd0bbace5c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c80fee3 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 6a32c1731d (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d4ef6f4dbb (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 540a6bdb38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ce8d959206 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6abd882752 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4061759949 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 6036b7efea (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 55237d751f (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 203bdcfaf9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 402b36ee01 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 824abbc8d7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 2196f43bbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 0d6a6602db (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8adb120ce5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9bca96686b (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c92112410b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 987a3940c6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 99eee3faab (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 60fcd55b3f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 0ce7d7b652 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> cf7da16d77 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> eeefe6e622 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7fca389202 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 243520680f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d635888aa1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 440306d285 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> f7a3476eb7 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 830456eca9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 69ab96ba5d (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 899ab996ca (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 92dccbb571 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 91926d3c70 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c51ce64d3e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d80eba7255 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> db7c12aef8 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 72a23cdfbd (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 6905d5ab06 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 33f84048ae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 421dbe1c51 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 3662b58228 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 6ea7e101f9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> a74ea9a4bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> b2fc7618a1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> c06b25ffae (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 4126e4bd7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 352c339deb (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
>>>>>>> 24ea37df0a (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
=======
 * COPYRIGHT:   (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> e8701b182a (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 66010df1ab (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9b7ec184c4 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a8edd4b153 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c23f495b50 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> d29537714a (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> d2ca6e75c1 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> f44c9d2be9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 152a82497c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> df02c52711 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> ba5db0e234 (i.maxlik: fix crash when classification result is NULL (#2724))
 *
 *              This program is free software under the GNU General Public
 *              License (>=v2). Read the file COPYING that comes with GRASS
 *              for details.
 *
 *****************************************************************************/

#ifndef GRASS_GIS_H
#define GRASS_GIS_H

/*============================= Include Files ==============================*/

/* System include files */
#include <stdio.h>
#include <stdarg.h>
#include <stdbool.h>
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
=======

>>>>>>> 9824e0155a (libgis: Enable the C99 bool type (#1567))
>>>>>>> 04884a7159 (libgis: Enable the C99 bool type (#1567))
=======
=======

<<<<<<< HEAD
>>>>>>> 9824e0155a (libgis: Enable the C99 bool type (#1567))
=======

>>>>>>> d80ad342af (libgis: Enable the C99 bool type (#1567))
>>>>>>> a102657b5b (libgis: Enable the C99 bool type (#1567))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9824e0155a (libgis: Enable the C99 bool type (#1567))
=======

>>>>>>> d80ad342af (libgis: Enable the C99 bool type (#1567))

=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
/* Grass and local include files */
#include <grass/config.h>
#include <grass/datetime.h>
#include <grass/version.h>

/*=========================== Constants/Defines ============================*/

#if !defined __GNUC__ || __GNUC__ < 2
#undef __attribute__
#define __attribute__(x)
#endif

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
static const char *GRASS_copyright __attribute__((unused)) =
    "GRASS GNU GPL licensed Software";
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
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
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
static const char *GRASS_copyright __attribute__((unused)) =
    "GRASS GNU GPL licensed Software";
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
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
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
static const char *GRASS_copyright __attribute__((unused)) =
    "GRASS GNU GPL licensed Software";
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
/*!
    \def UNUSED
    \brief A macro for an attribute, if attached to a variable,
           indicating that the variable is not used
*/
#if (defined(__GNUC__) || defined(__APPLE__)) && !defined(_MSC_VER)
#define UNUSED __attribute__((unused))
#else
#define UNUSED
#endif

static const char *GRASS_copyright UNUSED = "GRASS GNU GPL licensed Software";

/*!
    \def FALLTHROUGH
    \brief A macro for a fallthrough statement attribute
 */
#if (defined(__GNUC__) && __GNUC__ >= 7) || \
    (defined(__clang__) && __clang_major__ >= 12)
#define FALLTHROUGH __attribute__((__fallthrough__))
#else
#define FALLTHROUGH ((void)0)
#endif
=======
static const char *GRASS_copyright __attribute__((unused)) =
    "GRASS GNU GPL licensed Software";
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
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
static const char *GRASS_copyright __attribute__((unused)) =
    "GRASS GNU GPL licensed Software";
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
static const char *GRASS_copyright __attribute__((unused)) =
    "GRASS GNU GPL licensed Software";
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
static const char *GRASS_copyright __attribute__((unused)) =
    "GRASS GNU GPL licensed Software";
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
static const char *GRASS_copyright __attribute__((unused)) =
    "GRASS GNU GPL licensed Software";
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))

/* GRASS version, GRASS date, git short hash of last change in GRASS headers
 * (and anything else in include)
 */
#define GIS_H_VERSION  GRASS_HEADERS_VERSION
/* git date of last change in GRASS headers
 * (and anything else in include)
 */
#define GIS_H_DATE     GRASS_HEADERS_DATE

#define G_gisinit(pgm) G__gisinit(GIS_H_VERSION, (pgm))
#define G_no_gisinit() G__no_gisinit(GIS_H_VERSION)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 04884a7159 (libgis: Enable the C99 bool type (#1567))
=======
>>>>>>> a102657b5b (libgis: Enable the C99 bool type (#1567))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
/* For boolean values and comparisons use the C99 type 'bool' with values 'true'
 */
/* and 'false' For historical reasons 'TRUE' and 'FALSE' are still valid. */
=======
/* For boolean values and comparisons use the C99 type 'bool' with values 'true' */
/* and 'false' For historical reasons 'TRUE' and 'FALSE' are still valid.        */
>>>>>>> 9824e0155a (libgis: Enable the C99 bool type (#1567))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a102657b5b (libgis: Enable the C99 bool type (#1567))
=======
/* For boolean values and comparisons use the C99 type 'bool' with values 'true' */
/* and 'false' For historical reasons 'TRUE' and 'FALSE' are still valid.        */
>>>>>>> d80ad342af (libgis: Enable the C99 bool type (#1567))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
/* For boolean values and comparisons use the C99 type 'bool' with values 'true'
 */
/* and 'false' For historical reasons 'TRUE' and 'FALSE' are still valid. */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
/* For boolean values and comparisons use the C99 type 'bool' with values 'true'
 */
/* and 'false' For historical reasons 'TRUE' and 'FALSE' are still valid. */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 04884a7159 (libgis: Enable the C99 bool type (#1567))
=======
>>>>>>> a102657b5b (libgis: Enable the C99 bool type (#1567))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
#ifndef TRUE
#define TRUE true
#endif

#ifndef FALSE
#define FALSE false
#endif

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
#if (defined(_FILE_OFFSET_BITS) && _FILE_OFFSET_BITS == 64) || \
    (__APPLE__ && __LP64__)
#define PRI_OFF_T "lld"
#else
#define PRI_OFF_T "ld"
#endif

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
/*! \brief Cross-platform Newline Character */
#define NEWLINE '\n'
#ifdef __MINGW32__
#define HOST_NEWLINE "\r\n"
#else
#define HOST_NEWLINE "\n"
#endif

/*! \brief Generate warning if function return value is unused */
#if __GNUC__ && (__GNUC__ >= 3 && __GNUC_MINOR__ >= 4)
#define WARN_UNUSED_RESULT __attribute__((warn_unused_result))
#else
#define WARN_UNUSED_RESULT
#endif

/*!
   \brief List of units
 */
#define U_UNDEFINED      -1
#define U_UNKNOWN        0
#define U_ACRES          1
#define U_HECTARES       2
#define U_KILOMETERS     3
#define U_METERS         4
#define U_MILES          5
#define U_FEET           6
#define U_RADIANS        7
#define U_DEGREES        8
#define U_USFEET         9
/* Temporal units from the datetime library */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e4d094b27b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bb044e52a8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d31cefad27 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 50dae61d8a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e7c536a439 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1441209c21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> db1cab9e66 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 85473eb6fe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e70fb84cab (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> ff5f864abb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81dde7e207 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c97738e09a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 658bea94d3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6d38446ead (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a6c7b3c876 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> dfca57e539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fb41c5cb2c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 04b9bde698 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a421be38ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fdfe3076fc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> adbcdc696e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b3d4c5eec4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a3fd93f832 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 7c71fbf389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
=======
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 0165b4754d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 48c92dd29d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3e7f56ab79 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f7b0361d9b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 760c96ff4b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
=======
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
=======
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
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
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 239ace486a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e4d094b27b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 907c1a8f92 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bb044e52a8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d31cefad27 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 11c95a7e4c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 50dae61d8a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e7c536a439 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 9271ad3d81 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1441209c21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> db1cab9e66 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 29172996a1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 85473eb6fe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e70fb84cab (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 00c0900a9a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff5f864abb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 81dde7e207 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> f119715acf (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c97738e09a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6ad2b2c24d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b0540bd24a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c9b16b100b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68e94e2177 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> cbeae81312 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 884fa1f156 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5045211539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> db36001fbe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bcb3a34081 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 3e7f56ab79 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f7b0361d9b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 239ace486a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 760c96ff4b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> eed879a954 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 658bea94d3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6d38446ead (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e65feed612 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 3ca117bbc2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2094945168 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> a6c7b3c876 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> dfca57e539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> fb41c5cb2c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 04b9bde698 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 907c1a8f92 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> a421be38ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 11c95a7e4c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> fdfe3076fc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 9271ad3d81 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> adbcdc696e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 29172996a1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b3d4c5eec4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 00c0900a9a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> a3fd93f832 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> f119715acf (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 7c71fbf389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b0540bd24a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b1f5dff731 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1cc6936fc1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> cbeae81312 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 4058ea1900 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 2873114db3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> db36001fbe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9bf6943cfb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
#define U_YEARS          DATETIME_YEAR
#define U_MONTHS         DATETIME_MONTH
#define U_DAYS           DATETIME_DAY
#define U_HOURS          DATETIME_HOUR
#define U_MINUTES        DATETIME_MINUTE
#define U_SECONDS        DATETIME_SECOND
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> osgeo-main
=======
=======
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3e7f56ab79 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> f7b0361d9b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 760c96ff4b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 239ace486a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
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
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e4d094b27b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 907c1a8f92 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bb044e52a8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d31cefad27 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 11c95a7e4c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 50dae61d8a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e7c536a439 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9271ad3d81 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1441209c21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> db1cab9e66 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 29172996a1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 85473eb6fe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e70fb84cab (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 00c0900a9a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> ff5f864abb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 81dde7e207 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f119715acf (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c97738e09a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6ad2b2c24d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b0540bd24a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c9b16b100b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 68e94e2177 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbeae81312 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 884fa1f156 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 5045211539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> db36001fbe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bcb3a34081 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 0165b4754d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 48c92dd29d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 3e7f56ab79 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f7b0361d9b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 760c96ff4b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
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
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> eed879a954 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 658bea94d3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6d38446ead (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e65feed612 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 3ca117bbc2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2094945168 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a6c7b3c876 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> dfca57e539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fb41c5cb2c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 04b9bde698 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 907c1a8f92 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a421be38ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 11c95a7e4c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fdfe3076fc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9271ad3d81 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> adbcdc696e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 29172996a1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b3d4c5eec4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 00c0900a9a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a3fd93f832 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f119715acf (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 7c71fbf389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b0540bd24a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b1f5dff731 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1cc6936fc1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbeae81312 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 4058ea1900 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2873114db3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> db36001fbe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9bf6943cfb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
#define U_YEARS         DATETIME_YEAR
#define U_MONTHS        DATETIME_MONTH
#define U_DAYS          DATETIME_DAY
#define U_HOURS         DATETIME_HOUR
#define U_MINUTES       DATETIME_MINUTE
#define U_SECONDS       DATETIME_SECOND
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 1cc6936fc1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 4058ea1900 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 2873114db3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9bf6943cfb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b0540bd24a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b1f5dff731 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 7c71fbf389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a3fd93f832 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b3d4c5eec4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> adbcdc696e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fdfe3076fc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a421be38ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 04b9bde698 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fb41c5cb2c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> dfca57e539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a6c7b3c876 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 2094945168 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3ca117bbc2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e65feed612 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e4d094b27b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bb044e52a8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d31cefad27 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 50dae61d8a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e7c536a439 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1441209c21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> db1cab9e66 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 85473eb6fe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e70fb84cab (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> ff5f864abb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 81dde7e207 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c97738e09a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 68e94e2177 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 884fa1f156 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5045211539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bcb3a34081 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b0540bd24a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c9b16b100b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 6ad2b2c24d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 0165b4754d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 48c92dd29d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3e7f56ab79 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f7b0361d9b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 760c96ff4b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> eed879a954 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 658bea94d3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6d38446ead (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 3e7f56ab79 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> f7b0361d9b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 760c96ff4b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 239ace486a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 073cd3f76c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> eed879a954 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e2cdbc7bf5 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 658bea94d3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d95da6adeb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 6d38446ead (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d6e9b6bb9c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c104fc60dc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 31b55bff37 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe652fab2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> a6c7b3c876 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c6d94bdfdc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> dfca57e539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7d3c75e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a2fae8c22 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> fb41c5cb2c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbf5dacd51 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 36d43bcb43 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 04b9bde698 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e8c04688ee (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 82879813d8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e4d094b27b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> a421be38ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 907c1a8f92 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bb044e52a8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d31cefad27 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> fdfe3076fc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 11c95a7e4c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 50dae61d8a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e7c536a439 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> adbcdc696e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9271ad3d81 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1441209c21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> db1cab9e66 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3d4c5eec4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 29172996a1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 85473eb6fe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e70fb84cab (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> a3fd93f832 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 00c0900a9a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ff5f864abb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 81dde7e207 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 7c71fbf389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f119715acf (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c97738e09a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6ad2b2c24d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b0540bd24a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c9b16b100b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68e94e2177 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 4058ea1900 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbeae81312 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 884fa1f156 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5045211539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 9bf6943cfb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> db36001fbe (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bcb3a34081 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 0165b4754d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 48c92dd29d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
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
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3e7f56ab79 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f7b0361d9b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 760c96ff4b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> eed879a954 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e2e2590594 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 658bea94d3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6d38446ead (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e0f80e91ca (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e65feed612 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 3ca117bbc2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> bd4e4b319f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 2094945168 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a6c7b3c876 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> dfca57e539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fb41c5cb2c (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 04b9bde698 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a421be38ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fdfe3076fc (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> adbcdc696e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b3d4c5eec4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a3fd93f832 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 7c71fbf389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b0540bd24a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b1f5dff731 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1cc6936fc1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 4058ea1900 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 2873114db3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9bf6943cfb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))

/*! \brief Projection code - XY coordinate system (unreferenced data) */
#define PROJECTION_XY    0
/*! \brief Projection code - UTM */
#define PROJECTION_UTM   1
/*! \brief Projection code - State Plane */
#define PROJECTION_SP    2
/*! \brief Projection code - Latitude-Longitude */
#define PROJECTION_LL    3
/*! \brief Projection code - other projection (other then noted above) */
#define PROJECTION_OTHER 99

#define PROJECTION_FILE  "PROJ_INFO"
#define UNIT_FILE        "PROJ_UNITS"
#define EPSG_FILE        "PROJ_EPSG"
#define WKT_FILE         "PROJ_WKT"
#define SRID_FILE        "PROJ_SRID"

#ifdef __MINGW32__
#define CONFIG_DIR "GRASS8"
#else
#define CONFIG_DIR ".grass8"
#endif

#ifdef MAX
#undef MAX
#endif
#define MAX(a, b) ((a) > (b) ? (a) : (b))

#ifdef MIN
#undef MIN
#endif
#define MIN(a, b) ((a) < (b) ? (a) : (b))

/* define PI and friends */
#undef M_PI
#define M_PI 3.14159265358979323846 /* pi */

#undef M_PI_2
#define M_PI_2 1.57079632679489661923 /* pi/2 */

#undef M_PI_4
#define M_PI_4 0.78539816339744830962 /* pi/4 */

#undef M_R2D
#define M_R2D 57.295779513082320877 /* 180/pi */

#undef M_D2R
#define M_D2R               0.017453292519943295769 /* pi/180 */

/* epsilon (IEEE: 2.220446e-16) */
#define GRASS_EPSILON       1.0e-15

/* Location of envariment variables */
#define G_VAR_GISRC         0
#define G_VAR_MAPSET        1

/* Where to find/store variables */
#define G_GISRC_MODE_FILE   0 /* files */
#define G_GISRC_MODE_MEMORY 1 /* memory only */

/* for G_parser() */
#define TYPE_INTEGER        1
#define TYPE_DOUBLE         2
#define TYPE_STRING         3
#define YES                 1
#define NO                  0

/* File/directory name lengths */
#define GNAME_MAX           256
#define GMAPSET_MAX         256

#define GPATH_MAX           4096

/* Basename default separator */
#define GBASENAME_SEP       "_"

/* Macros for type size independent integers                    */
/* Use these for portability to ensure integers are truly 32bit */
/* and are handled in a uniform manner                          */

/* Convert integer to 4 bytes - little endian */
#define serialize_int32_le(buf, x)     \
    do {                               \
        (buf)[0] = ((x) >> 0) & 0xFF;  \
        (buf)[1] = ((x) >> 8) & 0xFF;  \
        (buf)[2] = ((x) >> 16) & 0xFF; \
        (buf)[3] = ((x) >> 24) & 0xFF; \
    } while (0)

/* Convert 4 bytes to an integer - little endian */
#define deserialize_int32_le(buf) \
    (((buf)[0] << 0) | ((buf)[1] << 8) | ((buf)[2] << 16) | ((buf)[3] << 24))

/* Convert integer to 4 bytes - big endian */
#define serialize_int32_be(buf, x)     \
    do {                               \
        (buf)[0] = ((x) >> 24) & 0xFF; \
        (buf)[1] = ((x) >> 16) & 0xFF; \
        (buf)[2] = ((x) >> 8) & 0xFF;  \
        (buf)[3] = ((x) >> 0) & 0xFF;  \
    } while (0)

/* Convert 4 bytes to an integer - big endian */
#define deserialize_int32_be(buf) \
    (((buf)[0] << 24) | ((buf)[1] << 16) | ((buf)[2] << 8) | ((buf)[3] << 0))

/* Cross-platform Directory Separator Character and null device stuff */
#define GRASS_DIRSEP '/'
#ifdef __MINGW32__
#define HOST_DIRSEP '\\'
#define G_DEV_NULL  "NUL:"
#else
#define HOST_DIRSEP '/'
#define G_DEV_NULL  "/dev/null"
#endif

/*!
   \typedef STD_OPT
   \brief Standard option identifiers (enum)

   Identifies of all recognized standard options.

   The term <em>old</em> in the descriptions means existing map which
   is supposed to exist before the module is called.
   On the other hand, the term <em>new</em> in the descriptions means
   that the map is not supposed to exist and that module will create one.

   Used by the G_parser() system.

   IMPORTANT NOTE: when adding new item to STD_OPT you should also
   update STD_OPT_STRINGS array in general/g.parser/standard_option.c.

 */
typedef enum {
    G_OPT_UNDEFINED,
    G_OPT_DB_SQL,       /*!< SQL statements */
    G_OPT_DB_WHERE,     /*!< SQL where conditions */
    G_OPT_DB_TABLE,     /*!< table name */
    G_OPT_DB_DRIVER,    /*!< driver name */
    G_OPT_DB_DATABASE,  /*!< database name */
    G_OPT_DB_SCHEMA,    /*!< database schema */
    G_OPT_DB_COLUMN,    /*!< one attr column */
    G_OPT_DB_COLUMNS,   /*!< one or more attr columns */
    G_OPT_DB_KEYCOLUMN, /*!< key column */

    G_OPT_I_GROUP,    /*!< old input imagery group */
    G_OPT_I_SUBGROUP, /*!< old input imagery subgroup */

    G_OPT_MEMORYMB,      /*!< Maximum memory to be used (in MB): cache size for
                            raster rows */
    G_OPT_R_INPUT,       /*!< old input raster map */
    G_OPT_R_INPUTS,      /*!< old input raster maps */
    G_OPT_R_OUTPUT,      /*!< new output raster map */
    G_OPT_R_OUTPUTS,     /*!< new output raster maps */
    G_OPT_R_MAP,         /*!< old input raster map */
    G_OPT_R_MAPS,        /*!< old input rasters map */
    G_OPT_R_BASE,        /*!< old input base raster map */
    G_OPT_R_COVER,       /*!< old input cover raster map */
    G_OPT_R_ELEV,        /*!< old input elevation raster map */
    G_OPT_R_ELEVS,       /*!< old input elevation raster maps */
    G_OPT_R_TYPE,        /*!< raster map type */
    G_OPT_R_INTERP_TYPE, /*!< interpolation type */
    G_OPT_R_BASENAME_INPUT,  /*!< old input basename raster maps */
    G_OPT_R_BASENAME_OUTPUT, /*!< new output basename raster maps */

    G_OPT_R3_INPUT,  /*!< old input raster3d map */
    G_OPT_R3_INPUTS, /*!< old input raster3d maps */
    G_OPT_R3_OUTPUT, /*!< new output raster3d map */
    G_OPT_R3_MAP,    /*!< old input raster3d map */
    G_OPT_R3_MAPS,   /*!< old input raster3d maps */
    G_OPT_R3_TYPE,   /*!< Type (FCELL or DCELL) of a new created raster3d map */
    G_OPT_R3_PRECISION, /*!< The precision of the new generated raster3d map */
    G_OPT_R3_TILE_DIMENSION, /*!< The tile dimension of a new generated raster3d
                                map */
    G_OPT_R3_COMPRESSION, /*!< The kind of compression of a new created raster3d
                             map */

    G_OPT_V_INPUT,     /*!< old input vector map */
    G_OPT_V_INPUTS,    /*!< old input vector maps */
    G_OPT_V_OUTPUT,    /*!< new output vector map */
    G_OPT_V_MAP,       /*!< old input vector map */
    G_OPT_V_MAPS,      /*!< old input vector maps */
    G_OPT_V_TYPE,      /*!< primitive type */
    G_OPT_V3_TYPE,     /*!< primitive type, 2D and 3D */
    G_OPT_V_FIELD,     /*!< layer number (layers used to be called fields) */
    G_OPT_V_FIELD_ALL, /*!< layer number (layers used to be called fields) */
    G_OPT_V_CAT,       /*!< one category */
    G_OPT_V_CATS,      /*!< more categories */
    G_OPT_V_ID,        /*!< one feature id */
    G_OPT_V_IDS,       /*!< more feature ids */

    G_OPT_F_INPUT,     /*!< old input file */
    G_OPT_F_BIN_INPUT, /*!< old binary input file */
    G_OPT_F_OUTPUT,    /*!< new output file */
    G_OPT_F_SEP,       /*!< data field separator */

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 94b7310cb1 (r.colors.out: Add JSON support (#4555))
    G_OPT_C,        /*!< color */
    G_OPT_CN,       /*!< color or none */
    G_OPT_C_FORMAT, /*!< set color format to rgb,hex,hsv or triplet */

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 68e94e2177 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5045211539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2873114db3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1cc6936fc1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
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
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
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
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
    G_OPT_C,  /*!< color */
    G_OPT_CN, /*!< color or none */
=======
    G_OPT_C,        /*!< color */
    G_OPT_CN,       /*!< color or none */
    G_OPT_C_FORMAT, /*!< set color format to rgb,hex,hsv or triplet */
>>>>>>> 6bac3385ba (r.colors.out: Add JSON support (#4555))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
    G_OPT_C,  /*!< color */
    G_OPT_CN, /*!< color or none */
=======
    G_OPT_C,        /*!< color */
    G_OPT_CN,       /*!< color or none */
    G_OPT_C_FORMAT, /*!< set color format to rgb,hex,hsv or triplet */
>>>>>>> 6bac3385ba (r.colors.out: Add JSON support (#4555))

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ca117bbc2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
    G_OPT_C,  /*!< color */
    G_OPT_CN, /*!< color or none */

>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e4d094b27b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d31cefad27 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e7c536a439 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> db1cab9e66 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e70fb84cab (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 81dde7e207 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6ad2b2c24d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68e94e2177 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5045211539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
    G_OPT_C,  /*!< color */
    G_OPT_CN, /*!< color or none */

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 3ca117bbc2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1cc6936fc1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 2873114db3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
    G_OPT_M_UNITS,      /*!< units */
    G_OPT_M_DATATYPE,   /*!< datatype */
    G_OPT_M_MAPSET,     /*!< mapset */
    G_OPT_M_LOCATION,   /*!< location */
    G_OPT_M_DBASE,      /*!< dbase */
    G_OPT_M_COORDS,     /*!< coordinates */
    G_OPT_M_COLR,       /*!< color rules */
    G_OPT_M_DIR,        /*!< directory input */
    G_OPT_M_REGION,     /*!< saved region */
    G_OPT_M_NULL_VALUE, /*!< null value string */
    G_OPT_M_NPROCS,     /*!< number of threads for parallel computing */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
>>>>>>> main
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
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e4d094b27b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d31cefad27 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e7c536a439 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> db1cab9e66 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e70fb84cab (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 81dde7e207 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6ad2b2c24d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68e94e2177 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 5045211539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 3ca117bbc2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1cc6936fc1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 2873114db3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
    G_OPT_M_UNITS,              /*!< units */
    G_OPT_M_DATATYPE,           /*!< datatype */
    G_OPT_M_MAPSET,             /*!< mapset */
    G_OPT_M_LOCATION,           /*!< location */
    G_OPT_M_DBASE,              /*!< dbase */
    G_OPT_M_COORDS,             /*!< coordinates */
    G_OPT_M_COLR,               /*!< color rules */
    G_OPT_M_DIR,                /*!< directory input */
    G_OPT_M_REGION,             /*!< saved region */
    G_OPT_M_NULL_VALUE,         /*!< null value string */
    G_OPT_M_NPROCS,             /*!< number of threads for parallel computing */

    G_OPT_STDS_INPUT,           /*!< old input space time dataset of type strds, str3ds or stvds */
    G_OPT_STDS_INPUTS,          /*!< old input space time datasets */
    G_OPT_STDS_OUTPUT,          /*!< new output space time dataset */
    G_OPT_STRDS_INPUT,          /*!< old input space time raster dataset */
    G_OPT_STRDS_INPUTS,         /*!< old input space time raster datasets */
    G_OPT_STRDS_OUTPUT,         /*!< new output space time raster dataset */
    G_OPT_STRDS_OUTPUTS,        /*!< new output space time raster datasets */
    G_OPT_STR3DS_INPUT,         /*!< old input space time raster3d dataset */
    G_OPT_STR3DS_INPUTS,        /*!< old input space time raster3d datasets */
    G_OPT_STR3DS_OUTPUT,        /*!< new output space time raster3d dataset */
    G_OPT_STVDS_INPUT,          /*!< old input space time vector dataset */
    G_OPT_STVDS_INPUTS,         /*!< old input space time vector datasets */
    G_OPT_STVDS_OUTPUT,         /*!< new output space time vector dataset */
    G_OPT_MAP_INPUT,            /*!< old input map of type raster, vector or raster3d  */
    G_OPT_MAP_INPUTS,           /*!< old input maps of type raster, vector or raster3d  */
    G_OPT_STDS_TYPE,            /*!< the type of a space time dataset: strds, str3ds, stvds */
    G_OPT_MAP_TYPE,             /*!< The type of an input map: raster, vect, rast3d */
    G_OPT_T_TYPE,               /*!< The temporal type of a space time dataset */
    G_OPT_T_WHERE,              /*!< A temporal GIS framework SQL WHERE statement */
    G_OPT_T_SAMPLE             /*!< Temporal sample methods */
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e4d094b27b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d31cefad27 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e7c536a439 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> db1cab9e66 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e70fb84cab (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 81dde7e207 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 68e94e2177 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5045211539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1cc6936fc1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2873114db3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 6ad2b2c24d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 3ca117bbc2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
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
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
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
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 19e9e21aa9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 9ac1c737f3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6c98972382 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cd06e6628a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
=======
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
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 43085d2b40 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 0fd325371d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7582fc9ff1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1b0c82c3cd (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a15f8edf63 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 42702596af (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> e4d094b27b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d31cefad27 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e7c536a439 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> db1cab9e66 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e70fb84cab (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 81dde7e207 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> osgeo-main
=======
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 6ad2b2c24d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68e94e2177 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5045211539 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 9d728eab21 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> e71c665a53 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 047446473b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 98bb69619b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0943599d80 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c7f7308f2f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 199a7978ba (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f340fd22c3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 3016f28936 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4f3a440e32 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fc8552968d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> aeb2a68635 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> cbe16d2194 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b95da67055 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 20c4fef446 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f114e7aa14 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 3ca117bbc2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> d9ea5124d9 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 9164d685c2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 876d0d5a74 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 70f3ad40b7 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 218ccb912d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ef8e26d203 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> b96783bb3a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9022f5ed1b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bd2fc8fa00 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> e132de72b6 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> d3de2fb8f0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> de2caeece8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 886d93287a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a1d06de3e1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 04a31aa925 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8af479a35 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 84913af40a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7cac712ee3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> d178e98fad (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 329e8f795b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c3e2c0c6ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c8caa43d13 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 01b1dd1389 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> c36046c283 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8ac3ae1058 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3b3deffab9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> fe0d3e76e8 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 86898e3f4d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b41fbbe432 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a38f06ab3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 180e64978a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 322172822f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 831293fa24 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 514acfc57d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 094662d8cb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 48b1950515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ebc3e326d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7c4bca54be (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> ed316538a9 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 915e5ac55d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4a5c436a7f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d78873d16e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 70c1720eae (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57b656d91d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f342172848 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6dc9b532d4 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 1cc6936fc1 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b1d91344aa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7bd5a01c1d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> edc668941a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 2873114db3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> a5a2fa0841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d3f362186e (wxpyimgview: explicit conversion to int (#2704))

    G_OPT_STDS_INPUT, /*!< old input space time dataset of type strds, str3ds or
                         stvds */
    G_OPT_STDS_INPUTS,   /*!< old input space time datasets */
    G_OPT_STDS_OUTPUT,   /*!< new output space time dataset */
    G_OPT_STRDS_INPUT,   /*!< old input space time raster dataset */
    G_OPT_STRDS_INPUTS,  /*!< old input space time raster datasets */
    G_OPT_STRDS_OUTPUT,  /*!< new output space time raster dataset */
    G_OPT_STRDS_OUTPUTS, /*!< new output space time raster datasets */
    G_OPT_STR3DS_INPUT,  /*!< old input space time raster3d dataset */
    G_OPT_STR3DS_INPUTS, /*!< old input space time raster3d datasets */
    G_OPT_STR3DS_OUTPUT, /*!< new output space time raster3d dataset */
    G_OPT_STVDS_INPUT,   /*!< old input space time vector dataset */
    G_OPT_STVDS_INPUTS,  /*!< old input space time vector datasets */
    G_OPT_STVDS_OUTPUT,  /*!< new output space time vector dataset */
    G_OPT_MAP_INPUT,  /*!< old input map of type raster, vector or raster3d  */
    G_OPT_MAP_INPUTS, /*!< old input maps of type raster, vector or raster3d  */
    G_OPT_STDS_TYPE, /*!< the type of a space time dataset: strds, str3ds, stvds
                      */
    G_OPT_MAP_TYPE,  /*!< The type of an input map: raster, vect, rast3d */
    G_OPT_T_TYPE,    /*!< The temporal type of a space time dataset */
    G_OPT_T_WHERE,   /*!< A temporal GIS framework SQL WHERE statement */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    G_OPT_T_SAMPLE,  /*!< Temporal sample methods */

    G_OPT_F_FORMAT, /*!< set output format to plain text or JSON */
=======
    G_OPT_T_SAMPLE   /*!< Temporal sample methods */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
    G_OPT_T_SAMPLE   /*!< Temporal sample methods */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
    G_OPT_T_SAMPLE   /*!< Temporal sample methods */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
} STD_OPT;

/*!
   \typedef STD_FLG
   \brief  Standard flag identifiers (enum)

   Identifies of all recognized standard flags.

   Used by the G_parser() system.
 */

/**/ typedef enum {
    G_FLG_UNDEFINED,
    G_FLG_V_TABLE, /*!< do not create attribute table */
    G_FLG_V_TOPO   /*!< do not build topology */
} STD_FLG;

/* Parser rules for G__option_rule() */
enum rule_type {
    RULE_EXCLUSIVE,
    RULE_REQUIRED,
    RULE_REQUIRES,
    RULE_REQUIRES_ALL,
    RULE_EXCLUDES,
    RULE_COLLECTIVE
};

/* Message format */
#define G_INFO_FORMAT_STANDARD \
    0 /* GRASS_MESSAGE_FORMAT=standard or not defined */
#define G_INFO_FORMAT_GUI    1 /* GRASS_MESSAGE_FORMAT=gui */
#define G_INFO_FORMAT_SILENT 2 /* GRASS_MESSAGE_FORMAT=silent */
#define G_INFO_FORMAT_PLAIN  3 /* GRASS_MESSAGE_FORMAT=plain */

/* Icon types */
#define G_ICON_CROSS         0
#define G_ICON_BOX           1
#define G_ICON_ARROW         2

/* default colors */
#define DEFAULT_FG_COLOR     "black"
#define DEFAULT_BG_COLOR     "white"
#define DEFAULT_COLOR_TABLE  "viridis"

/* error codes */
#define G_FATAL_EXIT         0
#define G_FATAL_PRINT        1
#define G_FATAL_RETURN       2

/*! \brief Endian check */
#define ENDIAN_LITTLE        0
#define ENDIAN_BIG           1
#define ENDIAN_OTHER         2

/* for vector maps */
/*!
   \brief Name of default key column
 */
#define GV_KEY_COLUMN        "cat"

/*!
   \brief Element types identifiers (enum)

   Identifies various element types. Element can be raster map,
   vector map, etc.
 */
enum {                            /* Dir */
       G_ELEMENT_RASTER = 1,      /*!< raster */
       G_ELEMENT_RASTER3D = 2,    /*!< 3d raster */
       G_ELEMENT_VECTOR = 3,      /*!< vector */
       G_ELEMENT_ASCIIVECTOR = 4, /*!< ASCII vector */
       G_ELEMENT_LABEL = 5,       /*!< labels */
       G_ELEMENT_REGION = 6,      /*!< region */
       G_ELEMENT_GROUP = 7        /*!< group */
};

/*=========================== Typedefs/Structures ==========================*/

/*!
   \brief 2D/3D raster map header (used also for region)
 */
struct Cell_head {
    /*! \brief Max number of bytes per raster data value minus 1 (raster header
       only)

       Note: -1 for FP raster maps
     */
    int format;
    /*! \brief Compression mode (raster header only)

       - 0: uncompressed
       - 1: compressed
       - -1: pre GRASS 3.0
     */
    int compressed;
    /*! \brief Number of rows for 2D data */
    int rows;
    /*! \brief Number of rows for 3D data */
    int rows3;
    /*! \brief Number of columns for 2D data */
    int cols;
    /*! \brief Number of columns for 3D data */
    int cols3;
    /*! \brief number of depths for 3D data */
    int depths;
    /*! \brief Projection code

       - PROJECTION_XY
       - PROJECTION_UTM
       - PROJECTION_SP
       - PROJECTION_LL
       - PROJECTION_OTHER
     */
    int proj;
    /*! \brief Projection zone (UTM) */
    int zone;
    /*! \brief Resolution - east to west cell size for 2D data */
    double ew_res;
    /*! \brief Resolution - east to west cell size for 3D data */
    double ew_res3;
    /*! \brief Resolution - north to south cell size for 2D data */
    double ns_res;
    /*! \brief Resolution - north to south cell size for 3D data */
    double ns_res3;
    /*! \brief Resolution - top to bottom cell size for 3D data */
    double tb_res;
    /*! \brief Extent coordinates (north) */
    double north;
    /*! \brief Extent coordinates (south) */
    double south;
    /*! \brief Extent coordinates (east) */
    double east;
    /*! \brief Extent coordinates (west) */
    double west;
    /*! \brief Extent coordinates (top) - 3D data */
    double top;
    /*! \brief Extent coordinates (bottom) - 3D data */
    double bottom;
};

/*
 ** Structure for I/O of 3dview files  (view.c)
 */
struct G_3dview {
    char pgm_id[40];     /* user-provided identifier */
    float from_to[2][3]; /* eye position & lookat position */
    float fov;           /* field of view */
    float twist;         /* right_hand rotation about from_to */
    float exag;          /* terrain elevation exageration */
    int mesh_freq;       /* cells per grid line */
    int poly_freq;       /* cells per polygon */
    int display_type;    /* 1 for mesh, 2 for poly, 3 for both */
    int lightson;        /* boolean */
    int dozero;          /* boolean */
    int colorgrid;       /* boolean */
    int shading;         /* boolean */
    int fringe;          /* boolean */
    int surfonly;        /* boolean */
    int doavg;           /* boolean */
    char grid_col[40];   /* colors */
    char bg_col[40];     /* colors */
    char other_col[40];  /* colors */
    float lightpos[4];   /* east, north, height, 1.0 for local 0.0 infin */
    float lightcol[3];   /* values between 0.0 to 1.0 for red, grn, blu */
    float ambient;
    float shine;
    struct Cell_head vwin;
};

struct Key_Value {
    int nitems;
    int nalloc;
    char **key;
    char **value;
};

/*!
   \brief Structure that stores option information

   The descriptions member contains pairs of option and option
   descriptions separated by semicolon ';'.
   For example, when options member is set using:
   \code
   opt->options = "break,rmdupl"
   \endcode
   the descriptions member should be set to:
   \verbatim
   "break;break lines on intersections;"
   "rmdupl;remove duplicates"
   \endverbatim

   Parsed descriptions are stored in the same order as options.

   GUI dependency is a list of options (separated by commas) to be updated
   if the value is changed.

   Used by the G_parser() system.
 */
struct Option {
    const char *key;     /*!< Key word used on command line */
    int type;            /*!< Option type */
    int required;        /*!< REQUIRED or OPTIONAL */
    int multiple;        /*!< Multiple entries OK */
    const char *options; /*!< Approved values or range or NULL */
    const char **opts;   /*!< NULL or NULL terminated array of parsed options */
    const char *key_desc; /*!< one word describing the key */
    const char *label; /*!< Optional short label, used in GUI as item label */
    const char *description;  /*!< String describing option */
    const char *descriptions; /*!< ';' separated pairs of option and option
                                 descriptions */
    const char **descs;       /*!< parsed descriptions, array of
                               either NULL or string */
    char *answer;             /*!< Option answer */
    const char *def;          /*!< Where original answer gets saved */
    char **answers;           /*!< Option answers (for multiple=YES) */
    struct Option *next_opt;  /*!< Pointer to next option struct */
    const char *gisprompt;    /*!< Interactive prompt guidance */
    const char *guisection; /*!< GUI Layout guidance: ';' delimited hierarchical
                               tree position */
    const char *guidependency;    /*!< GUI dependency */
    int (*checker)(const char *); /*!< Routine to check answer or NULL  */
    int count;
};

/*!
   \brief Structure that stores flag info

   Used by the G_parser() system.
 */
struct Flag {
    char key;                /*!< Key char used on command line */
    char answer;             /*!< Stores flag state: 0/1 */
    char suppress_required;  /*!< Suppresses checking of required options */
    char suppress_overwrite; /*!< Suppresses checking of existing output */
    const char *label; /*!< Optional short label, used in GUI as item label */
    const char *description; /*!< String describing flag meaning   */
    const char *guisection; /*!< GUI Layout guidance: ';' delimited hierarchical
                               tree position */
    struct Flag *next_flag; /*!< Pointer to next flag struct */
};

/*!
   \brief Structure that stores module info

   Used by the G_parser() system.
 */
struct GModule {
    const char *label;       /*!< Optional short description for GUI */
    const char *description; /*!< String describing module */
    const char **keywords;   /*!< Keywords describing module */
    /* further items are possible: author(s), version, year */
    int overwrite; /*!< overwrite old files */
    int verbose;   /*!< print all information about progress and so on */
};

struct TimeStamp {
    DateTime dt[2]; /* two datetimes */
    int count;
};

struct Counter {
    int value;
};

struct Popen {
    FILE *fp;
    int pid;
};

typedef int CELL;
typedef double DCELL;
typedef float FCELL;

/* 64 bit signed integer */
#if HAVE_INT64_T
#include <sys/types.h>
typedef int64_t grass_int64;
#elif defined(__MINGW32__)
typedef __int64 grass_int64;
#elif HAVE_LONG_LONG_INT
typedef long long int grass_int64;
#elif HAVE_LARGEFILES
typedef off_t grass_int64;
#else
#error "no 64 bit integer available"
#endif

/* LCELL = large CELL, proposed new raster data type */
typedef grass_int64 LCELL;

struct _Color_Value_ {
    DCELL value;
    unsigned char red;
    unsigned char grn;
    unsigned char blu;
};

struct _Color_Rule_ {
    struct _Color_Value_ low, high;
    struct _Color_Rule_ *next;
    struct _Color_Rule_ *prev;
};

struct _Color_Info_ {
    struct _Color_Rule_ *rules;
    int n_rules;

    struct {
        unsigned char *red;
        unsigned char *grn;
        unsigned char *blu;
        unsigned char *set;
        int nalloc;
        int active;
    } lookup;

    struct {
        DCELL *vals;
        /* pointers to color rules corresponding to the intervals btwn vals */
        struct _Color_Rule_ **rules;
        int nalloc;
        int active;
    } fp_lookup;

    DCELL min, max;
};

struct Colors {
    int version; /* set by read_colors: -1=old,1=new */
    DCELL shift;
    int invert;
    int is_float; /* defined on floating point raster data? */
    int null_set; /* the colors for null are set? */
    unsigned char null_red;
    unsigned char null_grn;
    unsigned char null_blu;
    int undef_set; /* the colors for cells not in range are set? */
    unsigned char undef_red;
    unsigned char undef_grn;
    unsigned char undef_blu;
    struct _Color_Info_ fixed;
    struct _Color_Info_ modular;
    DCELL cmin;
    DCELL cmax;
    int organizing;
};

/*!
   \brief List of integers
 */
struct ilist {
    /*!
       \brief Array of values
     */
    int *value;
    /*!
       \brief Number of values in the list
     */
    int n_values;
    /*!
       \brief Allocated space for values
     */
    int alloc_values;
};

/*============================== Prototypes ================================*/

/* Since there are so many prototypes for the gis library they are stored */
/* in the file gisdefs.h */
#include <grass/defs/gis.h>

#endif /* GRASS_GIS_H */
