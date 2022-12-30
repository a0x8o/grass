# RFC 7: Language Standards Support

Author of the first draft: Nicklas Larsson

Status: Motion passed, 29 March 2021

## Introduction
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
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
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
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
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
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
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
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
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
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
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
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
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
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
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
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
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
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
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
=======
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
=======

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
=======

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))

The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code
(ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these
languages have evolved significantly in the last 10–20 years. There is, however,
no clearly stated policy of supported language standard(s), nor mechanism to
update this policy when needed or wanted. This result in uncertainty for
contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language
standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this
subject.

## Background

Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have
been taken to adapt and modernize. The latest big modernization of the C code
was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)),
when it was updated to conform to C89 (ANSI C) standard. A major job, which has
payed-off well. However, during the years, language features of successive
standards have slipped into the code base, which is no longer strictly C89
(nor C90) conformant. There are no compelling reasons to revert the existing
code to strict C89, therefore the community has to decide which standard to
adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and
officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list
[thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion

<<<<<<< HEAD
It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
The advantage of having clearly stated policy on language standard
requirements/support is important not only for contributors, but also sets the
frame for supported platforms. For the latter, also the reverse is true: in
deciding supported standard the community needs to consider the degree of
support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also
with C17 and C++17. There is therefore no need to modernize it the way it was
done to C in the 2000’s. Nevertheless, conforming to newer standards may
provide better cross platform support and possibly safer code.
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
The code base of GRASS GIS consists today (Feb. 2021) of predominantly C code (ca 50 %), Python (ca 30 %) and a smaller amount of C++ (ca 5 %). Each of these languages have evolved significantly in the last 10–20 years. There is, however, no clearly stated policy of supported language standard(s), nor mechanism to update this policy when needed or wanted. This result in uncertainty for contributors for what may be allowed and solutions that may not be optimal.

This RFC aims at setting a policy for GRASS GIS project regarding language standard support for C and C++.

In addition, this is also intended to set a precedent for future updates on this subject.

## Background
Throughout its long history, soon 40 years, GRASS GIS has evolved and steps have been taken to adapt and modernize. The latest big modernization of the C code was done in 2002–2006 ([summary](https://lists.osgeo.org/pipermail/grass-dev/2021-February/094955.html)), when it was updated to conform to C89 (ANSI C) standard. A major job, which has payed-off well. However, during the years, language features of successive standards have slipped into the code base, which is no longer strictly C89 (nor C90) conformant. There are no compelling reasons to revert the existing code to strict C89, therefore the community has to decide which standard to adhere to.

The small amount of C++ code in GRASS GIS has never been formalised and officially made to conform to any specific standard.

See also the discussion leading to this RFC on the mailing list [thread](https://lists.osgeo.org/pipermail/grass-dev/2021-January/094899.html).

## Discussion
The advantage of having clearly stated policy on language standard requirements/support is important not only for contributors, but also sets the frame for supported platforms. For the latter, also the reverse is true: in deciding supported standard the community needs to consider the degree of support of standards for various platforms.

It should be emphasized that existing GRASS GIS C and C++ code compiles also with C17 and C++17. There is therefore no need to modernize it the way it was done to C in the 2000’s. Nevertheless, conforming to newer standards may provide better cross platform support and possibly safer code.
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))

Regarding C, there are three standards that may be considered: C99, C11 and
C17. C99 never really reached full support on key platforms, this is
particularly the case for Windows
([Visual Studio 2013](https://devblogs.microsoft.com/cppblog/c99-library-support-in-visual-studio-2013/)).
Partly in consequence of this lack of support for some C99 features, the C11
standard was made less strict: making some C99 mandatory features optional.
Thus, from autumn 2020 even
[MSVC complies to C11](https://devblogs.microsoft.com/cppblog/c11-and-c17-standard-support-arriving-in-msvc/)
core feature support. Starting with
[GCC 4.9](https://gcc.gnu.org/wiki/C11Status) it had “substantially
complete” support for C11, Clang from
[version 3.1](https://releases.llvm.org/3.1/docs/ClangReleaseNotes.html).
[C17](https://en.wikipedia.org/wiki/C17_(C_standard_revision)), on the other
hand, doesn’t add new features compared to C11. Its difference is more
interesting from compiler point of view, whereas code “good for C11” is
good for C17.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
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
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
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
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
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
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to
consider. The platform and compiler support for all of these are significantly
better. However, C++11 is at this date in general considered the standard and
until compelling reasons argue otherwise, the C++11 standard should be policy of
the GRASS GIS project.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
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
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
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
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
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
>>>>>>> osgeo-main
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to
consider. The platform and compiler support for all of these are significantly
better. However, C++11 is at this date in general considered the standard and
until compelling reasons argue otherwise, the C++11 standard should be policy of
the GRASS GIS project.
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
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
=======
>>>>>>> osgeo-main
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to
consider. The platform and compiler support for all of these are significantly
better. However, C++11 is at this date in general considered the standard and
until compelling reasons argue otherwise, the C++11 standard should be policy of
the GRASS GIS project.
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
<<<<<<< HEAD
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
=======
<<<<<<< HEAD
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
=======
Regarding C++, there are the C++98, C++03, C++11, C++14 and C++17 standards to consider. The platform and compiler support for all of these are significantly better. However, C++11 is at this date in general considered the standard and until compelling reasons argue otherwise, the C++11 standard should be policy of the GRASS GIS project.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))

## Proposed Language Standards Support

### C Language
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))

=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))

>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
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
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
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
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======

=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
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
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
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
>>>>>>> osgeo-main
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
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
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======

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
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
=======

>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not
supported, alternative fallback code must be provided.

### C++ Language

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
=======
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
C11 with core (mandatory) features [brief summary](https://en.wikipedia.org/wiki/C11_(C_standard_revision))

Optional features may be used if availability is tested with macro, and if not supported, alternative fallback code must be provided.

### C++ Language
C++11 [summary](https://en.wikipedia.org/wiki/C%2B%2B11)

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
