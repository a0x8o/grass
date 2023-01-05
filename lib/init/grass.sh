#! /bin/sh
#############################################################################
#
# MODULE:   	GRASS initialization (Shell)
# AUTHOR(S):	Original author unknown - probably CERL
#               Andreas Lange - Germany - andreas.lange@rhein-main.de
#   	    	Huidae Cho - Korea - grass4u@gmail.com
#   	    	Justin Hickey - Thailand - jhickey@hpcc.nectec.or.th
#   	    	Markus Neteler - Germany/Italy - neteler@itc.it
#		Hamish Bowman - New Zealand - hamish_b at yahoo,com
# PURPOSE:  	Sets up some environment variables.
#               It also parses any remaining command line options for
#               setting the GISDBASE, LOCATION, and/or MAPSET.
#               Finally it starts GRASS with the appropriate user
#   	    	interface and cleans up after it is finished.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1b1f0f4b5e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 64ef346811 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> main
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43cc51eca7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4255a3409f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
# COPYRIGHT:    (C) 2000-2024 by the GRASS Development Team
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
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
=======
=======
=======
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
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
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
=======
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> c722182c26 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b4675dccbc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1c3b930edc (r.terrafow: explicit use of default constructors (#2660))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68c589f721 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> osgeo-main
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
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
<<<<<<< HEAD
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
>>>>>>> 55f5df1296 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 170c3816b1 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> d337db2dff (Merge branch 'a0x8o' into stag0)
=======
<<<<<<< HEAD
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> 936c2c0116 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
>>>>>>> 4c8699bc56 (r.terrafow: explicit use of default constructors (#2660))
=======
<<<<<<< HEAD
>>>>>>> d0c4af5f80 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 099850264f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 0e678c812a (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 3df1af6046 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> ab3f49acee (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 984f2e4b5f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 8c60dd2ea6 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> fa8258f7da (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> a281b09609 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f3d76d90e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d57829fdd5 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 4c14c5377c (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 482cd79ba4 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> b13ee245c1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 067b5a8bb0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> f59448a530 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> fd3cfb9175 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 115d1c2b17 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 0785c4fdc0 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 8da59835e3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 706ee84443 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 1ac37540a5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 45a737e836 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 40ae4b13c4 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 60bf55d59f (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 21a39e2108 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> e86987389e (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> d46f4229a7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c745556f47 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
=======
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
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> 09b5ece2f7 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a1e3744f68 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> ca3778dbc8 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> b8d5485baf (i.maxlik: fix crash when classification result is NULL (#2724))
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4255a3409f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
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
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 506d884519 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c066e85bd (i.maxlik: fix crash when classification result is NULL (#2724))
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
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
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
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 5a6c7b69e7 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2b1d4404b4 (i.maxlik: fix crash when classification result is NULL (#2724))
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
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
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
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 30bd67812c (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7e84920a91 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
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
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
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
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 0b1431f1d8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 763393c2b3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 630833279b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2fb156cfe5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 2ff2be4826 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> d0c4af5f80 (i.maxlik: fix crash when classification result is NULL (#2724))
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
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
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
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 918f6991c4 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 28cedb28c6 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 099850264f (i.maxlik: fix crash when classification result is NULL (#2724))
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
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
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
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> bdf51e20a8 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 3df1af6046 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c7dc67a478 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 984f2e4b5f (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 8f9937d00a (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> fa8258f7da (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c4ee228391 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> f3d76d90e7 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> d88b10832d (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 4c14c5377c (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 385c333a86 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> b13ee245c1 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> a7da23483e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> f59448a530 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> fb8e87c2a1 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 115d1c2b17 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> e0fc7e2fee (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 8da59835e3 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> fc4d6dbb1b (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 1ac37540a5 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 3662b58228 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 40ae4b13c4 (i.maxlik: fix crash when classification result is NULL (#2724))
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
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
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
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 3d3f3040e9 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> dfc4e9b268 (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 21a39e2108 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 7c58471b8e (i.maxlik: fix crash when classification result is NULL (#2724))
<<<<<<< HEAD
>>>>>>> 5ce13cea96 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c1fe2d6941 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> c745556f47 (i.maxlik: fix crash when classification result is NULL (#2724))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
=======
# COPYRIGHT:    (C) 2000-2023 by the GRASS Development Team
>>>>>>> 6104ec7096 (i.maxlik: fix crash when classification result is NULL (#2724))
>>>>>>> 2788a5026e (i.maxlik: fix crash when classification result is NULL (#2724))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
# COPYRIGHT:    (C) 2000-2022 by the GRASS Development Team
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b613d037dd (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> c7e56315ec (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> c68c3cd4d0 (i.maxlik: fix crash when classification result is NULL (#2724))
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fc6ae6c77c (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 9e866bbf71 (r.terrafow: explicit use of default constructors (#2660))
>>>>>>> 89354d0c4e (Merge branch 'a0x8o' into stag0)
#
#               This program is free software under the GNU General
#   	    	Public License (>=v2). Read the file COPYING that
#   	    	comes with GRASS for details.
#
#############################################################################

trap "echo 'User break!' ; exit" 2 3 9 15

if [ -z "$GRASS_PYTHON" ] ; then
    GRASS_PYTHON=python3
fi
export GRASS_PYTHON

exec "$GRASS_PYTHON" "@BINDIR@/grass.py" "$@" &
