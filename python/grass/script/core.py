"""
Core functions to be used in Python scripts.

Usage:

::

    from grass.script import core as grass
    grass.parser()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
(C) 2008-2023 by the GRASS Development Team
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
(C) 2008-2023 by the GRASS Development Team
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
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
(C) 2008-2024 by the GRASS Development Team
=======
(C) 2008-2021 by the GRASS Development Team
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
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
(C) 2008-2022 by the GRASS Development Team
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
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
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
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
(C) 2008-2023 by the GRASS Development Team
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
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
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
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
(C) 2008-2022 by the GRASS Development Team
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
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
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
=======
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
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
=======
(C) 2008-2021 by the GRASS Development Team
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
(C) 2008-2022 by the GRASS Development Team
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
(C) 2008-2023 by the GRASS Development Team
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
(C) 2008-2021 by the GRASS Development Team
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
(C) 2008-2022 by the GRASS Development Team
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
(C) 2008-2023 by the GRASS Development Team
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
(C) 2008-2021 by the GRASS Development Team
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
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2008-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
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
(C) 2008-2021 by the GRASS Development Team
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
(C) 2008-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
(C) 2008-2023 by the GRASS Development Team
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
(C) 2008-2023 by the GRASS Development Team
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
(C) 2008-2021 by the GRASS Development Team
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
(C) 2008-2022 by the GRASS Development Team
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
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9b17b70e23 (r.terrafow: explicit use of default constructors (#2660))
This program is free software under the GNU General Public
License (>=v2). Read the file COPYING that comes with GRASS
for details.

.. sectionauthor:: Glynn Clements
.. sectionauthor:: Martin Landa <landa.martin gmail.com>
.. sectionauthor:: Michael Barton <michael.barton asu.edu>
"""

from __future__ import annotations

import os
import sys
import atexit
import subprocess
import shutil
import codecs
import string
import random
import shlex
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
import json
import csv
import io
>>>>>>> osgeo-main
=======
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
import json
import csv
import io
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
from tempfile import NamedTemporaryFile
from pathlib import Path

from .utils import KeyValue, parse_key_val, basename, encode, decode, try_remove
from grass.exceptions import ScriptError, CalledModuleError
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
from grass.grassdb.manage import resolve_mapset_path
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
from grass.grassdb.manage import resolve_mapset_path
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
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
from grass.grassdb.manage import resolve_mapset_path
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
from grass.grassdb.manage import resolve_mapset_path
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
from grass.grassdb.manage import resolve_mapset_path
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
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
from grass.grassdb.manage import resolve_mapset_path
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
from grass.grassdb.manage import resolve_mapset_path
=======
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
from grass.grassdb.manage import resolve_mapset_path
=======
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
from grass.grassdb.manage import resolve_mapset_path
=======
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
from grass.grassdb.manage import resolve_mapset_path
=======
<<<<<<< HEAD
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
from grass.grassdb.manage import resolve_mapset_path
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))


# subprocess wrapper that uses shell on Windows
class Popen(subprocess.Popen):
    _builtin_exts = {".com", ".exe", ".bat", ".cmd"}

    @staticmethod
    def _escape_for_shell(arg):
        # TODO: what are cmd.exe's parsing rules?
        return arg

    def __init__(self, args, **kwargs):
        if (
            sys.platform == "win32"
            and isinstance(args, list)
            and not kwargs.get("shell", False)
            and kwargs.get("executable") is None
        ):
            cmd = shutil.which(args[0])
            if cmd is None:
                raise OSError(_("Cannot find the executable {0}").format(args[0]))
            args = [cmd] + args[1:]
            name, ext = os.path.splitext(cmd)
            if ext.lower() not in self._builtin_exts:
                kwargs["shell"] = True
                args = [self._escape_for_shell(arg) for arg in args]

            # hides the window on MS Windows - another window will be activated
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            si.wShowWindow = subprocess.SW_HIDE
            kwargs["startupinfo"] = si

        subprocess.Popen.__init__(self, args, **kwargs)


PIPE = subprocess.PIPE
STDOUT = subprocess.STDOUT


raise_on_error = False  # raise exception instead of calling fatal()
_capture_stderr = False  # capture stderr of subprocesses if possible


def call(*args, **kwargs):
    return Popen(*args, **kwargs).wait()


# GRASS-oriented interface to subprocess module

_popen_args = [
    "bufsize",
    "executable",
    "stdin",
    "stdout",
    "stderr",
    "preexec_fn",
    "close_fds",
    "cwd",
    "env",
    "universal_newlines",
    "startupinfo",
    "creationflags",
    "encoding",
]


def _make_val(val):
    """Convert value to a unicode string"""
    if isinstance(val, (bytes, str)):
        return decode(val)
    if isinstance(val, (int, float)):
        return str(val)
    try:
        return ",".join(map(_make_val, iter(val)))
    except TypeError:
        pass
    return str(val)


def _make_unicode(val, enc):
    """Convert value to unicode with given encoding

    :param val: value to be converted
    :param enc: encoding to be used
    """
    if val is None or enc is None:
        return val

    if enc == "default":
        return decode(val)
    return decode(val, encoding=enc)


def get_commands(*, env=None):
    """Create list of available GRASS commands to use when parsing
    string from the command line

    :return: list of commands (set) and directory of scripts (collected
             by extension - MS Windows only)

    >>> cmds = list(get_commands()[0])
    >>> cmds.sort()
    >>> cmds[:5]
    ['d.barscale', 'd.colorlist', 'd.colortable', 'd.correlate', 'd.erase']

    """
    if not env:
        env = os.environ
    gisbase = env.get("GISBASE")

    # Lazy-importing to avoid circular dependencies.
    # pylint: disable=import-outside-toplevel
    if not gisbase:
        from grass.script.setup import get_install_path

        gisbase = get_install_path()

    cmd = []
    scripts = {".py": []} if sys.platform == "win32" else {}

    def scan(gisbase, directory):
        dir_path = os.path.join(gisbase, directory)
        if os.path.exists(dir_path):
            for fname in os.listdir(os.path.join(gisbase, directory)):
                if scripts:  # win32
                    name, ext = os.path.splitext(fname)
                    if ext != ".manifest":
                        cmd.append(name)
                    if ext in scripts.keys():
                        scripts[ext].append(name)
                else:
                    cmd.append(fname)

    for directory in ("bin", "scripts"):
        scan(gisbase, directory)

    # scan gui/scripts/
    gui_path = os.path.join(gisbase, "etc", "gui", "scripts")
    if os.path.exists(gui_path):
        os.environ["PATH"] = os.getenv("PATH") + os.pathsep + gui_path
        cmd += os.listdir(gui_path)

    return set(cmd), scripts


# Added because of scripts calling scripts on MS Windows.
# Module name (here cmd) differs from the file name (does not have extension).
# Additionally, we don't run scripts using system executable mechanism,
# so we need the full path name.
# However, scripts are on the PATH and '.PY' in in PATHEXT, so we can use
# shutil.which to get the full file path. Addons are on PATH too.
# An alternative to which function call would be to check the script path and
# addons path. This is proposed improvement for the future.
# Another alternative is to check some global list of scripts but this list
# needs to be created first. The question is what is less expensive.
# Note that getting the full path is only part of the solution,
# the other part is to use the right Python as an executable and pass the full
# script path as a parameter.
# Nevertheless, it is unclear on which places which extensions are added.
# This function also could skip the check for platform but depends
# how will be used, this is most general but not most effective.
def get_real_command(cmd):
    """Returns the real file command for a module (cmd)

    For Python scripts on MS Windows it returns full path to the script
    and adds a '.py' extension.
    For other cases it just returns a module (name).
    So, you can just use this function for all without further check.

    >>> get_real_command('g.region')
    'g.region'

    :param cmd: the command
    """
    if sys.platform == "win32":
        # we in fact expect pure module name (without extension)
        # so, lets remove extension
        if os.path.splitext(cmd)[1] == ".py":
            cmd = cmd[:-3]
        # PATHEXT is necessary to check on Windows (force lowercase)
        pathext = [x.lower() for x in os.environ["PATHEXT"].split(os.pathsep)]
        if ".py" not in pathext:
            # we assume that PATHEXT contains always '.py'
            os.environ["PATHEXT"] = ".py;" + os.environ["PATHEXT"]
        full_path = shutil.which(cmd + ".py")
        if full_path:
            return full_path

    return cmd


def make_command(
    prog,
    flags="",
    overwrite=False,
    quiet=False,
    verbose=False,
    superquiet=False,
    errors=None,
    **options,
):
    """Return a list of strings suitable for use as the args parameter to
    Popen() or call(). Example:


    >>> make_command("g.message", flags = 'w', message = 'this is a warning')
    ['g.message', '-w', 'message=this is a warning']


    :param str prog: GRASS module
    :param str flags: flags to be used (given as a string)
    :param bool overwrite: True to enable overwriting the output (<tt>--o</tt>)
    :param bool quiet: True to run quietly (<tt>--q</tt>)
    :param bool superquiet: True to run extra quietly (<tt>--qq</tt>)
    :param bool verbose: True to run verbosely (<tt>--v</tt>)
    :param options: module's parameters

    :return: list of arguments
    """
    args = [_make_val(prog)]
    if overwrite:
        args.append("--o")
    if quiet:
        args.append("--q")
    if verbose:
        args.append("--v")
    if superquiet:
        args.append("--qq")
    if flags:
        flags = _make_val(flags)
        if "-" in flags:
            raise ScriptError("'-' is not a valid flag")
        args.append("-" + flags)
    for opt, val in options.items():
        if opt in _popen_args:
            continue
        # convert string to bytes
        if val is not None:
            if opt.startswith("_"):
                opt = opt[1:]
                warning(
                    _(
                        "To run the module <%s> add underscore at the end"
                        " of the option <%s> to avoid conflict with Python"
                        " keywords. Underscore at the beginning is"
                        " deprecated in GRASS GIS 7.0 and has been removed"
                        " in version 7.1."
                    )
                    % (prog, opt)
                )
            elif opt.endswith("_"):
                opt = opt[:-1]
            args.append(opt + "=" + _make_val(val))
    return args


def handle_errors(returncode, result, args, kwargs):
    """Error handler for :func:`run_command()` and similar functions

    The functions which are using this function to handle errors,
    can be typically called with an *errors* parameter.
    This function can handle one of the following values: raise,
    fatal, status, exit, and ignore. The value raise is a default.

    If returncode is 0, *result* is returned, unless
    ``errors="status"`` is set.

    If *kwargs* dictionary contains key ``errors``, the value is used
    to determine the return value and the behavior on error.
    The value ``errors="raise"`` is a default in which case a
    ``CalledModuleError`` exception is raised.

    For ``errors="fatal"``, the function calls :func:`fatal()`
    which has its own rules on what happens next.

    For ``errors="status"``, the *returncode* will be returned.
    This is useful, e.g., for cases when the exception-based error
    handling mechanism is not desirable or the return code has some
    meaning not necessarily interpreted as an error by the caller.

    For ``errors="exit"``, ``sys.exit()`` is called with the
    *returncode*, so it behaves similarly to a Bash script with
    ``set -e``. No additional error message or exception is produced.
    This might be useful for a simple script where error message
    produced by the called module provides sufficient information about
    what happened to the end user.

    Finally, for ``errors="ignore"``, the value of *result* will be
    passed in any case regardless of the *returncode*.
    """

    def get_module_and_code(args, kwargs):
        """Get module name and formatted command"""
        # TODO: construction of the whole command is far from perfect
        args = make_command(*args, **kwargs)
        # Since we are in error handler, let's be extra cautious
        # about an empty command.
        module = args[0] if args else None
        code = " ".join(args)
        return module, code

    handler = kwargs.get("errors", "raise")
    if handler.lower() == "status":
        return returncode
    if returncode == 0:
        return result
    if handler.lower() == "ignore":
        return result
<<<<<<< HEAD
<<<<<<< HEAD
    if handler.lower() == "fatal":
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    elif handler.lower() == "fatal":
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        module, code = get_module_and_code(args, kwargs)
        fatal(
            _(
                "Module {module} ({code}) failed with"
                " non-zero return code {returncode}"
            ).format(module=module, code=code, returncode=returncode)
        )
    elif handler.lower() == "exit":
        sys.exit(returncode)
    else:
        module, code = get_module_and_code(args, kwargs)
        raise CalledModuleError(module=module, code=code, returncode=returncode)


def start_command(
    prog,
    flags="",
    overwrite=False,
    quiet=False,
    verbose=False,
    superquiet=False,
    **kwargs,
):
    """Returns a Popen object with the command created by make_command.
    Accepts any of the arguments which Popen() accepts apart from "args"
    and "shell".

    >>> p = start_command("g.gisenv", stdout=subprocess.PIPE)
    >>> print(p)  # doctest: +ELLIPSIS
    <...Popen object at 0x...>
    >>> print(p.communicate()[0])  # doctest: +SKIP
    GISDBASE='/opt/grass-data';
    LOCATION_NAME='spearfish60';
    MAPSET='glynn';
    GUI='text';
    MONITOR='x0';

    If the module parameter is the same as Python keyword, add
    underscore at the end of the parameter. For example, use
    ``lambda_=1.6`` instead of ``lambda=1.6``.

    :param str prog: GRASS module
    :param str flags: flags to be used (given as a string)
    :param bool overwrite: True to enable overwriting the output (<tt>--o</tt>)
    :param bool quiet: True to run quietly (<tt>--q</tt>)
    :param bool superquiet: True to run extra quietly (<tt>--qq</tt>)
    :param bool verbose: True to run verbosely (<tt>--v</tt>)
    :param kwargs: module's parameters

    :return: Popen object
    """
    options = {}
    popts = {}
    for opt, val in kwargs.items():
        if opt in _popen_args:
            popts[opt] = val
        else:
            options[opt] = val

    args = make_command(
        prog,
        flags=flags,
        overwrite=overwrite,
        quiet=quiet,
        superquiet=superquiet,
        verbose=verbose,
        **options,
    )

    if debug_level() > 0:
        sys.stderr.write(
            "D1/{}: {}.start_command(): {}\n".format(
                debug_level(), __name__, " ".join(args)
            )
        )
        sys.stderr.flush()
    return Popen(args, **popts)


def run_command(*args, **kwargs):
    """Execute a module synchronously

    This function passes all arguments to ``start_command()``,
    then waits for the process to complete. It is similar to
    ``subprocess.check_call()``, but with the :func:`make_command()`
    interface. By default, an exception is raised in case of a non-zero
    return code by default.

    >>> run_command('g.region', raster='elevation')

    See :func:`start_command()` for details about parameters and usage.

    The behavior on error can be changed using *errors* parameter
    which is passed to the :func:`handle_errors()` function.

    :param *args: unnamed arguments passed to :func:`start_command()`
    :param **kwargs: named arguments passed to :func:`start_command()`
    :param str errors: passed to :func:`handle_errors()`

    .. versionchanged:: 8.0
        Before 8.0, the function was returning 0 when no error occurred
        for backward compatibility with code which was checking that
        value. Now the function returns None, unless ``errors="status"``
        is specified.
    .. versionchanged:: 7.2
        In 7.0.0, this function was returning the error code. However,
        it was rarely checked especially outside of the core code.
        Additionally, :func:`read_command()` needed a mechanism to
        report errors as it was used more and more in context which
        required error handling, Thus, exceptions were introduced as a
        more expected default behavior for Python programmers. The
        change was backported to 7.0 series.

    :raises: ``CalledModuleError`` when module returns non-zero return code
    """
    encoding = "default"
    if "encoding" in kwargs:
        encoding = kwargs["encoding"]

    if _capture_stderr and "stderr" not in kwargs.keys():
        kwargs["stderr"] = PIPE
    ps = start_command(*args, **kwargs)
    if _capture_stderr:
        stdout, stderr = ps.communicate()
        if encoding is not None:
            stdout = _make_unicode(stdout, encoding)
            stderr = _make_unicode(stderr, encoding)
        returncode = ps.poll()
        if returncode and stderr:
            sys.stderr.write(stderr)
    else:
        returncode = ps.wait()
    return handle_errors(returncode, result=None, args=args, kwargs=kwargs)


def pipe_command(*args, **kwargs):
    """Passes all arguments to start_command(), but also adds
    "stdout = PIPE". Returns the Popen object.

    >>> p = pipe_command("g.gisenv")
    >>> print(p)  # doctest: +ELLIPSIS
    <....Popen object at 0x...>
    >>> print(p.communicate()[0])  # doctest: +SKIP
    GISDBASE='/opt/grass-data';
    LOCATION_NAME='spearfish60';
    MAPSET='glynn';
    GUI='text';
    MONITOR='x0';

    :param list args: list of unnamed arguments (see start_command() for details)
    :param list kwargs: list of named arguments (see start_command() for details)

    :return: Popen object
    """
    kwargs["stdout"] = PIPE
    return start_command(*args, **kwargs)


def feed_command(*args, **kwargs):
    """Passes all arguments to start_command(), but also adds
    "stdin = PIPE". Returns the Popen object.

    :param list args: list of unnamed arguments (see start_command() for details)
    :param list kwargs: list of named arguments (see start_command() for details)

    :return: Popen object
    """
    kwargs["stdin"] = PIPE
    return start_command(*args, **kwargs)


def read_command(*args, **kwargs):
    """Passes all arguments to pipe_command, then waits for the process to
    complete, returning its stdout (i.e. similar to shell `backticks`).

    The behavior on error can be changed using *errors* parameter
    which is passed to the :func:`handle_errors()` function.

    :param list args: list of unnamed arguments (see start_command() for details)
    :param list kwargs: list of named arguments (see start_command() for details)

    :return: stdout
    """
    encoding = "default"
    if "encoding" in kwargs:
        encoding = kwargs["encoding"]

    if _capture_stderr and "stderr" not in kwargs.keys():
        kwargs["stderr"] = PIPE
    process = pipe_command(*args, **kwargs)
    stdout, stderr = process.communicate()
    if encoding is not None:
        stdout = _make_unicode(stdout, encoding)
        stderr = _make_unicode(stderr, encoding)
    returncode = process.poll()
    if returncode and _capture_stderr and stderr:
        # Print only when we are capturing it and there was some output.
        # (User can request ignoring the subprocess stderr and then we get only None.)
        sys.stderr.write(stderr)
    return handle_errors(returncode, stdout, args, kwargs)


def parse_command(*args, **kwargs):
    """Passes all arguments to read_command, then parses the output
    by default with parse_key_val().

    If the command has parameter <em>format</em> and is called with
    <em>format=json</em>, the output will be parsed into a dictionary.
    Similarly, with <em>format=csv</em> the output will be parsed into
    a list of lists (CSV rows).

    ::

        parse_command("v.db.select", ..., format="json")

    Custom parsing function can be optionally given by <em>parse</em> parameter
    including its arguments, e.g.

    ::

        parse_command(..., parse=(gs.parse_key_val, {'sep': ':'}))

    Parameter <em>delimiter</em> is deprecated.

    :param args: list of unnamed arguments (see start_command() for details)
    :param kwargs: list of named arguments (see start_command() for details)

    :return: parsed module output
    """

    def parse_csv(result):
        return list(csv.DictReader(io.StringIO(result)))

    parse = None
    parse_args = {}
    if "parse" in kwargs:
        if isinstance(kwargs["parse"], tuple):
            parse = kwargs["parse"][0]
            parse_args = kwargs["parse"][1]
        del kwargs["parse"]
    elif kwargs.get("format") == "json":
        parse = json.loads
    elif kwargs.get("format") == "csv":
        parse = parse_csv

    if not parse:
        parse = parse_key_val  # use default fn
        if "delimiter" in kwargs:
            parse_args = {"sep": kwargs["delimiter"]}
            del kwargs["delimiter"]

    res = read_command(*args, **kwargs)

    return parse(res, **parse_args)


def write_command(*args, **kwargs):
    """Execute a module with standard input given by *stdin* parameter.

    Passes all arguments to ``feed_command()``, with the string specified
    by the *stdin* argument fed to the process' standard input.

    >>> write_command(
    ...    'v.in.ascii', input='-',
    ...    stdin='%s|%s' % (635818.8, 221342.4),
    ...    output='view_point')
    0

    See ``start_command()`` for details about parameters and usage.

    The behavior on error can be changed using *errors* parameter
    which is passed to the :func:`handle_errors()` function.

    :param *args: unnamed arguments passed to ``start_command()``
    :param **kwargs: named arguments passed to ``start_command()``

    :returns: 0 with default parameters for backward compatibility only

    :raises: ``CalledModuleError`` when module returns non-zero return code
    """
    encoding = "default"
    if "encoding" in kwargs:
        encoding = kwargs["encoding"]
    # TODO: should we delete it from kwargs?
    stdin = kwargs["stdin"]
    if encoding is None or encoding == "default":
        stdin = encode(stdin)
    else:
        stdin = encode(stdin, encoding=encoding)
    if _capture_stderr and "stderr" not in kwargs.keys():
        kwargs["stderr"] = PIPE
    process = feed_command(*args, **kwargs)
    unused, stderr = process.communicate(stdin)
    if encoding is not None:
        unused = _make_unicode(unused, encoding)
        stderr = _make_unicode(stderr, encoding)
    returncode = process.poll()
    if returncode and _capture_stderr and stderr:
        sys.stderr.write(stderr)
    return handle_errors(returncode, None, args, kwargs)


def exec_command(
    prog,
    flags="",
    overwrite=False,
    quiet=False,
    verbose=False,
    superquiet=False,
    env=None,
    **kwargs,
):
    """Interface to os.execvpe(), but with the make_command() interface.

    :param str prog: GRASS module
    :param str flags: flags to be used (given as a string)
    :param bool overwrite: True to enable overwriting the output (<tt>--o</tt>)
    :param bool quiet: True to run quietly (<tt>--q</tt>)
    :param bool superquiet: True to run quietly (<tt>--qq</tt>)
    :param bool verbose: True to run verbosely (<tt>--v</tt>)
    :param env: dictionary with system environment variables (`os.environ` by default)
    :param list kwargs: module's parameters

    """
    args = make_command(prog, flags, overwrite, quiet, superquiet, verbose, **kwargs)

    if env is None:
        env = os.environ
    os.execvpe(prog, args, env)


# interface to g.message


def message(msg, flag=None, env=None):
    """Display a message using `g.message`

    :param str msg: message to be displayed
    :param str flag: flags (given as string)
    :param env: dictionary with system environment variables (`os.environ` by default)
    """
    run_command("g.message", flags=flag, message=msg, errors="ignore", env=env)


<<<<<<< HEAD
def debug(msg, debug=1, env=None):
=======
def debug(msg, debug=1):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
    """Display a debugging message using `g.message -d`.

    The visibility of a debug message at runtime is controlled by
    setting the corresponding DEBUG level with `g.gisenv set="DEBUG=X"`
    (with `X` set to the debug level specified in the function call).

    :param str msg: debugging message to be displayed
    :param str debug: debug level (0-5) with the following recommended levels:
        Use 1 for messages generated once of few times,
        3 for messages generated for each raster row or vector line,
        5 for messages generated for each raster cell or vector point.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
    :param env: dictionary with system environment variables (`os.environ` by default)
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    :param env: dictionary with system environment variables (`os.environ` by default)
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
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
    :param env: dictionary with system environment variables (`os.environ` by default)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    :param env: dictionary with system environment variables (`os.environ` by default)
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
    :param env: dictionary with system environment variables (`os.environ` by default)
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
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
    :param env: dictionary with system environment variables (`os.environ` by default)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
    :param env: dictionary with system environment variables (`os.environ` by default)
=======
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
    :param env: dictionary with system environment variables (`os.environ` by default)
=======
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
    :param env: dictionary with system environment variables (`os.environ` by default)
=======
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
    :param env: dictionary with system environment variables (`os.environ` by default)
=======
<<<<<<< HEAD
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
    :param env: dictionary with system environment variables (`os.environ` by default)
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
    """
    if debug_level() >= debug:
        # TODO: quite a random hack here, do we need it somewhere else too?
        if sys.platform == "win32":
            msg = msg.replace("&", "^&")

        run_command("g.message", flags="d", message=msg, debug=debug, env=env)


def verbose(msg, env=None):
    """Display a verbose message using `g.message -v`

    :param str msg: verbose message to be displayed
    :param env: dictionary with system environment variables (`os.environ` by default)
    """
    message(msg, flag="v", env=env)


def info(msg, env=None):
    """Display an informational message using `g.message -i`

    :param str msg: informational message to be displayed
    :param env: dictionary with system environment variables (`os.environ` by default)
    """
    message(msg, flag="i", env=env)


def percent(i, n, s, env=None):
    """Display a progress info message using `g.message -p`

    ::

        message(_("Percent complete..."))
        n = 100
        for i in range(n):
            percent(i, n, 1)
        percent(1, 1, 1)

    :param int i: current item
    :param int n: total number of items
    :param int s: increment size
    :param env: dictionary with system environment variables (`os.environ` by default)
    """
    message("%d %d %d" % (i, n, s), flag="p", env=env)


def warning(msg, env=None):
    """Display a warning message using `g.message -w`

    :param str msg: warning message to be displayed
    :param env: dictionary with system environment variables (`os.environ` by default)
    """
    message(msg, flag="w", env=env)


def error(msg, env=None):
    """Display an error message using `g.message -e`

    This function does not end the execution of the program.
    The right action after the error is up to the caller.
    For error handling using the standard mechanism use :func:`fatal()`.

    :param str msg: error message to be displayed
    :param env: dictionary with system environment variables (`os.environ` by default)
    """
    message(msg, flag="e", env=env)


def fatal(msg, env=None):
    """Display an error message using `g.message -e`, then abort or raise

    Raises exception when module global raise_on_error is 'True', abort
    (calls exit) otherwise.
    Use :func:`set_raise_on_error()` to set the behavior.

    :param str msg: error message to be displayed
    :param env: dictionary with system environment variables (`os.environ` by default)
    """
    global raise_on_error
    if raise_on_error:
        raise ScriptError(msg)

    error(msg, env=env)
    sys.exit(1)


def set_raise_on_error(raise_exp=True):
    """Define behaviour on fatal error (fatal() called)

    :param bool raise_exp: True to raise ScriptError instead of calling
                           sys.exit(1) in fatal()

    :return: current status
    """
    global raise_on_error
    tmp_raise = raise_on_error
    raise_on_error = raise_exp
    return tmp_raise


def get_raise_on_error():
    """Return True if a ScriptError exception is raised instead of calling
    sys.exit(1) in case a fatal error was invoked with fatal()
    """
    global raise_on_error
    return raise_on_error


# TODO: solve also warnings (not printed now)
def set_capture_stderr(capture=True):
    """Enable capturing standard error output of modules and print it.

    By default, standard error output (stderr) of child processes shows
    in the same place as output of the parent process. This may not
    always be the same place as ``sys.stderr`` is written.
    After calling this function, functions in the ``grass.script``
    package will capture the stderr of child processes and pass it
    to ``sys.stderr`` if there is an error.

    .. note::

        This is advantageous for interactive shells such as the one in GUI
        and interactive notebooks such as Jupyter Notebook.

    The capturing can be applied only in certain cases, for example
    in case of run_command() it is applied because run_command() nor
    its callers do not handle the streams, however feed_command()
    cannot do capturing because its callers handle the streams.

    The previous state is returned. Passing ``False`` disables the
    capturing.

    .. versionadded:: 7.4
    """
    global _capture_stderr
    tmp = _capture_stderr
    _capture_stderr = capture
    return tmp


def get_capture_stderr():
    """Return True if stderr is captured, False otherwise.

    See set_capture_stderr().
    """
    global _capture_stderr
    return _capture_stderr


# interface to g.parser


def _parse_opts(lines: list) -> tuple[dict[str, str], dict[str, bool]]:
    options: dict[str, str] = {}
    flags: dict[str, bool] = {}
    for line in lines:
        if not line:
            break
        try:
            var, val = line.split(b"=", 1)
        except ValueError:
            raise SyntaxError("invalid output from g.parser: {}".format(line))
        try:
            var = decode(var)
            val = decode(val)
        except UnicodeError as error:
            raise SyntaxError(
                "invalid output from g.parser ({error}): {line}".format(
                    error=error, line=line
                )
            )
        if var.startswith("flag_"):
            flags[var[5:]] = bool(int(val))
        elif var.startswith("opt_"):
            options[var[4:]] = val
        elif var in {"GRASS_OVERWRITE", "GRASS_VERBOSE"}:
            os.environ[var] = val
        else:
            raise SyntaxError(
                "unexpected output variable from g.parser: {}".format(line)
            )
    return (options, flags)


def parser() -> tuple[dict[str, str], dict[str, bool]]:
    """Interface to g.parser, intended to be run from the top-level, e.g.:

    ::

        if __name__ == "__main__":
            options, flags = grass.parser()
            main()

    Thereafter, the global variables "options" and "flags" will be
    dictionaries containing option/flag values, keyed by lower-case
    option/flag names. The values in "options" are strings, those in
    "flags" are Python booleans.

    Overview table of parser standard options:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
>>>>>>> osgeo-main
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
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
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
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
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8f8045592c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
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
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
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
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 9fa78e6a12 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
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
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
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
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
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
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
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
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
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
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
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
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
=======
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
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
    https://grass.osgeo.org/grass80/manuals/parser_standard_options.html
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
    https://grass.osgeo.org/grass-devel/manuals/parser_standard_options.html
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
    """
    if not os.getenv("GISBASE"):
        print("You must be in GRASS GIS to run this program.", file=sys.stderr)
        sys.exit(1)

    cmdline = [basename(sys.argv[0])]
    cmdline += [shlex.quote(a) for a in sys.argv[1:]]
    os.environ["CMDLINE"] = " ".join(cmdline)

    argv = sys.argv[:]
    name = argv[0]
    if not os.path.isabs(name):
        if os.sep in name or (os.altsep and os.altsep in name):
            argv[0] = os.path.abspath(name)
        else:
            argv[0] = os.path.join(sys.path[0], name)

    prog = "g.parser.exe" if sys.platform == "win32" else "g.parser"
    p = subprocess.Popen([prog, "-n"] + argv, stdout=subprocess.PIPE)
    s = p.communicate()[0]
    lines = s.split(b"\0")

    if not lines or lines[0] != b"@ARGS_PARSED@":
        stdout = os.fdopen(sys.stdout.fileno(), "wb")
        stdout.write(s)
        sys.exit(p.returncode)
    return _parse_opts(lines[1:])


# interface to g.tempfile


def tempfile(create=True, env=None):
    """Returns the name of a temporary file, created with g.tempfile.

    :param bool create: True to create a file
    :param env: environment

    :return: path to a tmp file
    """
    flags = ""
    if not create:
        flags += "d"

    return read_command("g.tempfile", flags=flags, pid=os.getpid(), env=env).strip()


def tempdir(env=None):
    """Returns the name of a temporary dir, created with g.tempfile."""
    tmp = tempfile(create=False, env=env)
    os.mkdir(tmp)

    return tmp


def tempname(length, lowercase=False):
    """Generate a GRASS and SQL compliant random name starting with tmp_
    followed by a random part of length "length"

    :param int length: length of the random part of the name to generate
    :param bool lowercase: use only lowercase characters to generate name
    :returns: String with a random name of length "length" starting with a letter
    :rtype: str

    :Example:

    >>> tempname(12)
    'tmp_MxMa1kAS13s9'

    .. seealso:: functions :func:`append_uuid()`, :func:`append_random()`
    """

    chars = string.ascii_lowercase + string.digits
    if not lowercase:
        chars += string.ascii_uppercase
    random_part = "".join(random.choice(chars) for _ in range(length))
    return "tmp_" + random_part


def _compare_projection(dic):
    """Check if projection has some possibility of duplicate names like
    Universal Transverse Mercator and Universe Transverse Mercator and
    unify them

    :param dic: The dictionary containing information about projection

    :return: The dictionary with the new values if needed

    """
    # the lookup variable is a list of list, each list contains all the
    # possible name for a projection system
    lookup = [["Universal Transverse Mercator", "Universe Transverse Mercator"]]
    for lo in lookup:
        for n in range(len(dic["name"])):
            if dic["name"][n] in lo:
                dic["name"][n] = lo[0]
    return dic


def _compare_units(dic):
    """Check if units has some possibility of duplicate names like
    meter and metre and unify them

    :param dic: The dictionary containing information about units

    :return: The dictionary with the new values if needed

    """
    # the lookup variable is a list of list, each list contains all the
    # possible name for a units
    lookup = [
        ["meter", "metre"],
        ["meters", "metres"],
        ["kilometer", "kilometre"],
        ["kilometers", "kilometres"],
    ]
    for item in lookup:
        for n in range(len(dic["unit"])):
            if dic["unit"][n].lower() in item:
                dic["unit"][n] = item[0]
        for n in range(len(dic["units"])):
            if dic["units"][n].lower() in item:
                dic["units"][n] = item[0]
    return dic


def _text_to_key_value_dict(
    filename, sep=":", val_sep=",", checkproj=False, checkunits=False
):
    """Convert a key-value text file, where entries are separated by newlines
    and the key and value are separated by `sep', into a key-value dictionary
    and discover/use the correct data types (float, int or string) for values.

    :param str filename: The name or name and path of the text file to convert
    :param str sep: The character that separates the keys and values, default
                    is ":"
    :param str val_sep: The character that separates the values of a single
                        key, default is ","
    :param bool checkproj: True if it has to check some information about
                           projection system
    :param bool checkproj: True if it has to check some information about units

    :return: The dictionary

    A text file with this content:
    ::

        a: Hello
        b: 1.0
        c: 1,2,3,4,5
        d : hello,8,0.1

    Will be represented as this dictionary:

    ::

        {'a': ['Hello'], 'c': [1, 2, 3, 4, 5], 'b': [1.0], 'd': ['hello', 8, 0.1]}

    """
    text = open(filename).readlines()
    kvdict = KeyValue()

    for line in text:
        if line.find(sep) >= 0:
            key, value = line.split(sep)
            key = key.strip()
            value = value.strip()
        else:
            # Jump over empty values
            continue
        values = value.split(val_sep)
        value_list = []

        for value in values:
            not_float = False
            not_int = False

            # Convert values into correct types
            # We first try integer then float
            try:
                value_converted = int(value)
            except ValueError:
                not_int = True
            if not_int:
                try:
                    value_converted = float(value)
                except ValueError:
                    not_float = True

            if not_int and not_float:
                value_converted = value.strip()

            value_list.append(value_converted)

        kvdict[key] = value_list
    if checkproj:
        kvdict = _compare_projection(kvdict)
    if checkunits:
        kvdict = _compare_units(kvdict)
    return kvdict


def compare_key_value_text_files(
    filename_a,
    filename_b,
    sep=":",
    val_sep=",",
    precision=0.000001,
    proj=False,
    units=False,
):
    """Compare two key-value text files

    This method will print a warning in case keys that are present in the first
    file are not present in the second one.
    The comparison method tries to convert the values into their native format
    (float, int or string) to allow correct comparison.

    An example key-value text file may have this content:

    ::

        a: Hello
        b: 1.0
        c: 1,2,3,4,5
        d : hello,8,0.1

    :param str filename_a: name of the first key-value text file
    :param str filenmae_b: name of the second key-value text file
    :param str sep: character that separates the keys and values, default is ":"
    :param str val_sep: character that separates the values of a single key,
                        default is ","
    :param double precision: precision with which the floating point values are compared
    :param bool proj: True if it has to check some information about projection system
    :param bool units: True if it has to check some information about units

    :return: True if full or almost identical, False if different
    """
    dict_a = _text_to_key_value_dict(filename_a, sep, checkproj=proj, checkunits=units)
    dict_b = _text_to_key_value_dict(filename_b, sep, checkproj=proj, checkunits=units)

    if sorted(dict_a.keys()) != sorted(dict_b.keys()):
        return False

    # We compare matching keys
    for key in dict_a.keys():
        # Floating point values must be handled separately
        if isinstance(dict_a[key], float) and isinstance(dict_b[key], float):
            if abs(dict_a[key] - dict_b[key]) > precision:
                return False
        elif isinstance(dict_a[key], float) or isinstance(dict_b[key], float):
            warning(
                _("Mixing value types. Will try to compare after integer conversion")
            )
            return int(dict_a[key]) == int(dict_b[key])
        elif key == "+towgs84":
            # We compare the sum of the entries
            if abs(sum(dict_a[key]) - sum(dict_b[key])) > precision:
                return False
        elif dict_a[key] != dict_b[key]:
            return False
    return True


# interface to g.gisenv


def gisenv(env=None):
    """Returns the output from running g.gisenv (with no arguments), as a
    dictionary. Example:

    >>> env = gisenv()
    >>> print(env['GISDBASE'])  # doctest: +SKIP
    /opt/grass-data

    :param env: dictionary with system environment variables (`os.environ` by default)
    :return: list of GRASS variables
    """
    s = read_command("g.gisenv", flags="n", env=env)
    return parse_key_val(s)


# interface to g.region


def locn_is_latlong(env=None) -> bool:
    """Tests if location is lat/long. Value is obtained
    by checking the "g.region -pu" projection code.

    :return: True for a lat/long region, False otherwise
    """
    s = read_command("g.region", flags="pu", env=env)
    kv = parse_key_val(s, ":")
    return kv["projection"].split(" ")[0] == "3"


def region(region3d=False, complete=False, env=None):
    """Returns the output from running "g.region -gu", as a
    dictionary. Example:

    :param bool region3d: True to get 3D region
    :param bool complete:
    :param env: dictionary with system environment variables (`os.environ` by default)

    >>> curent_region = region()
    >>> # obtain n, s, e and w values
    >>> [curent_region[key] for key in "nsew"]  # doctest: +ELLIPSIS
    [..., ..., ..., ...]
    >>> # obtain ns and ew resulutions
    >>> (curent_region['nsres'], curent_region['ewres'])  # doctest: +ELLIPSIS
    (..., ...)

    :return: dictionary of region values
    """
    flgs = "gu"
    if region3d:
        flgs += "3"
    if complete:
        flgs += "cep"

    s = read_command("g.region", flags=flgs, env=env)
    reg = parse_key_val(s, val_type=float)
    for k in [
        "projection",
        "zone",
        "rows",
        "cols",
        "cells",
        "rows3",
        "cols3",
        "cells3",
        "depths",
    ]:
        if k not in reg:
            continue
        reg[k] = int(reg[k])

    return reg


def region_env(region3d=False, flags=None, env=None, **kwargs):
    """Returns region settings as a string which can used as
    GRASS_REGION environmental variable.

    If no 'kwargs' are given then the current region is used. Note
    that this function doesn't modify the current region!

    See also :func:`use_temp_region()` for alternative method how to define
    temporary region used for raster-based computation.

    :param bool region3d: True to get 3D region
    :param string flags: for example 'a'
    :param env: dictionary with system environment variables (`os.environ` by default)
    :param kwargs: g.region's parameters like 'raster', 'vector' or 'region'

    ::

        os.environ['GRASS_REGION'] = grass.region_env(region='detail')
        grass.mapcalc('map=1', overwrite=True)
        os.environ.pop('GRASS_REGION')

    :return: string with region values
    :return: empty string on error
    """
    # read proj/zone from WIND file
    gis_env = gisenv(env)
    windfile = os.path.join(
        gis_env["GISDBASE"], gis_env["LOCATION_NAME"], gis_env["MAPSET"], "WIND"
    )
    with open(windfile) as fd:
        grass_region = ""
<<<<<<< HEAD
        for line in fd:
            key, value = (x.strip() for x in line.split(":", 1))
=======
        for line in fd.readlines():
            key, value = map(lambda x: x.strip(), line.split(":", 1))
>>>>>>> 75456afff2 (style: Fixes literal-membership (PLR6201) for other code (#3954))
            if kwargs and key not in {"proj", "zone"}:
                continue
            if (
                not kwargs
                and not region3d
                and key
                in {
                    "top",
                    "bottom",
                    "cols3",
                    "rows3",
                    "depths",
                    "e-w resol3",
                    "n-s resol3",
                    "t-b resol",
                }
            ):
                continue

            grass_region += "%s: %s;" % (key, value)

    if not kwargs:  # return current region
        return grass_region

    # read other values from `g.region -gu`
    flgs = "ug"
    if region3d:
        flgs += "3"
    if flags:
        flgs += flags

    s = read_command("g.region", flags=flgs, env=env, **kwargs)
    if not s:
        return ""
    reg = parse_key_val(s)

    kwdata = [
        ("north", "n"),
        ("south", "s"),
        ("east", "e"),
        ("west", "w"),
        ("cols", "cols"),
        ("rows", "rows"),
        ("e-w resol", "ewres"),
        ("n-s resol", "nsres"),
    ]
    if region3d:
        kwdata += [
            ("top", "t"),
            ("bottom", "b"),
            ("cols3", "cols3"),
            ("rows3", "rows3"),
            ("depths", "depths"),
            ("e-w resol3", "ewres3"),
            ("n-s resol3", "nsres3"),
            ("t-b resol", "tbres"),
        ]

    for wkey, rkey in kwdata:
        grass_region += "%s: %s;" % (wkey, reg[rkey])

    return grass_region


def use_temp_region():
    """Copies the current region to a temporary region with "g.region save=",
    then sets WIND_OVERRIDE to refer to that region. Installs an atexit
    handler to delete the temporary region upon termination.
    """
    name = "tmp.%s.%d" % (os.path.basename(sys.argv[0]), os.getpid())
    run_command("g.region", flags="u", save=name, overwrite=True)
    os.environ["WIND_OVERRIDE"] = name
    atexit.register(del_temp_region)


def del_temp_region():
    """Unsets WIND_OVERRIDE and removes any region named by it."""
    try:
        name = os.environ.pop("WIND_OVERRIDE")
        run_command("g.remove", flags="f", quiet=True, type="region", name=name)
    except (KeyError, CalledModuleError):
        # The function succeeds even when called more than once.
        pass


# interface to g.findfile


def find_file(name, element="cell", mapset=None, env=None):
    """Returns the output from running g.findfile as a
    dictionary.

    Elements in g.findfile refer to mapset directories. However, in
    parts of the code, different element terms like rast, raster, or rast3d
    are used. For convenience the function translates such element types
    to respective mapset elements. Current translations are:
    "rast": "cell",
    "raster": "cell",
    "rast3d": "grid3",
    "raster3d": "grid3",
    "raster_3d": "grid3",

    Example:

    >>> result = find_file('elevation', element='cell')
    >>> print(result['fullname'])
    elevation@PERMANENT
    >>> print(result['file'])  # doctest: +ELLIPSIS
    /.../PERMANENT/cell/elevation
    >>> result = find_file('elevation', element='raster')
    >>> print(result['fullname'])
    elevation@PERMANENT
    >>> print(result['file'])  # doctest: +ELLIPSIS
    /.../PERMANENT/cell/elevation


    :param str name: file name
    :param str element: element type (default 'cell')
    :param str mapset: mapset name (default all mapsets in search path)
    :param env: environment

    :return: parsed output of g.findfile
    """
    element_translation = {
        "rast": "cell",
        "raster": "cell",
        "rast3d": "grid3",
        "raster3d": "grid3",
        "raster_3d": "grid3",
    }

    if element in element_translation:
        element = element_translation[element]

    # g.findfile returns non-zero when file was not found
    # so we ignore return code and just focus on stdout
    process = start_command(
        "g.findfile",
        flags="n",
        element=element,
        file=name,
        mapset=mapset,
        stdout=PIPE,
        env=env,
    )
    stdout = process.communicate()[0]
    return parse_key_val(stdout)


# interface to g.list


def list_strings(type, pattern=None, mapset=None, exclude=None, flag="", env=None):
    """List of elements as strings.

    Returns the output from running g.list, as a list of qualified
    names.

    :param str type: element type (raster, vector, raster_3d, region, ...)
    :param str pattern: pattern string
    :param str mapset: mapset name (if not given use search path)
    :param str exclude: pattern string to exclude maps from the research
    :param str flag: pattern type: 'r' (basic regexp), 'e' (extended regexp),
                     or '' (glob pattern)
    :param env: environment

    :return: list of elements
    """
    if type == "cell":
        verbose(_('Element type should be "raster" and not "%s"') % type, env=env)

    result = []
    for line in read_command(
        "g.list",
        quiet=True,
        flags="m" + flag,
        type=type,
        pattern=pattern,
        exclude=exclude,
        mapset=mapset,
        env=env,
    ).splitlines():
        result.append(line.strip())

    return result


def list_pairs(type, pattern=None, mapset=None, exclude=None, flag="", env=None):
    """List of elements as pairs

    Returns the output from running g.list, as a list of
    (name, mapset) pairs

    :param str type: element type (raster, vector, raster_3d, region, ...)
    :param str pattern: pattern string
    :param str mapset: mapset name (if not given use search path)
    :param str exclude: pattern string to exclude maps from the research
    :param str flag: pattern type: 'r' (basic regexp), 'e' (extended regexp),
                     or '' (glob pattern)
    :param env: environment

    :return: list of elements
    """
    return [
        tuple(map.split("@", 1))
        for map in list_strings(type, pattern, mapset, exclude, flag, env)
    ]


def list_grouped(
    type, pattern=None, check_search_path=True, exclude=None, flag="", env=None
):
    """List of elements grouped by mapsets.

    Returns the output from running g.list, as a dictionary where the
    keys are mapset names and the values are lists of maps in that
    mapset. Example:

    >>> list_grouped('vect', pattern='*roads*')['PERMANENT']
    ['railroads', 'roadsmajor']

    :param str type: element type (raster, vector, raster_3d, region, ...)
                     or list of elements
    :param str pattern: pattern string
    :param str check_search_path: True to add mapsets for the search path
                                  with no found elements
    :param str exclude: pattern string to exclude maps from the research
    :param str flag: pattern type: 'r' (basic regexp), 'e' (extended regexp),
                                    or '' (glob pattern)
    :param env: environment

    :return: directory of mapsets/elements
    """
    if isinstance(type, str) or len(type) == 1:
        types = [type]
        store_types = False
    else:
        types = type
        store_types = True
        flag += "t"
    for i in range(len(types)):
        if types[i] == "cell":
            verbose(
                _('Element type should be "raster" and not "%s"') % types[i], env=env
            )
            types[i] = "raster"
    result = {}
    if check_search_path:
        for mapset in mapsets(search_path=True, env=env):
            if store_types:
                result[mapset] = {}
            else:
                result[mapset] = []

    mapset = None
    for line in read_command(
        "g.list",
        quiet=True,
        flags="m" + flag,
        type=types,
        pattern=pattern,
        exclude=exclude,
        env=env,
    ).splitlines():
        try:
            name, mapset = line.split("@")
        except ValueError:
            warning(_("Invalid element '%s'") % line, env=env)
            continue

        if store_types:
            type_, name = name.split("/")
            if mapset in result:
                if type_ in result[mapset]:
                    result[mapset][type_].append(name)
                else:
                    result[mapset][type_] = [
                        name,
                    ]
            else:
                result[mapset] = {
                    type_: [
                        name,
                    ]
                }
        elif mapset in result:
            result[mapset].append(name)
        else:
            result[mapset] = [
                name,
            ]

    return result


# color parsing

named_colors = {
    "white": (1.00, 1.00, 1.00),
    "black": (0.00, 0.00, 0.00),
    "red": (1.00, 0.00, 0.00),
    "green": (0.00, 1.00, 0.00),
    "blue": (0.00, 0.00, 1.00),
    "yellow": (1.00, 1.00, 0.00),
    "magenta": (1.00, 0.00, 1.00),
    "cyan": (0.00, 1.00, 1.00),
    "aqua": (0.00, 0.75, 0.75),
    "grey": (0.75, 0.75, 0.75),
    "gray": (0.75, 0.75, 0.75),
    "orange": (1.00, 0.50, 0.00),
    "brown": (0.75, 0.50, 0.25),
    "purple": (0.50, 0.00, 1.00),
    "violet": (0.50, 0.00, 1.00),
    "indigo": (0.00, 0.50, 1.00),
}


def parse_color(val, dflt=None):
    """Parses the string "val" as a GRASS colour, which can be either one of
    the named colours or an R:G:B tuple e.g. 255:255:255. Returns an
    (r,g,b) triple whose components are floating point values between 0
    and 1. Example:

    >>> parse_color("red")
    (1.0, 0.0, 0.0)
    >>> parse_color("255:0:0")
    (1.0, 0.0, 0.0)

    :param val: color value
    :param dflt: default color value

    :return: tuple RGB
    """
    if val in named_colors:
        return named_colors[val]

    vals = val.split(":")
    if len(vals) == 3:
        return tuple(float(v) / 255 for v in vals)

    return dflt


# check GRASS_OVERWRITE


def overwrite():
    """Return True if existing files may be overwritten"""
    owstr = "GRASS_OVERWRITE"
    return owstr in os.environ and os.environ[owstr] != "0"


# check GRASS_VERBOSE


def verbosity():
    """Return the verbosity level selected by GRASS_VERBOSE

    Currently, there are 5 levels of verbosity:
    -1 nothing will be printed (also fatal errors and warnings will be discarded)

    0 only errors and warnings are printed, triggered by "--q" or "--quiet" flag.

    1 progress information (percent) and important messages will be printed

    2 all messages will be printed

    3 also verbose messages will be printed. Triggered by "--v" or "--verbose" flag.
    """
    vbstr = os.getenv("GRASS_VERBOSE")
    if vbstr:
        return int(vbstr)
    return 2


# Various utilities, not specific to GRASS


def find_program(pgm, *args):
    """Attempt to run a program, with optional arguments.

    You must call the program in a way that will return a successful
    exit code. For GRASS modules this means you need to pass it some
    valid CLI option, like "--help". For other programs a common
    valid do-little option is usually "--version".

    Example:

    >>> find_program('r.sun', '--help')
    True
    >>> find_program('ls', '--version')
    True

    :param str pgm: program name
    :param args: list of arguments

    :return: False if the attempt failed due to a missing executable
            or non-zero return code
    :return: True otherwise
    """
    nuldev = open(os.devnull, "w+")
    try:
        # TODO: the doc or impl is not correct, any return code is accepted
        call([pgm] + list(args), stdin=nuldev, stdout=nuldev, stderr=nuldev)
        found = True
    except Exception:
        found = False
    nuldev.close()

    return found


# interface to g.mapsets


def mapsets(search_path=False, env=None):
    """List available mapsets

    :param bool search_path: True to list mapsets only in search path

    :return: list of mapsets
    """
    flags = "p" if search_path else "l"
    mapsets = read_command("g.mapsets", flags=flags, sep="newline", quiet=True, env=env)
    if not mapsets:
        fatal(_("Unable to list mapsets"), env=env)

    return mapsets.splitlines()


# interface to `g.proj -c`


def create_location(*args, **kwargs):
    if "dbase" in kwargs:
        kwargs["path"] = kwargs["dbase"]
        del kwargs["dbase"]
    if "location" in kwargs:
        kwargs["name"] = kwargs["location"]
        del kwargs["location"]
    return create_project(*args, **kwargs)


def create_project(
    path,
    name=None,
    epsg=None,
    proj4=None,
    filename=None,
    wkt=None,
    datum=None,
    datum_trans=None,
    desc=None,
    overwrite=False,
):
    """Create new project

    Raise ScriptError on error.

    :param str path: path to GRASS database or project; if path to database, project
                     name must be specified with name parameter
    :param str name: project name to create
    :param epsg: if given create new project based on EPSG code
    :param proj4: if given create new project based on Proj4 definition
    :param str filename: if given create new project based on georeferenced file
    :param str wkt: if given create new project based on WKT definition
                    (can be path to PRJ file or WKT string)
    :param datum: GRASS format datum code
    :param datum_trans: datum transformation parameters (used for epsg and proj4)
    :param desc: description of the project (creates MYNAME file)
    :param bool overwrite: True to overwrite project if exists (WARNING:
                           ALL DATA from existing project ARE DELETED!)
    """
    # Add default mapset to project path if needed
    if not name:
        path = os.path.join(path, "PERMANENT")

    # resolve dbase, location and mapset
    mapset_path = resolve_mapset_path(path=path, location=name)

    # create dbase if not exists
    if not os.path.exists(mapset_path.directory):
        os.mkdir(mapset_path.directory)

    # Lazy-importing to avoid circular dependencies.
    # pylint: disable=import-outside-toplevel
    if os.environ.get("GISBASE"):
        env = os.environ
    else:
        from grass.script.setup import setup_runtime_env

        env = os.environ.copy()
        setup_runtime_env(env=env)

    # Even g.proj and g.message need GISRC to be present.
    # The names don't really matter here.
    tmp_gisrc, env = create_environment(
        mapset_path.directory, mapset_path.location, mapset_path.mapset, env=env
    )

    # check if location already exists
    if Path(mapset_path.directory, mapset_path.location).exists():
        if not overwrite:
            fatal(
                _("Location <%s> already exists. Operation canceled.")
                % mapset_path.location,
                env=env,
            )
        warning(
            _("Location <%s> already exists and will be overwritten")
            % mapset_path.location,
            env=env,
        )
        shutil.rmtree(os.path.join(mapset_path.directory, mapset_path.location))

    stdin = None
    kwargs = {}
    if datum:
        kwargs["datum"] = datum
    if datum_trans:
        kwargs["datum_trans"] = datum_trans

    if epsg:
        ps = pipe_command(
            "g.proj",
            quiet=True,
            flags="t",
            epsg=epsg,
            project=mapset_path.location,
            stderr=PIPE,
            env=env,
            **kwargs,
        )
    elif proj4:
        ps = pipe_command(
            "g.proj",
            quiet=True,
            flags="t",
            proj4=proj4,
            project=mapset_path.location,
            stderr=PIPE,
            env=env,
            **kwargs,
        )
    elif filename:
        ps = pipe_command(
            "g.proj",
            quiet=True,
            georef=filename,
            project=mapset_path.location,
            stderr=PIPE,
            env=env,
        )
    elif wkt:
        if os.path.isfile(wkt):
            ps = pipe_command(
                "g.proj",
                quiet=True,
                wkt=wkt,
                project=mapset_path.location,
                stderr=PIPE,
                env=env,
            )
        else:
            ps = pipe_command(
                "g.proj",
                quiet=True,
                wkt="-",
                project=mapset_path.location,
                stderr=PIPE,
                stdin=PIPE,
                env=env,
            )
            stdin = encode(wkt)
    else:
        _create_location_xy(mapset_path.directory, mapset_path.location)

    if epsg or proj4 or filename or wkt:
        error = ps.communicate(stdin)[1]
        try_remove(tmp_gisrc)

        if ps.returncode != 0 and error:
            raise ScriptError(repr(error))

    _set_location_description(mapset_path.directory, mapset_path.location, desc)


def _set_location_description(path, location, text):
    """Set description (aka title aka MYNAME) for a location"""
    try:
        fd = codecs.open(
            os.path.join(path, location, "PERMANENT", "MYNAME"),
            encoding="utf-8",
            mode="w",
        )
        if text:
            fd.write(text + os.linesep)
        else:
            fd.write(os.linesep)
        fd.close()
    except OSError as e:
        raise ScriptError(repr(e))


def _create_location_xy(database, location):
    """Create unprojected location

    Raise ScriptError on error.

    :param database: GRASS database where to create new location
    :param location: location name
    """
    cur_dir = Path.cwd()
    try:
        os.chdir(database)
        os.mkdir(location)
        os.mkdir(os.path.join(location, "PERMANENT"))

        # create DEFAULT_WIND and WIND files
        regioninfo = [
            "proj:       0",
            "zone:       0",
            "north:      1",
            "south:      0",
            "east:       1",
            "west:       0",
            "cols:       1",
            "rows:       1",
            "e-w resol:  1",
            "n-s resol:  1",
            "top:        1",
            "bottom:     0",
            "cols3:      1",
            "rows3:      1",
            "depths:     1",
            "e-w resol3: 1",
            "n-s resol3: 1",
            "t-b resol:  1",
        ]

        defwind = open(os.path.join(location, "PERMANENT", "DEFAULT_WIND"), "w")
        for param in regioninfo:
            defwind.write(param + "%s" % os.linesep)
        defwind.close()

        shutil.copy(
            os.path.join(location, "PERMANENT", "DEFAULT_WIND"),
            os.path.join(location, "PERMANENT", "WIND"),
        )

        os.chdir(cur_dir)
    except OSError as e:
        raise ScriptError(repr(e))


# interface to g.version


def version():
    """Get GRASS version as dictionary

    ::

        >>> print(version())
        {'proj4': '4.8.0', 'geos': '3.3.5', 'libgis_revision': '52468',
         'libgis_date': '2012-07-27 22:53:30 +0200 (Fri, 27 Jul 2012)',
         'version': '7.0.svn', 'date': '2012', 'gdal': '2.0dev',
         'revision': '53670'}

    """
    data = parse_command("g.version", flags="rge", errors="ignore")
    for k, v in data.items():
        data[k.strip()] = v.replace('"', "").strip()

    return data


# get debug_level
_debug_level = None


def debug_level(force=False):
    global _debug_level
    if not force and _debug_level is not None:
        return _debug_level
    _debug_level = 0
    if find_program("g.gisenv", "--help"):
        try:
            _debug_level = int(gisenv().get("DEBUG", 0))
            if _debug_level < 0 or _debug_level > 5:
                raise ValueError(_("Debug level {0}").format(_debug_level))
        except ValueError as e:
            _debug_level = 0
            sys.stderr.write(
                _(
                    "WARNING: Ignoring unsupported debug level (must be >=0 and <=5):"
                    " {}\n"
                ).format(e)
            )

    return _debug_level


# TODO: Move legal_name() to utils or a new dedicated "name" module.
# TODO: Remove the pygrass backwards compatibility version of it?


def legal_name(s):
    """Checks if the string contains only allowed characters.

    This is the Python implementation of :func:`G_legal_filename()` function.

    ..note::

        It is not clear when exactly use this function, but it might be
        useful anyway for checking map names and column names.
    """
    if not s or s[0] == ".":
        warning(_("Illegal filename <%s>. Cannot be 'NULL' or start with '.'.") % s)
        return False

    illegal = [c for c in s if c in "/\"'@,=*~" or c <= " " or c >= "\177"]
    if illegal:
        illegal = "".join(sorted(set(illegal)))
        warning(
            _("Illegal filename <%(s)s>. <%(il)s> not allowed.\n")
            % {"s": s, "il": illegal}
        )
        return False

    return True


def sanitize_mapset_environment(env):
    """Remove environmental variables relevant only
    for a specific mapset. This should be called
    when a copy of environment is used with a different mapset."""
    if "WIND_OVERRIDE" in env:
        del env["WIND_OVERRIDE"]
    if "GRASS_REGION" in env:
        del env["GRASS_REGION"]
    return env


def create_environment(gisdbase, location, mapset, env=None):
    """Creates environment to be passed in run_command for example.
    Returns tuple with temporary file path and the environment. The user
    of this function is responsible for deleting the file."""
    with NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("MAPSET: {mapset}\n".format(mapset=mapset))
        f.write("GISDBASE: {g}\n".format(g=gisdbase))
        f.write("LOCATION_NAME: {l}\n".format(l=location))
        f.write("GUI: text\n")
    env = env.copy() if env else os.environ.copy()
    env["GISRC"] = f.name
    # remove mapset-specific env vars
    env = sanitize_mapset_environment(env)
    return f.name, env


if __name__ == "__main__":
    import doctest

    doctest.testmod()
