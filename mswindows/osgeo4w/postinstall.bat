set ICON=%OSGEO4W_ROOT%\apps\grass\grass@POSTFIX@\gui\icons\grass_osgeo.ico
set BATCH=%OSGEO4W_ROOT%\bin\@GRASS_EXECUTABLE@.bat
textreplace -std -t "%BATCH%"
textreplace -std -t "%OSGEO4W_ROOT%\apps\grass\grass@POSTFIX@\etc\fontcap"

for /F "tokens=* USEBACKQ" %%F IN (`getspecialfolder Documents`) do set DOCUMENTS=%%F

if not %OSGEO4W_MENU_LINKS%==0 xxmklink "%OSGEO4W_STARTMENU%\GRASS GIS @VERSION@.lnk" "%BATCH%"  "--gui" "%DOCUMENTS%" "Launch GRASS GIS @VERSION@" 1 "%ICON%" 
if not %OSGEO4W_DESKTOP_LINKS%==0 xxmklink "%OSGEO4W_DESKTOP%\GRASS GIS @VERSION@.lnk" "%BATCH%"  "--gui" "%DOCUMENTS%" "Launch GRASS GIS @VERSION@" 1 "%ICON%" 

rem run g.mkfontcap outside a GRASS session during
rem an OSGeo4W installation for updating paths to fonts

rem set gisbase
set GISBASE=%OSGEO4W_ROOT%\apps\grass\grass@POSTFIX@

rem set path to freetype dll and its dependencies
set FREETYPEBASE=%OSGEO4W_ROOT%\bin;%OSGEO4W_ROOT%\apps\msys\bin;%GISBASE%\lib

rem set dependencies to path
set PATH=%FREETYPEBASE%;%PATH%

rem GISRC must be set
set GISRC=dummy

rem run g.mkfontcap outside a GRASS session
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
"%GISBASE%\bin\g.mkfontcap.exe" -o
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
"%GISBASE%\bin\g.mkfontcap.exe" --overwrite
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
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
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
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
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
"%GISBASE%\bin\g.mkfontcap.exe" -o
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main

del "%BATCH%.tmpl
