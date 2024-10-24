/* **************************************************************
 *
 *  MODULE:       v.in.dwg
 *
 *  AUTHOR(S):    Radim Blazek
 *
 *  PURPOSE:      Import of DWG/DXF files
 *
 *  COPYRIGHT:    (C) 2001 by the GRASS Development Team
 *
 *                This program is free software under the
 *                GNU General Public License (>=v2).
 *                Read the file COPYING that comes with GRASS
 *                for details.
 *
 * In addition, as a special exception, Radim Blazek gives permission
 * to link the code of this program with the OpenDWG libraries (or with
 * modified versions of the OpenDWG libraries that use the same license
 * as OpenDWG libraries), and distribute linked combinations including the two.
 * You must obey the GNU General Public License in all respects for all
 * of the code used other than. If you modify this file, you may extend
 * this exception to your version of the file, but you are not obligated
 * to do so. If you do not wish to do so, delete this exception statement
 * from your version.
 *
 * **************************************************************/

/* transformation, first level is 0 ( called from main ) and transformation
 *  for this level is 0,0,0, 1,1,1, 0 so that no transformation is done on first
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
 * level (not efective but better readable?) */
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
 * level (not effective but better readable?) */
=======
 * level (not efective but better readable?) */
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
 * level (not efective but better readable?) */
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
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 * level (not efective but better readable?) */
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
typedef struct {
    double dx, dy, dz;
    double xscale, yscale, zscale;
    double rotang;
} TRANS;

extern int cat;
extern int
    n_elements; /* number of processed elements (only low level elements) */
extern int
    n_skipped; /* number of skipped low level elements (different layer name) */
extern struct Map_info Map;
extern dbDriver *driver;
extern dbString sql;
extern dbString str;
extern struct line_pnts *Points;
extern struct line_cats *Cats;
extern PAD_LAY Layer;
extern char *Txt;
extern char *Block;
extern struct field_info *Fi;
extern AD_DB_HANDLE dwghandle;
extern TRANS *Trans; /* transformation */
extern int atrans;   /* number of allocated levels */
extern struct Option *layers_opt;
extern struct Flag *invert_flag;

void wrentity(PAD_ENT_HDR adenhd, PAD_ENT aden, int level, AD_VMADDR entlist,
              int circle_as_point);
