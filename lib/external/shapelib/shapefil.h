#ifndef SHAPEFILE_H_INCLUDED
#define SHAPEFILE_H_INCLUDED

/******************************************************************************
 *
 * Project:  Shapelib
 * Purpose:  Primary include file for Shapelib.
 * Author:   Frank Warmerdam, warmerdam@pobox.com
 *
 ******************************************************************************
 * Copyright (c) 1999, Frank Warmerdam
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> osgeo-main
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
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
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
 *
 * SPDX-License-Identifier: MIT OR LGPL-2.0-or-later
 ******************************************************************************
 *
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
 *
 * This software is available under the following "MIT Style" license,
 * or at the option of the licensee under the LGPL (see COPYING).  This
 * option is discussed in more detail in shapelib.html.
 *
 * --
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 ******************************************************************************
 *
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
 * $Log: shapefil.h,v $
 * Revision 1.52  2011-12-11 22:26:46  fwarmerdam
 * upgrade .qix access code to use SAHooks (gdal #3365)
 *
 * Revision 1.51  2011-07-24 05:59:25  fwarmerdam
 * minimize use of CPLError in favor of SAHooks.Error()
 *
 * Revision 1.50  2011-05-13 17:35:17  fwarmerdam
 * added DBFReorderFields() and DBFAlterFields() functions (from Even)
 *
 * Revision 1.49  2011-04-16 14:38:21  fwarmerdam
 * avoid warnings with gcc on SHP_CVSID
 *
 * Revision 1.48  2010-08-27 23:42:52  fwarmerdam
 * add SHPAPI_CALL attribute in code
 *
 * Revision 1.47  2010-01-28 11:34:34  fwarmerdam
 * handle the shape file length limits more gracefully (#3236)
 *
 * Revision 1.46  2008-11-12 14:28:15  fwarmerdam
 * DBFCreateField() now works on files with records
 *
 * Revision 1.45  2008/11/11 17:47:10  fwarmerdam
 * added DBFDeleteField() function
 *
 * Revision 1.44  2008/01/16 20:05:19  bram
 * Add file hooks that accept UTF-8 encoded filenames on some platforms.  Use
 *SASetupUtf8Hooks tosetup the hooks and check SHPAPI_UTF8_HOOKS for its
 *availability.  Currently, this is only available on the Windows platform that
 *decodes the UTF-8 filenames to wide character strings and feeds them to
 *_wfopen and _wremove.
 *
 * Revision 1.43  2008/01/10 16:35:30  fwarmerdam
 * avoid _ prefix on #defined symbols (bug 1840)
 *
 * Revision 1.42  2007/12/18 18:28:14  bram
 * - create hook for client specific atof (bugzilla ticket 1615)
 * - check for NULL handle before closing cpCPG file, and close after reading.
 *
 * Revision 1.41  2007/12/15 20:25:32  bram
 * dbfopen.c now reads the Code Page information from the DBF file, and exports
 * this information as a string through the DBFGetCodePage function.  This is
 * either the number from the LDID header field ("LDID/<number>") or as the
 * content of an accompanying .CPG file.  When creating a DBF file, the code can
 * be set using DBFCreateEx.
 *
 * Revision 1.40  2007/12/06 07:00:25  fwarmerdam
 * dbfopen now using SAHooks for fileio
 *
 * Revision 1.39  2007/12/04 20:37:56  fwarmerdam
 * preliminary implementation of hooks api for io and errors
 *
 * Revision 1.38  2007/11/21 22:39:56  fwarmerdam
 * close shx file in readonly mode (GDAL #1956)
 *
 * Revision 1.37  2007/10/27 03:31:14  fwarmerdam
 * limit default depth of tree to 12 levels (gdal ticket #1594)
 *
 * Revision 1.36  2007/09/10 23:33:15  fwarmerdam
 * Upstreamed support for visibility flag in SHPAPI_CALL for the needs
 * of GDAL (gdal ticket #1810).
 *
 * Revision 1.35  2007/09/03 19:48:10  fwarmerdam
 * move DBFReadAttribute() static dDoubleField into dbfinfo
 *
 * Revision 1.34  2006/06/17 15:33:32  fwarmerdam
 * added pszWorkField - bug 1202 (rso)
 *
 * Revision 1.33  2006/02/15 01:14:30  fwarmerdam
 * added DBFAddNativeFieldType
 *
 * Revision 1.32  2006/01/26 15:07:32  fwarmerdam
 * add bMeasureIsUsed flag from Craig Bruce: Bug 1249
 *
 * Revision 1.31  2006/01/05 01:27:27  fwarmerdam
 * added dbf deletion mark/fetch
 *
 * Revision 1.30  2005/01/03 22:30:13  fwarmerdam
 * added support for saved quadtrees
 *
 * Revision 1.29  2004/09/26 20:09:35  fwarmerdam
 * avoid rcsid warnings
 *
 * Revision 1.28  2003/12/29 06:02:18  fwarmerdam
 * added cpl_error.h option
 *
 * Revision 1.27  2003/04/21 18:30:37  warmerda
 * added header write/update public methods
 *
 * Revision 1.26  2002/09/29 00:00:08  warmerda
 * added FTLogical and logical attribute read/write calls
 *
 * Revision 1.25  2002/05/07 13:46:30  warmerda
 * added DBFWriteAttributeDirectly().
 *
 * Revision 1.24  2002/04/10 16:59:54  warmerda
 * added SHPRewindObject
 *
 * Revision 1.23  2002/01/15 14:36:07  warmerda
 * updated email address
 *
 * Revision 1.22  2002/01/15 14:32:00  warmerda
 * try to improve SHPAPI_CALL docs
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
 * Copyright (c) 2012-2013, Even Rouault <even dot rouault at mines-paris dot
 *org>
=======
 * Copyright (c) 2012-2016, Even Rouault <even dot rouault at spatialys.com>
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
 *
 * This software is available under the following "MIT Style" license,
 * or at the option of the licensee under the LGPL (see COPYING).  This
 * option is discussed in more detail in shapelib.html.
 *
 * --
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 ******************************************************************************
 *
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
 * $Log: shapefil.h,v $
 * Revision 1.52  2011-12-11 22:26:46  fwarmerdam
 * upgrade .qix access code to use SAHooks (gdal #3365)
 *
 * Revision 1.51  2011-07-24 05:59:25  fwarmerdam
 * minimize use of CPLError in favor of SAHooks.Error()
 *
 * Revision 1.50  2011-05-13 17:35:17  fwarmerdam
 * added DBFReorderFields() and DBFAlterFields() functions (from Even)
 *
 * Revision 1.49  2011-04-16 14:38:21  fwarmerdam
 * avoid warnings with gcc on SHP_CVSID
 *
 * Revision 1.48  2010-08-27 23:42:52  fwarmerdam
 * add SHPAPI_CALL attribute in code
 *
 * Revision 1.47  2010-01-28 11:34:34  fwarmerdam
 * handle the shape file length limits more gracefully (#3236)
 *
 * Revision 1.46  2008-11-12 14:28:15  fwarmerdam
 * DBFCreateField() now works on files with records
 *
 * Revision 1.45  2008/11/11 17:47:10  fwarmerdam
 * added DBFDeleteField() function
 *
 * Revision 1.44  2008/01/16 20:05:19  bram
 * Add file hooks that accept UTF-8 encoded filenames on some platforms.  Use
 *SASetupUtf8Hooks tosetup the hooks and check SHPAPI_UTF8_HOOKS for its
 *availability.  Currently, this is only available on the Windows platform that
 *decodes the UTF-8 filenames to wide character strings and feeds them to
 *_wfopen and _wremove.
 *
 * Revision 1.43  2008/01/10 16:35:30  fwarmerdam
 * avoid _ prefix on #defined symbols (bug 1840)
 *
 * Revision 1.42  2007/12/18 18:28:14  bram
 * - create hook for client specific atof (bugzilla ticket 1615)
 * - check for NULL handle before closing cpCPG file, and close after reading.
 *
 * Revision 1.41  2007/12/15 20:25:32  bram
 * dbfopen.c now reads the Code Page information from the DBF file, and exports
 * this information as a string through the DBFGetCodePage function.  This is
 * either the number from the LDID header field ("LDID/<number>") or as the
 * content of an accompanying .CPG file.  When creating a DBF file, the code can
 * be set using DBFCreateEx.
 *
 * Revision 1.40  2007/12/06 07:00:25  fwarmerdam
 * dbfopen now using SAHooks for fileio
 *
 * Revision 1.39  2007/12/04 20:37:56  fwarmerdam
 * preliminary implementation of hooks api for io and errors
 *
 * Revision 1.38  2007/11/21 22:39:56  fwarmerdam
 * close shx file in readonly mode (GDAL #1956)
 *
 * Revision 1.37  2007/10/27 03:31:14  fwarmerdam
 * limit default depth of tree to 12 levels (gdal ticket #1594)
 *
 * Revision 1.36  2007/09/10 23:33:15  fwarmerdam
 * Upstreamed support for visibility flag in SHPAPI_CALL for the needs
 * of GDAL (gdal ticket #1810).
 *
 * Revision 1.35  2007/09/03 19:48:10  fwarmerdam
 * move DBFReadAttribute() static dDoubleField into dbfinfo
 *
 * Revision 1.34  2006/06/17 15:33:32  fwarmerdam
 * added pszWorkField - bug 1202 (rso)
 *
 * Revision 1.33  2006/02/15 01:14:30  fwarmerdam
 * added DBFAddNativeFieldType
 *
 * Revision 1.32  2006/01/26 15:07:32  fwarmerdam
 * add bMeasureIsUsed flag from Craig Bruce: Bug 1249
 *
 * Revision 1.31  2006/01/05 01:27:27  fwarmerdam
 * added dbf deletion mark/fetch
 *
 * Revision 1.30  2005/01/03 22:30:13  fwarmerdam
 * added support for saved quadtrees
 *
 * Revision 1.29  2004/09/26 20:09:35  fwarmerdam
 * avoid rcsid warnings
 *
 * Revision 1.28  2003/12/29 06:02:18  fwarmerdam
 * added cpl_error.h option
 *
 * Revision 1.27  2003/04/21 18:30:37  warmerda
 * added header write/update public methods
 *
 * Revision 1.26  2002/09/29 00:00:08  warmerda
 * added FTLogical and logical attribute read/write calls
 *
 * Revision 1.25  2002/05/07 13:46:30  warmerda
 * added DBFWriteAttributeDirectly().
 *
 * Revision 1.24  2002/04/10 16:59:54  warmerda
 * added SHPRewindObject
 *
 * Revision 1.23  2002/01/15 14:36:07  warmerda
 * updated email address
 *
 * Revision 1.22  2002/01/15 14:32:00  warmerda
 * try to improve SHPAPI_CALL docs
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
 */

#include <stdio.h>

#ifdef USE_CPL
#include "cpl_conv.h"
#endif

#ifdef __cplusplus
extern "C" {
#endif

/************************************************************************/
/*           Version related macros (added in 1.6.0)                    */
/************************************************************************/

#define SHAPELIB_VERSION_MAJOR 1
#define SHAPELIB_VERSION_MINOR 6
#define SHAPELIB_VERSION_MICRO 0

#define SHAPELIB_MAKE_VERSION_NUMBER(major, minor, micro) \
    ((major) * 10000 + (minor) * 100 + (micro))

#define SHAPELIB_VERSION_NUMBER                          \
    SHAPELIB_MAKE_VERSION_NUMBER(SHAPELIB_VERSION_MAJOR, \
                                 SHAPELIB_VERSION_MINOR, \
                                 SHAPELIB_VERSION_MICRO)

#define SHAPELIB_AT_LEAST(major, minor, micro) \
    (SHAPELIB_VERSION_NUMBER >=                \
     SHAPELIB_MAKE_VERSION_NUMBER(major, minor, micro))

/************************************************************************/
/*                        Configuration options.                        */

/************************************************************************/

/* -------------------------------------------------------------------- */
/*      Should the DBFReadStringAttribute() strip leading and           */
/*      trailing white space?                                           */
/* -------------------------------------------------------------------- */
#define TRIM_DBF_WHITESPACE

/* -------------------------------------------------------------------- */
/*      Should we write measure values to the Multipatch object?        */
/*      Reportedly ArcView crashes if we do write it, so for now it     */
/*      is disabled.                                                    */
/* -------------------------------------------------------------------- */
#define DISABLE_MULTIPATCH_MEASURE

/* -------------------------------------------------------------------- */
/*      SHPAPI_CALL                                                     */
/*                                                                      */
/*      The following two macros are present to allow forcing           */
/*      various calling conventions on the Shapelib API.                */
/*                                                                      */
/*      To force __stdcall conventions (needed to call Shapelib         */
/*      from Visual Basic and/or Delphi I believe) the makefile could   */
/*      be modified to define:                                          */
/*                                                                      */
/*        /DSHPAPI_CALL=__stdcall                                       */
/*                                                                      */
/*      If it is desired to force export of the Shapelib API without    */
/*      using the shapelib.def file, use the following definition.      */
/*                                                                      */
/*        /DSHAPELIB_DLLEXPORT                                          */
/*                                                                      */
/*      To get both at once it will be necessary to hack this           */
/*      include file to define:                                         */
/*                                                                      */
/*        #define SHPAPI_CALL __declspec(dllexport) __stdcall           */
/*        #define SHPAPI_CALL1 __declspec(dllexport) * __stdcall        */
/*                                                                      */
/*      The complexity of the situation is partly caused by the        */
/*      peculiar requirement of Visual C++ that __stdcall appear        */
/*      after any "*"'s in the return value of a function while the     */
/*      __declspec(dllexport) must appear before them.                  */
/* -------------------------------------------------------------------- */

#ifdef SHAPELIB_DLLEXPORT
#define SHPAPI_CALL     __declspec(dllexport)
#define SHPAPI_CALL1(x) __declspec(dllexport) x
#endif

#ifndef SHPAPI_CALL
#if defined(USE_GCC_VISIBILITY_FLAG)
#define SHPAPI_CALL     __attribute__((visibility("default")))
#define SHPAPI_CALL1(x) __attribute__((visibility("default"))) x
#else
#define SHPAPI_CALL
#endif
#endif

#ifndef SHPAPI_CALL1
#define SHPAPI_CALL1(x) x SHPAPI_CALL
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
#endif

/* -------------------------------------------------------------------- */
/*      Macros for controlling CVSID and ensuring they don't appear     */
/*      as unreferenced variables resulting in lots of warnings.        */
/* -------------------------------------------------------------------- */
#ifndef DISABLE_CVSID
#if defined(__GNUC__) && __GNUC__ >= 4
#define SHP_CVSID(string) \
    static const char cpl_cvsid[] __attribute__((used)) = string;
#else
#define SHP_CVSID(string)                       \
    static const char cpl_cvsid[] = string;     \
    static const char *cvsid_aw()               \
    {                                           \
        return (cvsid_aw() ? NULL : cpl_cvsid); \
    }
#endif
#else
#define SHP_CVSID(string)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
#endif

/* -------------------------------------------------------------------- */
/*      On some platforms, additional file IO hooks are defined that    */
/*      UTF-8 encoded filenames Unicode filenames                       */
/* -------------------------------------------------------------------- */
<<<<<<< HEAD
#if defined(_WIN32)
=======
#if defined(_WIN32) || defined(__WIN32__) || defined(WIN32)
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
#define SHPAPI_WINDOWS
#define SHPAPI_UTF8_HOOKS
#endif

/* -------------------------------------------------------------------- */
/*      IO/Error hook functions.                                        */
/* -------------------------------------------------------------------- */
typedef int *SAFile;

#ifndef SAOffset
#if defined(_MSC_VER) && _MSC_VER >= 1400
typedef unsigned __int64 SAOffset;
#else
typedef unsigned long SAOffset;
#endif
#endif

typedef struct {
<<<<<<< HEAD
<<<<<<< HEAD
    SAFile (*FOpen)(const char *filename, const char *access, void *pvUserData);
    SAOffset (*FRead)(void *p, SAOffset size, SAOffset nmemb, SAFile file);
    SAOffset (*FWrite)(const void *p, SAOffset size, SAOffset nmemb,
                       SAFile file);
=======
    SAFile (*FOpen)(const char *filename, const char *access);
    SAOffset (*FRead)(void *p, SAOffset size, SAOffset nmemb, SAFile file);
    SAOffset (*FWrite)(void *p, SAOffset size, SAOffset nmemb, SAFile file);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    SAFile (*FOpen)(const char *filename, const char *access);
    SAOffset (*FRead)(void *p, SAOffset size, SAOffset nmemb, SAFile file);
    SAOffset (*FWrite)(void *p, SAOffset size, SAOffset nmemb, SAFile file);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    SAOffset (*FSeek)(SAFile file, SAOffset offset, int whence);
    SAOffset (*FTell)(SAFile file);
    int (*FFlush)(SAFile file);
    int (*FClose)(SAFile file);
<<<<<<< HEAD
<<<<<<< HEAD
    int (*Remove)(const char *filename, void *pvUserData);

    void (*Error)(const char *message);
    double (*Atof)(const char *str);
    void *pvUserData;
=======
    int (*Remove)(const char *filename);

    void (*Error)(const char *message);
    double (*Atof)(const char *str);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    int (*Remove)(const char *filename);

    void (*Error)(const char *message);
    double (*Atof)(const char *str);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
} SAHooks;

void SHPAPI_CALL SASetupDefaultHooks(SAHooks *psHooks);
#ifdef SHPAPI_UTF8_HOOKS
void SHPAPI_CALL SASetupUtf8Hooks(SAHooks *psHooks);
#endif

/************************************************************************/
/*                             SHP Support.                             */

/************************************************************************/
typedef struct tagSHPObject SHPObject;

typedef struct {
    SAHooks sHooks;

    SAFile fpSHP;
    SAFile fpSHX;

    int nShapeType; /* SHPT_* */

    unsigned int nFileSize; /* SHP file */

    int nRecords;
    int nMaxRecords;
    unsigned int *panRecOffset;
    unsigned int *panRecSize;

    double adBoundsMin[4];
    double adBoundsMax[4];

    int bUpdated;

    unsigned char *pabyRec;
    int nBufSize;

    int bFastModeReadObject;
    unsigned char *pabyObjectBuf;
    int nObjectBufSize;
    SHPObject *psCachedObject;
} SHPInfo;

typedef SHPInfo *SHPHandle;
<<<<<<< HEAD
<<<<<<< HEAD

typedef struct {
    int year;
    int month;
    int day;
} SHPDate;
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

/* -------------------------------------------------------------------- */
/*      Shape types (nSHPType)                                          */
/* -------------------------------------------------------------------- */
#define SHPT_NULL        0
#define SHPT_POINT       1
#define SHPT_ARC         3
#define SHPT_POLYGON     5
#define SHPT_MULTIPOINT  8
#define SHPT_POINTZ      11
#define SHPT_ARCZ        13
#define SHPT_POLYGONZ    15
#define SHPT_MULTIPOINTZ 18
#define SHPT_POINTM      21
#define SHPT_ARCM        23
#define SHPT_POLYGONM    25
#define SHPT_MULTIPOINTM 28
#define SHPT_MULTIPATCH  31

/* -------------------------------------------------------------------- */
/*      Part types - everything but SHPT_MULTIPATCH just uses           */
/*      SHPP_RING.                                                      */
/* -------------------------------------------------------------------- */

#define SHPP_TRISTRIP    0
#define SHPP_TRIFAN      1
#define SHPP_OUTERRING   2
#define SHPP_INNERRING   3
#define SHPP_FIRSTRING   4
#define SHPP_RING        5

/* -------------------------------------------------------------------- */
/*      SHPObject - represents on shape (without attributes) read       */
/*      from the .shp file.                                             */
/* -------------------------------------------------------------------- */
struct tagSHPObject {
    int nSHPType;

    int nShapeId; /* -1 is unknown/unassigned */

    int nParts;
    int *panPartStart;
    int *panPartType;

    int nVertices;
    double *padfX;
    double *padfY;
    double *padfZ;
    double *padfM;

    double dfXMin;
    double dfYMin;
    double dfZMin;
    double dfMMin;

    double dfXMax;
    double dfYMax;
    double dfZMax;
    double dfMMax;

    int bMeasureIsUsed;
    int bFastModeReadObject;
};

/* -------------------------------------------------------------------- */
/*      SHP API Prototypes                                              */
/* -------------------------------------------------------------------- */

/* If pszAccess is read-only, the fpSHX field of the returned structure */
/* will be NULL as it is not necessary to keep the SHX file open */
SHPHandle SHPAPI_CALL SHPOpen(const char *pszShapeFile, const char *pszAccess);
SHPHandle SHPAPI_CALL SHPOpenLL(const char *pszShapeFile, const char *pszAccess,
<<<<<<< HEAD
<<<<<<< HEAD
                                const SAHooks *psHooks);
SHPHandle SHPAPI_CALL SHPOpenLLEx(const char *pszShapeFile,
                                  const char *pszAccess, const SAHooks *psHooks,
                                  int bRestoreSHX);

int SHPAPI_CALL SHPRestoreSHX(const char *pszShapeFile, const char *pszAccess,
                              const SAHooks *psHooks);
=======
                                SAHooks *psHooks);
SHPHandle SHPAPI_CALL SHPOpenLLEx(const char *pszShapeFile,
                                  const char *pszAccess, SAHooks *psHooks,
                                  int bRestoreSHX);

int SHPAPI_CALL SHPRestoreSHX(const char *pszShapeFile, const char *pszAccess,
                              SAHooks *psHooks);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))

=======
                                SAHooks *psHooks);
SHPHandle SHPAPI_CALL SHPOpenLLEx(const char *pszShapeFile,
                                  const char *pszAccess, SAHooks *psHooks,
                                  int bRestoreSHX);

int SHPAPI_CALL SHPRestoreSHX(const char *pszShapeFile, const char *pszAccess,
                              SAHooks *psHooks);

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
/* If setting bFastMode = TRUE, the content of SHPReadObject() is owned by the
 * SHPHandle. */
/* So you cannot have 2 valid instances of SHPReadObject() simultaneously. */
/* The SHPObject padfZ and padfM members may be NULL depending on the geometry
 */
/* type. It is illegal to free at hand any of the pointer members of the
 * SHPObject structure */
void SHPAPI_CALL SHPSetFastModeReadObject(SHPHandle hSHP, int bFastMode);

SHPHandle SHPAPI_CALL SHPCreate(const char *pszShapeFile, int nShapeType);
SHPHandle SHPAPI_CALL SHPCreateLL(const char *pszShapeFile, int nShapeType,
<<<<<<< HEAD
<<<<<<< HEAD
                                  const SAHooks *psHooks);
void SHPAPI_CALL SHPGetInfo(const SHPHandle hSHP, int *pnEntities,
                            int *pnShapeType, double *padfMinBound,
                            double *padfMaxBound);

SHPObject SHPAPI_CALL1(*) SHPReadObject(const SHPHandle hSHP, int iShape);
int SHPAPI_CALL SHPWriteObject(SHPHandle hSHP, int iShape,
                               const SHPObject *psObject);
=======
                                  SAHooks *psHooks);
void SHPAPI_CALL SHPGetInfo(SHPHandle hSHP, int *pnEntities, int *pnShapeType,
                            double *padfMinBound, double *padfMaxBound);

SHPObject SHPAPI_CALL1(*) SHPReadObject(SHPHandle hSHP, int iShape);
int SHPAPI_CALL SHPWriteObject(SHPHandle hSHP, int iShape, SHPObject *psObject);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                                  SAHooks *psHooks);
void SHPAPI_CALL SHPGetInfo(SHPHandle hSHP, int *pnEntities, int *pnShapeType,
                            double *padfMinBound, double *padfMaxBound);

SHPObject SHPAPI_CALL1(*) SHPReadObject(SHPHandle hSHP, int iShape);
int SHPAPI_CALL SHPWriteObject(SHPHandle hSHP, int iShape, SHPObject *psObject);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL SHPDestroyObject(SHPObject *psObject);
void SHPAPI_CALL SHPComputeExtents(SHPObject *psObject);
SHPObject SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
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
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======

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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
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

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
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
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======

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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
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

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    SHPCreateObject(int nSHPType, int nShapeId, int nParts,
                    const int *panPartStart, const int *panPartType,
                    int nVertices, const double *padfX, const double *padfY,
                    const double *padfZ, const double *padfM);
SHPObject SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(const SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

=======

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
>>>>>>> osgeo-main
    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> main
=======
=======

>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======

>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
=======

>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))

    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======

=======
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
=======

>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
=======

>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))

    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
    SHPCreateSimpleObject(int nSHPType, int nVertices, const double *padfX,
                          const double *padfY, const double *padfZ);

int SHPAPI_CALL SHPRewindObject(SHPHandle hSHP, SHPObject *psObject);

void SHPAPI_CALL SHPClose(SHPHandle hSHP);
void SHPAPI_CALL SHPWriteHeader(SHPHandle hSHP);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
const char SHPAPI_CALL1(*) SHPTypeName(int nSHPType);
const char SHPAPI_CALL1(*) SHPPartTypeName(int nPartType);

/* -------------------------------------------------------------------- */
/*      Shape quadtree indexing API.                                    */
/* -------------------------------------------------------------------- */

/* this can be two or four for binary or quad tree */
#define MAX_SUBNODE            4

/* upper limit of tree levels for automatic estimation */
#define MAX_DEFAULT_TREE_DEPTH 12

typedef struct shape_tree_node {
    /* region covered by this node */
    double adfBoundsMin[4];
    double adfBoundsMax[4];

    /* list of shapes stored at this node.  The papsShapeObj pointers
       or the whole list can be NULL */
    int nShapeCount;
    int *panShapeIds;
    SHPObject **papsShapeObj;

    int nSubNodes;
    struct shape_tree_node *apsSubNode[MAX_SUBNODE];

} SHPTreeNode;

typedef struct {
    SHPHandle hSHP;

    int nMaxDepth;
    int nDimension;
    int nTotalCount;

    SHPTreeNode *psRoot;
} SHPTree;

SHPTree SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
=======
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
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  const double *padfBoundsMin, const double *padfBoundsMax);
>>>>>>> osgeo-main
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
<<<<<<< HEAD
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);
=======
>>>>>>> osgeo-main

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);
=======
    SHPTreeFindLikelyShapes(const SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(const double *, const double *,
                                      const double *, const double *, int);
>>>>>>> osgeo-main

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

typedef struct SHPDiskTreeInfo *SHPTreeDiskHandle;

SHPTreeDiskHandle SHPAPI_CALL SHPOpenDiskTree(const char *pszQIXFilename,
<<<<<<< HEAD
                                              SAHooks *psHooks);
=======
                                              const SAHooks *psHooks);
>>>>>>> osgeo-main

void SHPAPI_CALL SHPCloseDiskTree(SHPTreeDiskHandle hDiskTree);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);
<<<<<<< HEAD

=======
=======
    SHPSearchDiskTreeEx(const SHPTreeDiskHandle hDiskTree,
                        double *padfBoundsMin, double *padfBoundsMax,
                        int *pnShapeCount);
>>>>>>> osgeo-main

=======

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))

    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)

    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*)

    SHPSearchDiskTree(FILE *fp, double *padfBoundsMin, double *padfBoundsMax,
                      int *pnShapeCount);

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))

    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)

    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*)

    SHPSearchDiskTree(FILE *fp, double *padfBoundsMin, double *padfBoundsMax,
                      int *pnShapeCount);

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
typedef struct SHPDiskTreeInfo *SHPTreeDiskHandle;

SHPTreeDiskHandle SHPAPI_CALL SHPOpenDiskTree(const char *pszQIXFilename,
                                              SAHooks *psHooks);

void SHPAPI_CALL SHPCloseDiskTree(SHPTreeDiskHandle hDiskTree);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
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
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

typedef struct SHPDiskTreeInfo *SHPTreeDiskHandle;

SHPTreeDiskHandle SHPAPI_CALL SHPOpenDiskTree(const char *pszQIXFilename,
                                              SAHooks *psHooks);

void SHPAPI_CALL SHPCloseDiskTree(SHPTreeDiskHandle hDiskTree);

int SHPAPI_CALL1(*)
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
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

=======
>>>>>>> osgeo-main
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

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
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))

    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)

    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*)

    SHPSearchDiskTree(FILE *fp, double *padfBoundsMin, double *padfBoundsMax,
                      int *pnShapeCount);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
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
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main

=======
>>>>>>> osgeo-main
=======
=======

>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)

    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*)

    SHPSearchDiskTree(FILE *fp, double *padfBoundsMin, double *padfBoundsMax,
                      int *pnShapeCount);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
typedef struct SHPDiskTreeInfo *SHPTreeDiskHandle;

SHPTreeDiskHandle SHPAPI_CALL SHPOpenDiskTree(const char *pszQIXFilename,
                                              SAHooks *psHooks);

void SHPAPI_CALL SHPCloseDiskTree(SHPTreeDiskHandle hDiskTree);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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

>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
=======

>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

<<<<<<< HEAD
int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
int SHPAPI_CALL1(*)

    SHPSearchDiskTree(FILE *fp, double *padfBoundsMin, double *padfBoundsMax,
                      int *pnShapeCount);

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
typedef struct SHPDiskTreeInfo *SHPTreeDiskHandle;

SHPTreeDiskHandle SHPAPI_CALL SHPOpenDiskTree(const char *pszQIXFilename,
                                              SAHooks *psHooks);

void SHPAPI_CALL SHPCloseDiskTree(SHPTreeDiskHandle hDiskTree);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======

=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======

=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD

=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======

=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

typedef struct SHPDiskTreeInfo *SHPTreeDiskHandle;

SHPTreeDiskHandle SHPAPI_CALL SHPOpenDiskTree(const char *pszQIXFilename,
                                              SAHooks *psHooks);

void SHPAPI_CALL SHPCloseDiskTree(SHPTreeDiskHandle hDiskTree);

int SHPAPI_CALL1(*)
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
int SHPAPI_CALL SHPWriteTreeLL(SHPTree *hTree, const char *pszFilename,
                               const SAHooks *psHooks);
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

=======
=======
=======

<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

<<<<<<< HEAD
<<<<<<< HEAD
int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);
=======
int SHPAPI_CALL1(*)

    SHPSearchDiskTree(FILE *fp, double *padfBoundsMin, double *padfBoundsMax,
                      int *pnShapeCount);
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))

=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======

    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)

    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*)

    SHPSearchDiskTree(FILE *fp, double *padfBoundsMin, double *padfBoundsMax,
                      int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======

    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)

    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*)

    SHPSearchDiskTree(FILE *fp, double *padfBoundsMin, double *padfBoundsMax,
                      int *pnShapeCount);

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
typedef struct SHPDiskTreeInfo *SHPTreeDiskHandle;

SHPTreeDiskHandle SHPAPI_CALL SHPOpenDiskTree(const char *pszQIXFilename,
                                              SAHooks *psHooks);

void SHPAPI_CALL SHPCloseDiskTree(SHPTreeDiskHandle hDiskTree);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
=======

=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

typedef struct SHPDiskTreeInfo *SHPTreeDiskHandle;

SHPTreeDiskHandle SHPAPI_CALL SHPOpenDiskTree(const char *pszQIXFilename,
                                              SAHooks *psHooks);

void SHPAPI_CALL SHPCloseDiskTree(SHPTreeDiskHandle hDiskTree);

int SHPAPI_CALL1(*)
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======

=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    SHPCreateTree(SHPHandle hSHP, int nDimension, int nMaxDepth,
                  double *padfBoundsMin, double *padfBoundsMax);
void SHPAPI_CALL SHPDestroyTree(SHPTree *hTree);

int SHPAPI_CALL SHPWriteTree(SHPTree *hTree, const char *pszFilename);

int SHPAPI_CALL SHPTreeAddShapeId(SHPTree *hTree, SHPObject *psObject);
int SHPAPI_CALL SHPTreeRemoveShapeId(SHPTree *hTree, int nShapeId);

void SHPAPI_CALL SHPTreeTrimExtraNodes(SHPTree *hTree);

int SHPAPI_CALL1(*)
    SHPTreeFindLikelyShapes(SHPTree *hTree, double *padfBoundsMin,
                            double *padfBoundsMax, int *);
int SHPAPI_CALL SHPCheckBoundsOverlap(double *, double *, double *, double *,
                                      int);

int SHPAPI_CALL1(*) SHPSearchDiskTree(FILE *fp, double *padfBoundsMin,
                                      double *padfBoundsMax, int *pnShapeCount);

typedef struct SHPDiskTreeInfo *SHPTreeDiskHandle;

SHPTreeDiskHandle SHPAPI_CALL SHPOpenDiskTree(const char *pszQIXFilename,
                                              SAHooks *psHooks);

void SHPAPI_CALL SHPCloseDiskTree(SHPTreeDiskHandle hDiskTree);

int SHPAPI_CALL1(*)
    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======

    SHPSearchDiskTreeEx(SHPTreeDiskHandle hDiskTree, double *padfBoundsMin,
                        double *padfBoundsMax, int *pnShapeCount);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
int SHPAPI_CALL SHPWriteTreeLL(SHPTree *hTree, const char *pszFilename,
                               SAHooks *psHooks);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

/* -------------------------------------------------------------------- */
/*      SBN Search API                                                  */
/* -------------------------------------------------------------------- */

typedef struct SBNSearchInfo *SBNSearchHandle;

SBNSearchHandle SHPAPI_CALL SBNOpenDiskTree(const char *pszSBNFilename,
<<<<<<< HEAD
<<<<<<< HEAD
                                            const SAHooks *psHooks);
=======
                                            SAHooks *psHooks);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
                                            SAHooks *psHooks);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL SBNCloseDiskTree(SBNSearchHandle hSBN);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
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
=======
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
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
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
    SBNSearchDiskTree(const SBNSearchHandle hSBN, const double *padfBoundsMin,
                      const double *padfBoundsMax, int *pnShapeCount);

int SHPAPI_CALL1(*)
    SBNSearchDiskTreeInteger(const SBNSearchHandle hSBN, int bMinX, int bMinY,
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))

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
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======

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
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
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
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    SBNSearchDiskTree(SBNSearchHandle hSBN, double *padfBoundsMin,
                      double *padfBoundsMax, int *pnShapeCount);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

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
=======
<<<<<<< HEAD
>>>>>>> main
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======

>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======

<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======

<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

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
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======
=======
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======
>>>>>>> osgeo-main
=======
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======
>>>>>>> osgeo-main
=======
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======
>>>>>>> osgeo-main

=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======

>>>>>>> osgeo-main
=======
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======

>>>>>>> osgeo-main
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
=======

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
    SBNSearchDiskTree(SBNSearchHandle hSBN, double *padfBoundsMin,
                      double *padfBoundsMax, int *pnShapeCount);

int SHPAPI_CALL1(*)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))

=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
    SBNSearchDiskTree(SBNSearchHandle hSBN, double *padfBoundsMin,
                      double *padfBoundsMax, int *pnShapeCount);

int SHPAPI_CALL1(*)
<<<<<<< HEAD

    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======

=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======

>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

=======

>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))

    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

<<<<<<< HEAD
<<<<<<< HEAD
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
    SBNSearchDiskTreeInteger(SBNSearchHandle hSBN, int bMinX, int bMinY,
                             int bMaxX, int bMaxY, int *pnShapeCount);

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
void SHPAPI_CALL SBNSearchFreeIds(int *panShapeId);

/************************************************************************/
/*                             DBF Support.                             */

/************************************************************************/
typedef struct {
    SAHooks sHooks;

    SAFile fp;

    int nRecords;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    int nRecordLength; /* Must fit on uint16 */
    int nHeaderLength; /* File header length (32) + field
                          descriptor length + spare space.
                          Must fit on uint16 */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> main
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
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
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
    int nRecordLength;
    int nHeaderLength;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
    int nRecordLength;
    int nHeaderLength;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    int nRecordLength;
    int nHeaderLength;
=======
    int nRecordLength;
    int nHeaderLength;
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
    int nRecordLength; /* Must fit on uint16 */
    int nHeaderLength; /* File header length (32) + field
                          descriptor length + spare space.
                          Must fit on uint16 */
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
    int nRecordLength;
    int nHeaderLength;
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
    int nRecordLength;
    int nHeaderLength;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
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
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
    int nRecordLength;
    int nHeaderLength;
=======
    int nRecordLength; /* Must fit on uint16 */
    int nHeaderLength; /* File header length (32) + field
                          descriptor length + spare space.
                          Must fit on uint16 */
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    int nFields;
    int *panFieldOffset;
    int *panFieldSize;
    int *panFieldDecimals;
    char *pachFieldType;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    char *pszHeader; /* Field descriptors */
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    char *pszHeader; /* Field descriptors */
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
=======
    char *pszHeader; /* Field descriptors */
=======
>>>>>>> osgeo-main
    char *pszHeader;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    char *pszHeader;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    char *pszHeader; /* Field descriptors */
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
    char *pszHeader;
=======
    char *pszHeader; /* Field descriptors */
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
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
    char *pszHeader; /* Field descriptors */
=======
    char *pszHeader;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    char *pszHeader;
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
    char *pszHeader; /* Field descriptors */
=======
    char *pszHeader;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    char *pszHeader;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
    char *pszHeader; /* Field descriptors */
=======
    char *pszHeader;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    char *pszHeader;
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
    char *pszHeader; /* Field descriptors */
=======
    char *pszHeader;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    char *pszHeader;
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
    char *pszHeader;
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
    char *pszHeader;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    char *pszHeader; /* Field descriptors */
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
    char *pszHeader;
=======
    char *pszHeader; /* Field descriptors */
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    char *pszHeader;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
    char *pszHeader;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
=======
    char *pszHeader;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))

    int nCurrentRecord;
    int bCurrentRecordModified;
    char *pszCurrentRecord;

    int nWorkFieldLength;
    char *pszWorkField;

    int bNoHeader;
    int bUpdated;

    union {
        double dfDoubleField;
        int nIntField;
    } fieldValue;

    int iLanguageDriver;
    char *pszCodePage;

    int nUpdateYearSince1900; /* 0-255 */
    int nUpdateMonth;         /* 1-12 */
    int nUpdateDay;           /* 1-31 */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
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
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))

    int bWriteEndOfFileChar; /* defaults to TRUE */

    int bRequireNextWriteSeek;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
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
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
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
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
} DBFInfo;

typedef DBFInfo *DBFHandle;

typedef enum {
    FTString,
    FTInteger,
    FTDouble,
    FTLogical,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
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
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
    FTDate,
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> main
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
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
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
    FTInvalid
} DBFFieldType;

#define XBASE_FLDHDR_SZ 32
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    FTDate,
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
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
=======
<<<<<<< HEAD
>>>>>>> main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> main
=======
=======
=======
=======
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                const SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage,
                                  const SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(const DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(const DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, const int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(const DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(const DBFHandle psDBF,
                                 const char *pszFieldName);

=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
<<<<<<< HEAD
>>>>>>> osgeo-main

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
<<<<<<< HEAD
>>>>>>> osgeo-main

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
>>>>>>> osgeo-main

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
>>>>>>> osgeo-main

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
>>>>>>> osgeo-main

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
>>>>>>> osgeo-main

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
>>>>>>> osgeo-main

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
>>>>>>> osgeo-main

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
    FTInvalid
} DBFFieldType;

#define XBASE_FLDHDR_SZ 32
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    FTDate,
    FTInvalid
} DBFFieldType;

<<<<<<< HEAD
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
=======
    FTDate,
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
    FTInvalid
} DBFFieldType;

/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    FTInvalid
} DBFFieldType;

#define XBASE_FLDHDR_SZ 32
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    FTDate,
    FTInvalid
} DBFFieldType;

=======
    FTInvalid
} DBFFieldType;

>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
    FTInvalid
} DBFFieldType;

>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
/* Field descriptor/header size */
#define XBASE_FLDHDR_SZ         32
/* Shapelib read up to 11 characters, even if only 10 should normally be used */
#define XBASE_FLDNAME_LEN_READ  11
/* On writing, we limit to 10 characters */
#define XBASE_FLDNAME_LEN_WRITE 10
/* Normally only 254 characters should be used. We tolerate 255 historically */
#define XBASE_FLD_MAX_WIDTH     255
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))

DBFHandle SHPAPI_CALL DBFOpen(const char *pszDBFFile, const char *pszAccess);
DBFHandle SHPAPI_CALL DBFOpenLL(const char *pszDBFFile, const char *pszAccess,
                                SAHooks *psHooks);
DBFHandle SHPAPI_CALL DBFCreate(const char *pszDBFFile);
DBFHandle SHPAPI_CALL DBFCreateEx(const char *pszDBFFile,
                                  const char *pszCodePage);
DBFHandle SHPAPI_CALL DBFCreateLL(const char *pszDBFFile,
                                  const char *pszCodePage, SAHooks *psHooks);

int SHPAPI_CALL DBFGetFieldCount(DBFHandle psDBF);
int SHPAPI_CALL DBFGetRecordCount(DBFHandle psDBF);
int SHPAPI_CALL DBFAddField(DBFHandle hDBF, const char *pszFieldName,
                            DBFFieldType eType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFAddNativeFieldType(DBFHandle hDBF, const char *pszFieldName,
                                      char chType, int nWidth, int nDecimals);

int SHPAPI_CALL DBFDeleteField(DBFHandle hDBF, int iField);

int SHPAPI_CALL DBFReorderFields(DBFHandle psDBF, int *panMap);

int SHPAPI_CALL DBFAlterFieldDefn(DBFHandle psDBF, int iField,
                                  const char *pszFieldName, char chType,
                                  int nWidth, int nDecimals);

DBFFieldType SHPAPI_CALL DBFGetFieldInfo(DBFHandle psDBF, int iField,
                                         char *pszFieldName, int *pnWidth,
                                         int *pnDecimals);

int SHPAPI_CALL DBFGetFieldIndex(DBFHandle psDBF, const char *pszFieldName);

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
int SHPAPI_CALL DBFReadIntegerAttribute(DBFHandle hDBF, int iShape, int iField);
double SHPAPI_CALL DBFReadDoubleAttribute(DBFHandle hDBF, int iShape,
                                          int iField);
const char SHPAPI_CALL1(*)
    DBFReadStringAttribute(DBFHandle hDBF, int iShape, int iField);
const char SHPAPI_CALL1(*)
    DBFReadLogicalAttribute(DBFHandle hDBF, int iShape, int iField);
<<<<<<< HEAD
<<<<<<< HEAD
SHPDate SHPAPI_CALL DBFReadDateAttribute(DBFHandle hDBF, int iShape,
                                         int iField);
int SHPAPI_CALL DBFIsAttributeNULL(const DBFHandle hDBF, int iShape,
                                   int iField);
=======
int SHPAPI_CALL DBFIsAttributeNULL(DBFHandle hDBF, int iShape, int iField);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
int SHPAPI_CALL DBFIsAttributeNULL(DBFHandle hDBF, int iShape, int iField);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

int SHPAPI_CALL DBFWriteIntegerAttribute(DBFHandle hDBF, int iShape, int iField,
                                         int nFieldValue);
int SHPAPI_CALL DBFWriteDoubleAttribute(DBFHandle hDBF, int iShape, int iField,
                                        double dFieldValue);
int SHPAPI_CALL DBFWriteStringAttribute(DBFHandle hDBF, int iShape, int iField,
                                        const char *pszFieldValue);
int SHPAPI_CALL DBFWriteNULLAttribute(DBFHandle hDBF, int iShape, int iField);

int SHPAPI_CALL DBFWriteLogicalAttribute(DBFHandle hDBF, int iShape, int iField,
                                         const char lFieldValue);
<<<<<<< HEAD
<<<<<<< HEAD
int SHPAPI_CALL DBFWriteDateAttribute(DBFHandle hDBF, int iShape, int iField,
                                      const SHPDate *dateFieldValue);
int SHPAPI_CALL DBFWriteAttributeDirectly(DBFHandle psDBF, int hEntity,
                                          int iField, const void *pValue);
const char SHPAPI_CALL1(*) DBFReadTuple(DBFHandle psDBF, int hEntity);
int SHPAPI_CALL DBFWriteTuple(DBFHandle psDBF, int hEntity,
                              const void *pRawTuple);

int SHPAPI_CALL DBFIsRecordDeleted(const DBFHandle psDBF, int iShape);
int SHPAPI_CALL DBFMarkRecordDeleted(DBFHandle psDBF, int iShape,
                                     int bIsDeleted);

DBFHandle SHPAPI_CALL DBFCloneEmpty(const DBFHandle psDBF,
                                    const char *pszFilename);

void SHPAPI_CALL DBFClose(DBFHandle hDBF);
void SHPAPI_CALL DBFUpdateHeader(DBFHandle hDBF);
char SHPAPI_CALL DBFGetNativeFieldType(const DBFHandle hDBF, int iField);

const char SHPAPI_CALL1(*) DBFGetCodePage(const DBFHandle psDBF);

void SHPAPI_CALL DBFSetLastModifiedDate(DBFHandle psDBF, int nYYSince1900,
                                        int nMM, int nDD);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> osgeo-main
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
int SHPAPI_CALL DBFWriteAttributeDirectly(DBFHandle psDBF, int hEntity,
                                          int iField, void *pValue);
const char SHPAPI_CALL1(*) DBFReadTuple(DBFHandle psDBF, int hEntity);
int SHPAPI_CALL DBFWriteTuple(DBFHandle psDBF, int hEntity, void *pRawTuple);

int SHPAPI_CALL DBFIsRecordDeleted(DBFHandle psDBF, int iShape);
int SHPAPI_CALL DBFMarkRecordDeleted(DBFHandle psDBF, int iShape,
                                     int bIsDeleted);

DBFHandle SHPAPI_CALL DBFCloneEmpty(DBFHandle psDBF, const char *pszFilename);

void SHPAPI_CALL DBFClose(DBFHandle hDBF);
void SHPAPI_CALL DBFUpdateHeader(DBFHandle hDBF);
char SHPAPI_CALL DBFGetNativeFieldType(DBFHandle hDBF, int iField);

const char SHPAPI_CALL1(*) DBFGetCodePage(DBFHandle psDBF);

void SHPAPI_CALL DBFSetLastModifiedDate(DBFHandle psDBF, int nYYSince1900,
                                        int nMM, int nDD);
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
int SHPAPI_CALL DBFWriteAttributeDirectly(DBFHandle psDBF, int hEntity,
                                          int iField, void *pValue);
const char SHPAPI_CALL1(*) DBFReadTuple(DBFHandle psDBF, int hEntity);
int SHPAPI_CALL DBFWriteTuple(DBFHandle psDBF, int hEntity, void *pRawTuple);

int SHPAPI_CALL DBFIsRecordDeleted(DBFHandle psDBF, int iShape);
int SHPAPI_CALL DBFMarkRecordDeleted(DBFHandle psDBF, int iShape,
                                     int bIsDeleted);

DBFHandle SHPAPI_CALL DBFCloneEmpty(DBFHandle psDBF, const char *pszFilename);

void SHPAPI_CALL DBFClose(DBFHandle hDBF);
void SHPAPI_CALL DBFUpdateHeader(DBFHandle hDBF);
char SHPAPI_CALL DBFGetNativeFieldType(DBFHandle hDBF, int iField);

const char SHPAPI_CALL1(*) DBFGetCodePage(DBFHandle psDBF);

void SHPAPI_CALL DBFSetLastModifiedDate(DBFHandle psDBF, int nYYSince1900,
                                        int nMM, int nDD);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
<<<<<<< HEAD
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======

void SHPAPI_CALL DBFSetWriteEndOfFileChar(DBFHandle psDBF, int bWriteFlag);
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))

#ifdef __cplusplus
}
#endif

#endif /* ndef SHAPEFILE_H_INCLUDED */
