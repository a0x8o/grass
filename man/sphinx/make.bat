@ECHO OFF

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set BUILDDIR=_build
set ALLSPHINXOPTS=-d %BUILDDIR%/doctrees %SPHINXOPTS% .
set I18NSPHINXOPTS=%SPHINXOPTS% .
if NOT "%PAPER%" == "" (
	set ALLSPHINXOPTS=-D latex_paper_size=%PAPER% %ALLSPHINXOPTS%
	set I18NSPHINXOPTS=-D latex_paper_size=%PAPER% %I18NSPHINXOPTS%
)

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  html       to make standalone HTML files
	echo.  dirhtml    to make HTML files named index.html in directories
	echo.  singlehtml to make a single large HTML file
	echo.  pickle     to make pickle files
	echo.  json       to make JSON files
	echo.  htmlhelp   to make HTML files and a HTML help project
	echo.  qthelp     to make HTML files and a qthelp project
	echo.  devhelp    to make HTML files and a Devhelp project
	echo.  epub       to make an epub
	echo.  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter
	echo.  text       to make text files
	echo.  man        to make manual pages
	echo.  texinfo    to make Texinfo files
	echo.  gettext    to make PO message catalogs
	echo.  changes    to make an overview over all changed/added/deprecated items
	echo.  linkcheck  to check all external links for integrity
	echo.  doctest    to run all doctests embedded in the documentation if enabled
	goto end
)

if "%1" == "clean" (
	for /d %%i in (%BUILDDIR%\*) do rmdir /q /s %%i
	del /q /s %BUILDDIR%\*
	goto end
)

if "%1" == "html" (
	%SPHINXBUILD% -b html %ALLSPHINXOPTS% %BUILDDIR%/html
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/html.
	goto end
)

if "%1" == "dirhtml" (
	%SPHINXBUILD% -b dirhtml %ALLSPHINXOPTS% %BUILDDIR%/dirhtml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/dirhtml.
	goto end
)

if "%1" == "singlehtml" (
	%SPHINXBUILD% -b singlehtml %ALLSPHINXOPTS% %BUILDDIR%/singlehtml
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The HTML pages are in %BUILDDIR%/singlehtml.
	goto end
)

if "%1" == "pickle" (
	%SPHINXBUILD% -b pickle %ALLSPHINXOPTS% %BUILDDIR%/pickle
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can process the pickle files.
	goto end
)

if "%1" == "json" (
	%SPHINXBUILD% -b json %ALLSPHINXOPTS% %BUILDDIR%/json
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can process the JSON files.
	goto end
)

if "%1" == "htmlhelp" (
	%SPHINXBUILD% -b htmlhelp %ALLSPHINXOPTS% %BUILDDIR%/htmlhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can run HTML Help Workshop with the ^
.hhp project file in %BUILDDIR%/htmlhelp.
	goto end
)

if "%1" == "qthelp" (
	%SPHINXBUILD% -b qthelp %ALLSPHINXOPTS% %BUILDDIR%/qthelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; now you can run "qcollectiongenerator" with the ^
.qhcp project file in %BUILDDIR%/qthelp, like this:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS83Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS83Documentation.ghc
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
=======
>>>>>>> main
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS83Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS83Documentation.ghc
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
<<<<<<< HEAD
>>>>>>> osgeo-main
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
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\grass_gis.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\grass_gis.ghc
=======
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS80Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS80Documentation.ghc
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
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<<<<<<< HEAD
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b603a5c6bb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2cd2b6c6fa (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 4dd6d0bd5b (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8c79884a51 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
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
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3777db3c7d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cb1dcf9f32 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 5eec7c15bf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 301e8b1961 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fac409e8c0 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2d98a74fb2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS80Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS80Documentation.ghc
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> c06a348ee6 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 703672315e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa1b49d230 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1e589bfdb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3a05fedbc9 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> adeb201999 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2c0d04b22e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 3725fe2da2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 4202a1e605 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dcd1c3ec53 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0779700f84 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
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
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS83Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS83Documentation.ghc
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
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS83Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS83Documentation.ghc
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
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS80Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS80Documentation.ghc
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 32b99b60b3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS80Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS80Documentation.ghc
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS83Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS83Documentation.ghc
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
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
	echo.^> qcollectiongenerator %BUILDDIR%\qthelp\GRASS83Documentation.qhcp
	echo.To view the help file:
	echo.^> assistant -collectionFile %BUILDDIR%\qthelp\GRASS83Documentation.ghc
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
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<<<<<<< HEAD
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
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 182ae4a08e (Programmer's manual: update GRASS GIS arch drawing (#1610))
	goto end
)

if "%1" == "devhelp" (
	%SPHINXBUILD% -b devhelp %ALLSPHINXOPTS% %BUILDDIR%/devhelp
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished.
	goto end
)

if "%1" == "epub" (
	%SPHINXBUILD% -b epub %ALLSPHINXOPTS% %BUILDDIR%/epub
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The epub file is in %BUILDDIR%/epub.
	goto end
)

if "%1" == "latex" (
	%SPHINXBUILD% -b latex %ALLSPHINXOPTS% %BUILDDIR%/latex
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished; the LaTeX files are in %BUILDDIR%/latex.
	goto end
)

if "%1" == "text" (
	%SPHINXBUILD% -b text %ALLSPHINXOPTS% %BUILDDIR%/text
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The text files are in %BUILDDIR%/text.
	goto end
)

if "%1" == "man" (
	%SPHINXBUILD% -b man %ALLSPHINXOPTS% %BUILDDIR%/man
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The manual pages are in %BUILDDIR%/man.
	goto end
)

if "%1" == "texinfo" (
	%SPHINXBUILD% -b texinfo %ALLSPHINXOPTS% %BUILDDIR%/texinfo
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The Texinfo files are in %BUILDDIR%/texinfo.
	goto end
)

if "%1" == "gettext" (
	%SPHINXBUILD% -b gettext %I18NSPHINXOPTS% %BUILDDIR%/locale
	if errorlevel 1 exit /b 1
	echo.
	echo.Build finished. The message catalogs are in %BUILDDIR%/locale.
	goto end
)

if "%1" == "changes" (
	%SPHINXBUILD% -b changes %ALLSPHINXOPTS% %BUILDDIR%/changes
	if errorlevel 1 exit /b 1
	echo.
	echo.The overview file is in %BUILDDIR%/changes.
	goto end
)

if "%1" == "linkcheck" (
	%SPHINXBUILD% -b linkcheck %ALLSPHINXOPTS% %BUILDDIR%/linkcheck
	if errorlevel 1 exit /b 1
	echo.
	echo.Link check complete; look for any errors in the above output ^
or in %BUILDDIR%/linkcheck/output.txt.
	goto end
)

if "%1" == "doctest" (
	%SPHINXBUILD% -b doctest %ALLSPHINXOPTS% %BUILDDIR%/doctest
	if errorlevel 1 exit /b 1
	echo.
	echo.Testing of doctests in the sources finished, look at the ^
results in %BUILDDIR%/doctest/output.txt.
	goto end
)

:end
