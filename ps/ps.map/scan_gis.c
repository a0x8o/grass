#include <unistd.h>
#include <string.h>
#include <grass/gis.h>
#include "local_proto.h"

int scan_gis(char *element, char *desc, char *key, char *data, char *name,
             char *mapset, int gobble)
{
    const char *ms;

    *mapset = 0;
    if (sscanf(data, "%s %s", name, mapset) < 1) {
        error(key, data, "illegal request (scan_gis)");
        if (gobble)
            gobble_input();
        return 0;
    }

    if (strcmp(name, "list") == 0) {
        if (isatty(0))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
            G_list_element(element, desc, mapset, NULL);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            G_list_element(element, desc, mapset, NULL);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
=======
            G_list_element(element, desc, mapset, NULL);
=======
>>>>>>> osgeo-main
            G_list_element(element, desc, mapset, (int (*)())NULL);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
            G_list_element(element, desc, mapset, (int (*)())NULL);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
            G_list_element(element, desc, mapset, NULL);
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
            G_list_element(element, desc, mapset, (int (*)())NULL);
=======
            G_list_element(element, desc, mapset, NULL);
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
            G_list_element(element, desc, mapset, NULL);
=======
            G_list_element(element, desc, mapset, (int (*)())NULL);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            G_list_element(element, desc, mapset, (int (*)())NULL);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
            G_list_element(element, desc, mapset, NULL);
=======
            G_list_element(element, desc, mapset, (int (*)())NULL);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            G_list_element(element, desc, mapset, (int (*)())NULL);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
            G_list_element(element, desc, mapset, NULL);
=======
            G_list_element(element, desc, mapset, (int (*)())NULL);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
            G_list_element(element, desc, mapset, (int (*)())NULL);
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
        reject();
        return 0;
    }

    ms = G_find_file2(element, name, mapset);
    if (ms == NULL) {
        error(key, data, "not found");
        if (gobble)
            gobble_input();
        return 0;
    }
    strcpy(mapset, ms);
    return 1;
}
