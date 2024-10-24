#include <stdlib.h>

#include <grass/gis.h>
#include <grass/glocale.h>

#include "local_proto.h"

void parse_args(int argc, char **argv, struct _options *options,
                struct _flags *flags)
{
    options->dsn = G_define_option();
    options->dsn->key = "input";
    options->dsn->type = TYPE_STRING;
    options->dsn->label = _("Name of input OGR or PostGIS data source");
    options->dsn->description =
        _("Examples:\n"
          "\t\tESRI Shapefile: directory containing a shapefile\n"
          "\t\tMapInfo File: directory containing a mapinfo file\n"
          "\t\tPostGIS database: connection string, eg. 'PG:dbname=db "
          "user=grass'");
    options->dsn->required = YES;
    options->dsn->gisprompt = "old,datasource,datasource";

    options->layer = G_define_option();
    options->layer->key = "layer";
    options->layer->type = TYPE_STRING;
    options->layer->required = NO;
    options->layer->multiple = NO;
    options->layer->label =
        _("Name of OGR layer or PostGIS feature table to be linked");
    options->layer->description = _("Examples:\n"
                                    "\t\tESRI Shapefile: shapefile name\n"
                                    "\t\tMapInfo File: mapinfo file name\n"
                                    "\t\tPostGIS database: table name");
    options->layer->key_desc = "name";
    options->layer->gisprompt = "old,datasource_layer,datasource_layer";

    options->where = G_define_standard_option(G_OPT_DB_WHERE);

    options->output = G_define_standard_option(G_OPT_V_OUTPUT);
    options->output->required = NO;
    options->output->description =
        _("Name for output GRASS vector map (default: input layer)");

    flags->override = G_define_flag();
    flags->override->key = 'o';
    flags->override->label =
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        _("Override projection check (use current location's projection)");
    flags->override->description = _("Assume that the dataset has the same "
                                     "projection as the current location");
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
        _("Override projection check (use current project's CRS)");
    flags->override->description =
        _("Assume that the dataset has the same "
          "coordinate reference system as the current project");
=======
        _("Override projection check (use current location's projection)");
    flags->override->description = _("Assume that the dataset has the same "
                                     "projection as the current location");
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
        _("Override projection check (use current location's projection)");
    flags->override->description = _("Assume that the dataset has the same "
                                     "projection as the current location");
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

    flags->proj = G_define_flag();
    flags->proj->key = 'j';
    flags->proj->description = _("Perform projection check only and exit");

    flags->format = G_define_flag();
    flags->format->key = 'f';
    flags->format->description = _("List supported formats and exit");
    flags->format->guisection = _("Print");
    flags->format->suppress_required = YES;

    flags->list = G_define_flag();
    flags->list->key = 'l';
    flags->list->description =
        _("List available layers in data source and exit");
    flags->list->guisection = _("Print");
    flags->list->suppress_required = YES;

    flags->tlist = G_define_flag();
    flags->tlist->key = 't';
    flags->tlist->label = _("List available layers including feature type "
                            "in data source and exit");
    flags->tlist->description =
        _("Format: layer name,type,projection check,geometry");
    flags->tlist->guisection = _("Print");
    flags->tlist->suppress_required = YES;

    flags->topo = G_define_standard_flag(G_FLG_V_TOPO);

    if (G_parser(argc, argv))
        exit(EXIT_FAILURE);
}
