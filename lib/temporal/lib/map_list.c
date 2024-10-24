/*****************************************************************************
 *
 * MODULE:       gis library
 *
 * AUTHOR(S):    Original author CERL, probably Dave Gerdes.
 *               Update to GRASS 5.7 Radim Blazek.
 *
 * PURPOSE:      Lower level functions for reading and manipulating integer list
 *
 * COPYRIGHT:    (C) 2001 by the GRASS Development Team
 *
 *               This program is free software under the GNU General Public
 *               License (>=v2). Read the file COPYING that comes with GRASS
 *               for details.
 *
 *****************************************************************************/

#include <stdlib.h>
#include <grass/gis.h>
#include <grass/temporal.h>

/**
 * \brief Free allocated memory of an integer list
 *
 * \param list The pointer to an integer list
 *
 * */
void tgis_free_map_list(tgisMapList *list)
{
    if (list->values) {
        int i;

        for (i = 0; i < list->n_values; i++) {
            if (list->values[i]->name)
                G_free(list->values[i]->name);
            if (list->values[i]->mapset)
                G_free(list->values[i]->mapset);
            G_free(list->values[i]);
        }
        G_free(list->values);
    }
    G_free(list);
}

/**
 * \brief Return a new integer list.
 *
 * G_fatal_error() will be invoked by the
 * allocation function.
 *
 * \return list The pointer to a new allocated integer list
 *
 * */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
tgisMapList *tgis_new_map_list(void)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
tgisMapList *tgis_new_map_list(void)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
=======
tgisMapList *tgis_new_map_list(void)
=======
>>>>>>> osgeo-main
tgisMapList *tgis_new_map_list()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
tgisMapList *tgis_new_map_list()
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
tgisMapList *tgis_new_map_list(void)
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
tgisMapList *tgis_new_map_list()
=======
tgisMapList *tgis_new_map_list(void)
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
tgisMapList *tgis_new_map_list(void)
=======
tgisMapList *tgis_new_map_list()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
tgisMapList *tgis_new_map_list()
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
tgisMapList *tgis_new_map_list(void)
=======
tgisMapList *tgis_new_map_list()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
tgisMapList *tgis_new_map_list()
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
tgisMapList *tgis_new_map_list(void)
=======
tgisMapList *tgis_new_map_list()
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
tgisMapList *tgis_new_map_list()
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
{
    tgisMapList *list = G_malloc(sizeof(tgisMapList));

    list->values = NULL;
    tgis_init_map_list(list);
    return list;
}

/**
 * \brief Init a tgisMapList and free allocated memory
 *
 * \param list The pointer to a tgisMapList
 *
 * */
void tgis_init_map_list(tgisMapList *list)
{
    if (list->values) {
        int i;

        for (i = 0; i < list->n_values; i++) {
            if (list->values[i]->name)
                G_free(list->values[i]->name);
            if (list->values[i]->mapset)
                G_free(list->values[i]->mapset);
            G_free(list->values[i]);
        }
        G_free(list->values);
    }

    list->values = NULL;
    list->n_values = 0;
    list->alloc_values = 0;
}

/**
 * \brief Add a map to tgisMapList
 *
 * This function adds a tgisMap to the list but does not check for duplicates.
 * In case reallocation fails, G_fatal_error() will be invoked by the
 * allocation function.
 *
 * The content of the map will not be copied, the pointer
 *to the map will be stored.
 *
 * \param list The tgisMapList pointer
 * \param map A pointer to a tgisMap struct that should be added
 *
 * */
void tgis_map_list_add(tgisMapList *list, tgisMap *map)
{
    if (list->n_values == list->alloc_values) {
        size_t size = (list->n_values + 1000) * sizeof(tgisMap *);
        void *p = G_realloc((void *)list->values, size);

        list->values = (tgisMap **)p;
        list->alloc_values = list->n_values + 1000;
    }

    list->values[list->n_values] = map;
    list->n_values++;
}

/**
 * \brief Insert map information into tgisMapList
 *
 * This function allocates a tgisMap, fills it with the provided information
 * and adds it to the list.
 * In case allocation fails, G_fatal_error() will be invoked by the
 * allocation function.
 *
 * All arguments are deep copied to the new allocated tgisMap struct.
 *
 * \param list The tgisMapList pointer
 * \param name The name of the map
 * \param mapset The name of the mapset
 * \param ts A pointer to the timestamp of the map
 *
 * */
void tgis_map_list_insert(tgisMapList *list, char *name, char *mapset,
                          struct TimeStamp *ts)
{
    tgisMap *map = G_calloc(1, sizeof(tgisMap));

    map->name = G_store(name);
    map->mapset = G_store(mapset);

    if (ts->count == 1)
        G_set_timestamp(&(map->ts), &(ts->dt[0]));
    if (ts->count == 2)
        G_set_timestamp_range(&(map->ts), &(ts->dt[0]), &(ts->dt[1]));

    tgis_map_list_add(list, map);
}
