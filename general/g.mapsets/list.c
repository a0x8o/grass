#include <string.h>
#include <stdio.h>
#include <grass/gis.h>
#include <grass/glocale.h>
#include "local_proto.h"
#include <grass/parson.h>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void list_available_mapsets(const char **mapset_name, int nmapsets,
                            const char *fs)
{
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
// Function to initialize a JSON object with a mapsets array
static JSON_Object *initialize_json_object(void)
{
    JSON_Value *root_value = json_value_init_object();
    if (!root_value) {
        G_fatal_error(_("Failed to initialize JSON object. Out of memory?"));
=======
void list_available_mapsets(const char **mapset_name, int nmapsets,
                            const char *fs)
{
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
    int n;

    G_message(_("Available mapsets:"));

    for (n = 0; n < nmapsets; n++) {
        fprintf(stdout, "%s", mapset_name[n]);
        if (n < nmapsets - 1) {
            if (strcmp(fs, "newline") == 0)
                fprintf(stdout, "\n");
            else if (strcmp(fs, "space") == 0)
                fprintf(stdout, " ");
            else if (strcmp(fs, "comma") == 0)
                fprintf(stdout, ",");
            else if (strcmp(fs, "tab") == 0)
                fprintf(stdout, "\t");
            else
                fprintf(stdout, "%s", fs);
        }
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    }

    JSON_Object *root_object = json_value_get_object(root_value);
    json_object_set_value(root_object, "mapsets", json_value_init_array());

    JSON_Array *mapsets = json_object_get_array(root_object, "mapsets");
    if (!mapsets) {
        json_value_free(root_value);
        G_fatal_error(_("Failed to initialize mapsets array. Out of memory?"));
    }

    return root_object;
}

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
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
// Function to serialize and print JSON object
static void serialize_and_print_json_object(JSON_Value *root_value)
{
    char *serialized_string = json_serialize_to_string_pretty(root_value);
    if (!serialized_string) {
        json_value_free(root_value);
        G_fatal_error(_("Failed to serialize JSON to pretty format."));
    }

    fprintf(stdout, "%s\n", serialized_string);
    json_free_serialized_string(serialized_string);
    json_value_free(root_value);
}

void list_available_mapsets(const char **mapset_name, int nmapsets,
                            const char *fs)
{
    G_message(_("Available mapsets:"));

    for (int n = 0; n < nmapsets; n++) {
        fprintf(stdout, "%s", mapset_name[n]);
        if (n < nmapsets - 1) {
            fprintf(stdout, "%s", fs);
=======
void list_available_mapsets(const char **mapset_name, int nmapsets,
                            const char *fs)
{
    int n;

    G_message(_("Available mapsets:"));

    for (n = 0; n < nmapsets; n++) {
        fprintf(stdout, "%s", mapset_name[n]);
        if (n < nmapsets - 1) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
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
void list_accessible_mapsets(const char *fs)
{
    int n;
    const char *name;

    G_message(_("Accessible mapsets:"));
    for (n = 0; (name = G_get_mapset_name(n)); n++) {
        /* match each mapset to its numeric equivalent */
        fprintf(stdout, "%s", name);
        if (G_get_mapset_name(n + 1)) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
            if (strcmp(fs, "newline") == 0)
                fprintf(stdout, "\n");
            else if (strcmp(fs, "space") == 0)
                fprintf(stdout, " ");
            else if (strcmp(fs, "comma") == 0)
                fprintf(stdout, ",");
            else if (strcmp(fs, "tab") == 0)
                fprintf(stdout, "\t");
            else
                fprintf(stdout, "%s", fs);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        }
    }
    fprintf(stdout, "\n");
}

void list_accessible_mapsets(const char *fs)
{
    const char *name;

    G_message(_("Accessible mapsets:"));

    for (int n = 0; (name = G_get_mapset_name(n)); n++) {
        /* match each mapset to its numeric equivalent */
        fprintf(stdout, "%s", name);
        if (G_get_mapset_name(n + 1)) {
<<<<<<< HEAD
            fprintf(stdout, "%s", fs);
=======
            if (strcmp(fs, "newline") == 0)
                fprintf(stdout, "\n");
            else if (strcmp(fs, "space") == 0)
                fprintf(stdout, " ");
            else if (strcmp(fs, "comma") == 0)
                fprintf(stdout, ",");
            else if (strcmp(fs, "tab") == 0)
                fprintf(stdout, "\t");
            else
                fprintf(stdout, "%s", fs);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
        }
    }
    fprintf(stdout, "\n");
}

// Lists all accessible mapsets in JSON format
void list_accessible_mapsets_json(void)
{
    const char *name;
    JSON_Object *root_object = initialize_json_object();
    JSON_Array *mapsets = json_object_get_array(root_object, "mapsets");

    for (int n = 0; (name = G_get_mapset_name(n)); n++) {
        json_array_append_string(mapsets, name);
    }

    serialize_and_print_json_object(
        json_object_get_wrapping_value(root_object));
}

// Lists available mapsets from a provided array in JSON format
void list_avaliable_mapsets_json(const char **mapset_names, int nmapsets)
{
    JSON_Object *root_object = initialize_json_object();
    JSON_Array *mapsets = json_object_get_array(root_object, "mapsets");

    for (int n = 0; n < nmapsets; n++) {
        json_array_append_string(mapsets, mapset_names[n]);
    }

    serialize_and_print_json_object(
        json_object_get_wrapping_value(root_object));
}
