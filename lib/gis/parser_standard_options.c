/*!
   \file lib/gis/parser_standard_options.c

   \brief GIS Library - Argument parsing functions (standard options)

   (C) 2001-2019 by the GRASS Development Team

   This program is free software under the GNU General Public License
   (>=v2). Read the file COPYING that comes with GRASS for details.

   \author Original author CERL
   \author Soeren Gebbert added Dec. 2009 WPS process_description document
   \author Luca Delucchi added Aug 2011 G_OPT_M_DIR
 */

#include <grass/gis.h>
#include <grass/glocale.h>

#include "parser_local_proto.h"

/*!
   \brief Create standardised Option structure.

   This function will create a standardised Option structure defined by
   parameter <i>opt</i>.

   Valid parameters are defined by the STD_OPT enum in the file gis.h.
   A list of valid parameter values sorted to groups is below.

   This function allocates memory for the Option structure and returns a
   pointer to this memory.

   If an invalid parameter was specified a empty Option structure will
   be returned (not NULL).

   Values also need to be added to general/g.parser/standard_option.c

   \par List of STD_OPT values sorted by module group
   - database:
   - G_OPT_DB_SQL
   - G_OPT_DB_WHERE
   - G_OPT_DB_TABLE
   - G_OPT_DB_DRIVER
   - G_OPT_DB_DATABASE
   - G_OPT_DB_SCHEMA
   - G_OPT_DB_COLUMN
   - G_OPT_DB_COLUMNS
   - G_OPT_DB_KEYCOLUMN

   - imagery:
   - G_OPT_I_GROUP
   - G_OPT_I_SUBGROUP

   - raster:
   - G_OPT_MEMORYMB
   - G_OPT_R_INPUT
   - G_OPT_R_INPUTS
   - G_OPT_R_OUTPUT
   - G_OPT_R_MAP
   - G_OPT_R_MAPS
   - G_OPT_R_BASE
   - G_OPT_R_COVER
   - G_OPT_R_ELEV
   - G_OPT_R_ELEVS
   - G_OPT_R_TYPE
   - G_OPT_R_INTERP_TYPE
   - G_OPT_R_BASENAME_INPUT
   - G_OPT_R_BASENAME_OUTPUT

   - raster3d:
   - G_OPT_R3_INPUT
   - G_OPT_R3_INPUTS
   - G_OPT_R3_OUTPUT
   - G_OPT_R3_MAP
   - G_OPT_R3_MAPS

   - vector:
   - G_OPT_V_INPUT
   - G_OPT_V_INPUTS
   - G_OPT_V_OUTPUT
   - G_OPT_V_MAP
   - G_OPT_V_MAPS
   - G_OPT_V_TYPE
   - G_OPT_V_FIELD
   - G_OPT_V_FIELD_ALL
   - G_OPT_V_CAT
   - G_OPT_V_CATS
   - G_OPT_V_ID
   - G_OPT_V_IDS

   - files
   - G_OPT_F_INPUT
   - G_OPT_F_BIN_INPUT
   - G_OPT_F_OUTPUT
   - G_OPT_F_SEP

   - colors
   - G_OPT_C
   - G_OPT_CN
   - G_OPT_C_FORMAT

   - misc
   - G_OPT_M_DIR
   - G_OPT_M_UNITS
   - G_OPT_M_DATATYPE
   - G_OPT_M_MAPSET
   - G_OPT_M_LOCATION
   - G_OPT_M_DBASE
   - G_OPT_M_COORDS
   - G_OPT_M_COLR
   - G_OPT_M_REGION
   - G_OPT_M_NULL_VALUE
   - G_OPT_M_NPROCS

   - temporal GIS framework
   - G_OPT_STDS_INPUT
   - G_OPT_STDS_INPUTS
   - G_OPT_STDS_OUTPUT
   - G_OPT_STRDS_INPUT
   - G_OPT_STRDS_INPUTS
   - G_OPT_STRDS_OUTPUT
   - G_OPT_STRDS_OUTPUTS
   - G_OPT_STR3DS_INPUT
   - G_OPT_STR3DS_INPUTS
   - G_OPT_STR3DS_OUTPUT
   - G_OPT_STVDS_INPUT
   - G_OPT_STVDS_INPUTS
   - G_OPT_STVDS_OUTPUT
   - G_OPT_MAP_INPUT
   - G_OPT_MAP_INPUTS
   - G_OPT_STDS_TYPE
   - G_OPT_MAP_TYPE
   - G_OPT_T_TYPE
   - G_OPT_T_WHERE

   \param opt type of Option struct to create specified by STD_OPT enum

   \return pointer to an Option struct
 */
struct Option *G_define_standard_option(int opt)
{
    struct Option *Opt;
    char *memstr;

    Opt = G_define_option();

    switch (opt) {
    case G_OPT_DB_SQL:
        Opt->key = "sql";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "sql_query";
        Opt->required = NO;
        Opt->label = _("SQL SELECT statement");
        Opt->description =
            _("Example: select * from towns where population > 10000");
        break;
    case G_OPT_DB_WHERE:
        Opt->key = "where";
        Opt->type = TYPE_STRING;
        Opt->gisprompt = "old,sql_query,sql_query";
        Opt->key_desc = "sql_query";
        Opt->required = NO;
        Opt->label =
            _("WHERE conditions of SQL statement without 'where' keyword");
        Opt->description = _("Example: income < 1000 and population >= 10000");
        break;
    case G_OPT_DB_TABLE:
        Opt->key = "table";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->description = _("Name of attribute table");
        Opt->gisprompt = "old,dbtable,dbtable";
        break;
    case G_OPT_DB_DRIVER:
        Opt->key = "driver";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->description = _("Name of database driver");
        Opt->gisprompt = "old,dbdriver,dbdriver";
        break;
    case G_OPT_DB_DATABASE:
        Opt->key = "database";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->description = _("Name of database");
        Opt->gisprompt = "old,dbname,dbname";
        break;
    case G_OPT_DB_SCHEMA:
        Opt->key = "schema";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->label = _("Database schema");
        Opt->description = _("Do not use this option if schemas "
                             "are not supported by driver/database server");
        break;
    case G_OPT_DB_COLUMN:
        Opt->key = "column";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->description = _("Name of attribute column");
        Opt->gisprompt = "old,dbcolumn,dbcolumn";
        break;
    case G_OPT_DB_COLUMNS:
        Opt->key = "columns";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->multiple = YES;
        Opt->description = _("Name of attribute column(s)");
        Opt->gisprompt = "old,dbcolumn,dbcolumn";
        break;
    case G_OPT_DB_KEYCOLUMN:
        Opt->key = "key";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->label = _("Name of key column");
        Opt->description = _("Must refer to an integer column");
        /* Opt->gisprompt = "old,dbcolumn,dbcolumn"; */
        Opt->answer = GV_KEY_COLUMN;
        break;

        /* imagery group */
    case G_OPT_I_GROUP:
        Opt->key = "group";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,group,group";
        Opt->description = _("Name of input imagery group");
        break;
    case G_OPT_I_SUBGROUP:
        Opt->key = "subgroup";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,subgroup,subgroup";
        Opt->description = _("Name of input imagery subgroup");
        break;

        /* raster maps */
    case G_OPT_MEMORYMB:
        Opt->key = "memory";
        Opt->type = TYPE_INTEGER;
        Opt->key_desc = "memory in MB";
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->answer = "300";
        /* start dynamic answer */
        /* check MEMORYMB in GISRC, set with g.gisenv */
        memstr = G_store(G_getenv_nofatal("MEMORYMB"));
        if (memstr && *memstr)
            Opt->answer = memstr;
        /* end dynamic answer */
        Opt->label = _("Maximum memory to be used (in MB)");
        Opt->description = _("Cache size for raster rows");
        break;
    case G_OPT_R_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,cell,raster";
        Opt->description = _("Name of input raster map");
        break;
    case G_OPT_R_INPUTS:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,cell,raster";
        Opt->description = _("Name of input raster map(s)");
        break;
    case G_OPT_R_OUTPUT:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "new,cell,raster";
        Opt->description = _("Name for output raster map");
        break;
    case G_OPT_R_OUTPUTS:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "new,cell,raster";
        Opt->description = _("Name for output raster map(s)");
        break;
    case G_OPT_R_MAP:
        Opt->key = "map";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,cell,raster";
        Opt->description = _("Name of raster map");
        break;
    case G_OPT_R_MAPS:
        Opt->key = "map";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,cell,raster";
        Opt->description = _("Name of raster map(s)");
        break;
    case G_OPT_R_BASE:
        Opt->key = "base";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,cell,raster";
        Opt->description = _("Name of base raster map");
        break;
    case G_OPT_R_COVER:
        Opt->key = "cover";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,cell,raster";
        Opt->description = _("Name of cover raster map");
        break;
    case G_OPT_R_ELEV:
        Opt->key = "elevation";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,cell,raster";
        Opt->description = _("Name of input elevation raster map");
        break;
    case G_OPT_R_ELEVS:
        Opt->key = "elevation";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,cell,raster";
        Opt->description = _("Name of input elevation raster map(s)");
        break;
    case G_OPT_R_TYPE:
        Opt->key = "type";
        Opt->type = TYPE_STRING;
        Opt->required = YES;
        Opt->multiple = NO;
        Opt->label = _("Type of raster map to be created");
        Opt->description = _("Storage type for resultant raster map");
        Opt->options = "CELL,FCELL,DCELL";
        G_asprintf((char **)&(Opt->descriptions), "CELL;%s;FCELL;%s;DCELL;%s",
                   _("Integer"), _("Single precision floating point"),
                   _("Double precision floating point"));
        break;
    case G_OPT_R_INTERP_TYPE:
        Opt->key = "method";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->description = _("Sampling interpolation method");
        Opt->options = "nearest,bilinear,bicubic";
        G_asprintf((char **)&(Opt->descriptions),
                   "nearest;%s;bilinear;%s;bicubic;%s",
                   _("Nearest-neighbor interpolation"),
                   _("Bilinear interpolation"), _("Bicubic interpolation"));
        break;
    case G_OPT_R_BASENAME_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "basename";
        Opt->required = YES;
        Opt->multiple = NO;
        Opt->gisprompt = "old,cell,raster";
        Opt->description = _("Name of input basename raster map(s)");
        break;
    case G_OPT_R_BASENAME_OUTPUT:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "basename";
        Opt->required = YES;
        Opt->multiple = NO;
        Opt->gisprompt = "new,cell,raster";
        Opt->description = _("Name for output basename raster map(s)");
        break;

        /*g3d maps */
    case G_OPT_R3_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,grid3,raster_3d";
        Opt->description = _("Name of input 3D raster map");
        break;
    case G_OPT_R3_INPUTS:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,grid3,raster_3d";
        Opt->description = _("Name of input 3D raster map(s)");
        break;
    case G_OPT_R3_OUTPUT:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "new,grid3,raster_3d";
        Opt->description = _("Name for output 3D raster map");
        break;
    case G_OPT_R3_MAP:
        Opt->key = "map";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,grid3,raster_3d";
        Opt->description = _("Name of 3D raster map");
        break;
    case G_OPT_R3_MAPS:
        Opt->key = "map";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,grid3,raster_3d";
        Opt->description = _("Name of 3D raster map(s)");
        break;
    case G_OPT_R3_TYPE:
        Opt->key = "type";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->answer = "default";
        Opt->options = "default,double,float";
        Opt->description = _("Data type used in the output raster3d map");
        break;
    case G_OPT_R3_PRECISION:
        Opt->key = "precision";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->answer = "default";
        Opt->description =
            _("Number of digits used as mantissa in the internal map storage, "
              "0 -23 for float, 0 - 52 for double, max or default");
        break;
    case G_OPT_R3_COMPRESSION:
        Opt->key = "compression";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->answer = "default";
        Opt->options = "default,zip,none";
        Opt->description =
            _("The compression method used in the output raster3d map");
        break;
    case G_OPT_R3_TILE_DIMENSION:
        Opt->key = "tiledimension";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->key_desc = "XxYxZ";
        Opt->answer = "default";
        Opt->description = _("The dimensions of the tiles used in the output "
                             "raster3d map (XxYxZ or default: 16x16x8)");
        break;

        /*vector maps */
    case G_OPT_V_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,vector,vector";
        Opt->label = _("Name of input vector map");
        Opt->description = _("Or data source for direct OGR access");
        break;
    case G_OPT_V_INPUTS:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,vector,vector";
        Opt->label = _("Name of input vector map(s)");
        Opt->description = _("Or data source(s) for direct OGR access");
        break;
    case G_OPT_V_OUTPUT:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "new,vector,vector";
        Opt->description = _("Name for output vector map");
        break;
    case G_OPT_V_MAP:
        Opt->key = "map";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,vector,vector";
        Opt->label = _("Name of vector map");
        Opt->description = _("Or data source for direct OGR access");
        break;
    case G_OPT_V_MAPS:
        Opt->key = "map";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,vector,vector";
        Opt->description = _("Name of vector map(s)");
        break;
    case G_OPT_V_TYPE:
        Opt->key = "type";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = YES;
        Opt->answer = "point,line,boundary,centroid,area";
        Opt->options = "point,line,boundary,centroid,area";
        Opt->description = _("Input feature type");
        break;
    case G_OPT_V3_TYPE:
        Opt->key = "type";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = YES;
        Opt->answer = "point,line,boundary,centroid,area,face,kernel";
        Opt->options = "point,line,boundary,centroid,area,face,kernel";
        Opt->description = _("Input feature type");
        break;
    case G_OPT_V_FIELD:
        Opt->key = "layer";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->answer = "1";
        Opt->label = _("Layer number or name");
        Opt->description =
            _("Vector features can have category values in different layers."
              " This number determines which layer to use. "
              "When used with direct OGR access this is the layer name.");
        Opt->gisprompt = "old,layer,layer";
        break;
    case G_OPT_V_FIELD_ALL:
        Opt->key = "layer";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->answer = "-1";
        Opt->label = _("Layer number or name ('-1' for all layers)");
        Opt->description =
            _("A single vector map can be connected to multiple database "
              "tables. This number determines which table to use. "
              "When used with direct OGR access this is the layer name.");
        Opt->gisprompt = "old,layer_all,layer";
        break;
    case G_OPT_V_CAT:
        Opt->key = "cat";
        Opt->type = TYPE_INTEGER;
        Opt->required = NO;
        Opt->description = _("Category value");
        Opt->gisprompt = "old,cat,cats";
        break;
    case G_OPT_V_CATS:
        Opt->key = "cats";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "range";
        Opt->required = NO;
        Opt->label = _("Category values");
        Opt->description = _("Example: 1,3,7-9,13");
        Opt->gisprompt = "old,cats,cats";
        break;
    case G_OPT_V_ID:
        Opt->key = "id";
        Opt->type = TYPE_INTEGER;
        Opt->required = NO;
        Opt->description = _("Feature id");
        break;
    case G_OPT_V_IDS:
        Opt->key = "ids";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "range";
        Opt->required = NO;
        Opt->label = _("Feature ids");
        Opt->description = _("Example: 1,3,7-9,13");
        break;

        /* files */
    case G_OPT_F_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,file,file";
        Opt->description = _("Name of input file");
        break;
    case G_OPT_F_BIN_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,bin,file";
        Opt->description = _("Name of input file");
        break;
    case G_OPT_F_OUTPUT:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "new,file,file";
        Opt->description = _("Name for output file");
        break;
    case G_OPT_F_SEP:
        Opt->key = "separator";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "character";
        Opt->required = NO;
        Opt->gisprompt = "old,separator,separator";
        Opt->answer = "pipe";
        Opt->label = _("Field separator");
        Opt->description =
            _("Special characters: pipe, comma, space, tab, newline");
        break;

        /* colors */
    case G_OPT_C:
        Opt->key = "color";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->answer = DEFAULT_FG_COLOR;
        Opt->gisprompt = "old,color,color";
        Opt->label = _("Color");
        Opt->description = _("Either a standard color name or R:G:B triplet");
        break;
    case G_OPT_CN:
        Opt->key = "color";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->answer = DEFAULT_FG_COLOR;
        Opt->gisprompt = "old,color_none,color";
        Opt->label = _("Color");
        Opt->description =
            _("Either a standard color name, R:G:B triplet, or \"none\"");
        break;
<<<<<<< HEAD
<<<<<<< HEAD
    case G_OPT_C_FORMAT:
        Opt->key = "color_format";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = NO;
        Opt->answer = "hex";
        Opt->options = "rgb,hex,hsv,triplet";
        Opt->label = _("Color format");
        Opt->description = _("Color format for output values.");
        G_asprintf(
            (char **)&(Opt->descriptions), "rgb;%s;hex;%s;hsv;%s;triplet;%s",
            _("output color in RGB format"), _("output color in HEX format"),
            _("output color in HSV format (experimental)"),
            _("output color in colon-separated RGB format"));
        break;
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

        /* misc */

    case G_OPT_M_DIR:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,dir,dir";
        Opt->description = _("Name of input directory");
        break;

    case G_OPT_M_UNITS:
        Opt->key = "units";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->options = "miles,feet,meters,kilometers,acres,hectares";
        Opt->description = _("Units");
        break;

    case G_OPT_M_DATATYPE:
        Opt->key = "type";
        Opt->key_desc = "datatype";
        Opt->type = TYPE_STRING;
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->description = _("Data type(s)");
        break;

    case G_OPT_M_MAPSET:
        Opt->key = "mapset";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->key_desc = "name";
        Opt->gisprompt = "old,mapset,mapset";
        Opt->label = _("Name of mapset (default: current search path)");
        Opt->description = _("'.' for current mapset");
        break;

    case G_OPT_M_LOCATION:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
        Opt->key = "project";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->label = _("Project (location) name");
        Opt->description = _("Project name (not path to project)");
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
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
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
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
        Opt->key = "location";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->label = _("Location name");
        Opt->description = _("Location name (not location path)");
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
        Opt->gisprompt = "old,location,location";
        Opt->key_desc = "name";
        break;

    case G_OPT_M_DBASE:
        Opt->key = "dbase";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->label = _("GRASS GIS database directory");
        Opt->description = _("Default: path to the current GRASS GIS database");
        Opt->gisprompt = "old,dbase,dbase";
        Opt->key_desc = "path";
        break;

    case G_OPT_M_COORDS:
        Opt->key = "coordinates";
        Opt->type = TYPE_DOUBLE;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->key_desc = "east,north";
        Opt->gisprompt = "old,coords,coords";
        Opt->description = _("Coordinates");
        break;

    case G_OPT_M_COLR:
        Opt->key = "color";
        Opt->key_desc = "style";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->options = G_color_rules_options();
        Opt->description = _("Name of color table");
        Opt->descriptions = G_color_rules_description_type();
        Opt->gisprompt = "old,colortable,colortable";
        break;

    case G_OPT_M_NULL_VALUE:
        Opt->key = "null_value";
        Opt->key_desc = "string";
        Opt->type = TYPE_STRING;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->description = _("String representing NULL value");
        break;

    case G_OPT_M_REGION:
        Opt->key = "region";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->gisprompt = "old,windows,region";
        Opt->description = _("Name of saved region");
        break;

    case G_OPT_M_NPROCS:
        Opt->key = "nprocs";
        Opt->type = TYPE_INTEGER;
        Opt->required = NO;
        Opt->multiple = NO;
        Opt->answer = "1";
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 6d10bb4d89 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 922eb0ee2b (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 06036d3399 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> bd3bed8e46 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> edc1ad4ff0 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
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
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 9b7fa9d273 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> b3a8e05232 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> fe5afb1a39 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> ce2336a470 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 5e881b2ad2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
        /* start dynamic answer */
        /* check NPROCS in GISRC, set with g.gisenv */
        memstr = G_store(G_getenv_nofatal("NPROCS"));
        if (memstr && *memstr)
            Opt->answer = memstr;
        /* end dynamic answer */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 783d161725 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 305382ede9 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f40bbc0cdf (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 44cee187ef (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 1683a3ac91 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c06532e663 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> b6fd7f4778 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5373cb0034 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
<<<<<<< HEAD
>>>>>>> 6373caf270 (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
        Opt->description = _("Number of threads for parallel computing");
        break;

        /* Spatio-temporal modules of the temporal GIS framework */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        Opt->description = _("Number of threads for parallel computing");
        break;

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        Opt->description = _("Number of threads for parallel computing");
        break;

<<<<<<< HEAD
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        Opt->description = _("Number of threads for parallel computing");
        break;

<<<<<<< HEAD
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
    /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
        /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        Opt->description = _("Number of threads for parallel computing");
        break;

<<<<<<< HEAD
    /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> c9e7c8086a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        Opt->description = _("Number of threads for parallel computing");
        break;

<<<<<<< HEAD
    /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 5a4c41171d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        Opt->description = _("Number of threads for parallel computing");
        break;

<<<<<<< HEAD
    /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 1abf332f3e (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        /* Spatio-temporal modules of the temporal GIS framework */
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
=======
=======
>>>>>>> 270077e68a (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
>>>>>>> 03a790ad9a (wxGUI: refactoring: build GUI tools' status bars based on wx.StatusBar widget (#1689))
        Opt->description = _("Number of threads for parallel computing");
        break;

<<<<<<< HEAD
    /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> b3428cff9f (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
        /* Spatio-temporal modules of the temporal GIS framework */
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
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> c660f119eb (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> f11184521d (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    /* Spatio-temporal modules of the temporal GIS framework */
>>>>>>> 015cec3442 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
>>>>>>> 16acf9dbd2 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
<<<<<<< HEAD
>>>>>>> 327a0b62e3 (wxGUI/map display: manage wx.StatusBar widget by AUI (#1646))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
    case G_OPT_STDS_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,stds,stds";
        Opt->description = _("Name of the input space time dataset");
        break;
    case G_OPT_STDS_INPUTS:
        Opt->key = "inputs";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,stds,stds";
        Opt->description = _("Name of the input space time datasets");
        break;
    case G_OPT_STDS_OUTPUT:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "new,stds,stds";
        Opt->description = _("Name of the output space time dataset");
        break;
    case G_OPT_STRDS_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,strds,strds";
        Opt->description = _("Name of the input space time raster dataset");
        break;
    case G_OPT_STRDS_INPUTS:
        Opt->key = "inputs";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,strds,strds";
        Opt->description = _("Name of the input space time raster datasets");
        break;
    case G_OPT_STRDS_OUTPUT:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "new,strds,strds";
        Opt->description = _("Name of the output space time raster dataset");
        break;
    case G_OPT_STRDS_OUTPUTS:
        Opt->key = "outputs";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "new,strds,strds";
        Opt->description = _("Name of the output space time raster datasets");
        break;
    case G_OPT_STVDS_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,stvds,stvds";
        Opt->description = _("Name of the input space time vector dataset");
        break;
    case G_OPT_STVDS_INPUTS:
        Opt->key = "inputs";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,stvds,stvds";
        Opt->description = _("Name of the input space time vector datasets");
        break;
    case G_OPT_STVDS_OUTPUT:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "new,stvds,stvds";
        Opt->description = _("Name of the output space time vector dataset");
        break;
    case G_OPT_STR3DS_INPUT:
        Opt->key = "input";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,str3ds,str3ds";
        Opt->description = _("Name of the input space time raster3d dataset");
        break;
    case G_OPT_STR3DS_INPUTS:
        Opt->key = "inputs";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,str3ds,str3ds";
        Opt->description = _("Name of the input space time raster3d datasets");
        break;
    case G_OPT_STR3DS_OUTPUT:
        Opt->key = "output";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "new,str3ds,str3ds";
        Opt->description = _("Name of the output space time raster3d dataset");
        break;
    case G_OPT_STDS_TYPE:
        Opt->key = "type";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->answer = "strds";
        Opt->options = "strds,stvds,str3ds";
        Opt->description = _("Type of the input space time dataset");
        break;
    case G_OPT_MAP_INPUT:
        Opt->key = "map";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->gisprompt = "old,map,map";
        Opt->description = _("Name of the input map");
        break;
    case G_OPT_MAP_INPUTS:
        Opt->key = "maps";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->multiple = YES;
        Opt->gisprompt = "old,map,map";
        Opt->description = _("Name of the input maps");
        break;
    case G_OPT_MAP_TYPE:
        Opt->key = "type";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->answer = "raster";
        Opt->options = "raster,vector,raster_3d";
        Opt->description = _("Type of the input map");
        break;
    case G_OPT_T_TYPE:
        Opt->key = "temporaltype";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->answer = "absolute";
        Opt->options = "absolute,relative";
        Opt->description = _("The temporal type of the space time dataset");
        break;
    case G_OPT_T_WHERE:
        Opt->key = "where";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "sql_query";
        Opt->required = NO;
        Opt->label = _("WHERE conditions of SQL statement without 'where' "
                       "keyword used in the temporal GIS framework");
        Opt->description = _("Example: start_time > '2001-01-01 12:30:00'");
        break;
    case G_OPT_T_SAMPLE:
        Opt->key = "sampling";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = NO;
        Opt->multiple = YES;
        Opt->answer = "start";
        Opt->options = "start,during,overlap,contain,equal,follows,precedes";
        Opt->description =
            _("The method to be used for sampling the input dataset");
        break;
<<<<<<< HEAD
<<<<<<< HEAD
    case G_OPT_F_FORMAT:
        Opt->key = "format";
        Opt->type = TYPE_STRING;
        Opt->key_desc = "name";
        Opt->required = YES;
        Opt->label = _("Output format");
        Opt->answer = "plain";
        Opt->options = "plain,json";
        Opt->descriptions = _("plain;Plain text output;"
                              "json;JSON (JavaScript Object Notation);");
        break;
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    }

    return Opt;
}

/*!
   \brief Create standardised Flag structure.

   This function will create a standardised Flag structure defined by
   parameter <i>flag</i>. A list of valid parameters below. It
   allocates memory for the Flag structure and returns a pointer to
   this memory.

   If an invalid parameter was specified a empty Flag structure will be
   returned (not NULL).

   - G_FLG_V_TABLE  (do not create attribute table)
   - G_FLG_V_TOPO   (do not build topology)

   \param flag type of Flag struct to create specified by STD_FLG enum.

   \return pointer to an Flag struct
 */
struct Flag *G_define_standard_flag(int flag)
{
    struct Flag *Flg;

    Flg = G_define_flag();

    switch (flag) {
    case G_FLG_V_TABLE:
        Flg->key = 't';
        Flg->description = _("Do not create attribute table");
        break;
    case G_FLG_V_TOPO:
        Flg->key = 'b';
        Flg->label = _("Do not build topology");
        Flg->description =
            _("Advantageous when handling a large number of points");
        break;
    }

    return Flg;
}
