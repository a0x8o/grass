#include "pv.h"

/* Not yet implemented - just defaults */

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
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
void vrml_put_view(FILE *vout, struct G_3dview *v3d UNUSED)
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
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
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
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
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
void vrml_put_view(FILE *vout, struct G_3dview *v3d)
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
{
    char tbuf[512];

#ifdef VRML2

    vrml_putline(vout, "view\n");

#else
    /*
       vrml_putline(1, vout, "DirectionalLight {");
       sprintf(tbuf,"intensity %f",1.0);
       vrml_putline(0, vout, tbuf);
       sprintf(tbuf,"color %f %f %f",1.0, 1.0, 1.0);
       vrml_putline(0, vout, tbuf);
       sprintf(tbuf,"direction %f %f %f",0.0, 0.0, -1.0);
       vrml_putline(0, vout, tbuf);
       vrml_putline(-1, vout,"}");
     */
    vrml_putline(1, vout, "PerspectiveCamera {");
    sprintf(tbuf, "position %f %f %f", 0.0, 0.0, 1.0);
    vrml_putline(0, vout, tbuf);
    /*
       sprintf(tbuf,"orientation %f %f %f  %f", 1.0, 0.0, 0.0, 4.3175);
     */
    sprintf(tbuf, "orientation %f %f %f  %f", 0.0, 0.0, 1.0, 0.0);
    vrml_putline(0, vout, tbuf);
    sprintf(tbuf, "focalDistance %f", 3.0);
    vrml_putline(0, vout, tbuf);
    sprintf(tbuf, "heightAngle %f", 0.785398); /* 45 degrees */
    vrml_putline(0, vout, tbuf);
    vrml_putline(-1, vout, "}");

#endif
}
