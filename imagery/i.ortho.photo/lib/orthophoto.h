#include <grass/gis.h>
#include <grass/imagery.h>
#include "mat.h"

/* #define DEBUG  1 */

#define INITIAL_X_VAR     500
#define INITIAL_Y_VAR     500
#define INITIAL_Z_VAR     1000
#define INITIAL_OMEGA_VAR 0.01
#define INITIAL_PHI_VAR   0.01
#define INITIAL_KAPPA_VAR 0.1

/* REF file in a group doing orthophoto */
struct Ortho_Image_Group_Ref {
    int nfiles;
    struct Ortho_Image_Group_Ref_Files {
        char name[GNAME_MAX];
        char mapset[GMAPSET_MAX];
    } *file;
    struct Ortho_Ref_Color {
        unsigned char *table; /* color table for min-max values */
        unsigned char *index; /* data translation index */
        unsigned char *buf;   /* data buffer for reading color file */
        int fd;               /* for image i/o */
        CELL min, max;        /* min,max CELL values */
        int n;                /* index into Ref_Files */
    } red, grn, blu;
};

/* camera file inside $MAPSET/CAMERA folder */
/* has a filename = camera name stored in
 * $MAPSET/$GROUP/$GROUPNAME/CAMERA */
struct Ortho_Camera_File_Ref {
    char cam_name[30];
    char cam_id[30];
    double Xp;
    double Yp;
    double CFL;
    int num_fid;
    struct Fiducial {
        char fid_id[30];
        double Xf;
        double Yf;
    } fiducials[20];
};

/* Standard X,Y,Z,E,N,H structure */
struct Ortho_Photo_Points {
    int count;
    double *e1;
    double *n1;
    double *z1;
    double *e2;
    double *n2;
    double *z2;
    int *status;
};

/* Ortho_Control_Points is identical to Ortho_Photo_Points
 * Why ? */
/* Standard X,Y,Z,E,N,H structure */
struct Ortho_Control_Points {
    int count;
    double *e1;
    double *n1;
    double *z1;
    double *e2;
    double *n2;
    double *z2;
    int *status;
};

/* Contents of $MAPSET/$GROUP/$GROUPNAME/INIT_EXP
 * a result of running lib/orthoref.c:
 * I_compute_ortho_equations()*/
struct Ortho_Camera_Exp_Init {
    double XC_init;
    double YC_init;
    double ZC_init;
    double omega_init;
    double phi_init;
    double kappa_init;
    double XC_var;
    double YC_var;
    double ZC_var;
    double omega_var;
    double phi_var;
    double kappa_var;
    int status;
};

struct Ortho_Image_Group {
    char name[GNAME_MAX];
    /* Ortho_Image_Group_Ref is identical to Ortho_Group_Ref, and
       we assume this is so in the code.  If Ortho_Image_Group_Ref
       is ever different, then there will have to be a new set of
       I_get_group_ref() functions to fill it.
       struct Ortho_Image_Group_Ref    group_ref; */
    struct Ref group_ref;
    struct Ortho_Camera_File_Ref camera_ref;
    struct Ortho_Photo_Points photo_points;
    struct Ortho_Control_Points control_points;
    struct Ortho_Camera_Exp_Init camera_exp;
    int ref_equation_stat;
    int con_equation_stat;
    double E12[3], N12[3], E21[3], N21[3], Z12[3], Z21[3];
    double XC, YC, ZC, omega, phi, kappa;
    MATRIX M, MI;
};

/* conz_points.c */
int I_new_con_point(struct Ortho_Control_Points *, double, double, double,
                    double, double, double, int);
int I_get_con_points(char *, struct Ortho_Control_Points *);
int I_put_con_points(char *, struct Ortho_Control_Points *);
int I_convert_con_points(char *, struct Ortho_Control_Points *,
                         struct Ortho_Control_Points *, double[3], double[3]);
/* georef.c */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
>>>>>>> osgeo-main
int I_compute_ref_equations(struct Ortho_Photo_Points *, double *, double *,
                            double *, double *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double *, double *,
                            double *, double *);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
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
int I_compute_ref_equations(struct Ortho_Photo_Points *, double *, double *,
                            double *, double *);
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
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
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double *, double *,
                            double *, double *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
int I_compute_ref_equations(struct Ortho_Photo_Points *, double *, double *,
                            double *, double *);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double *, double *,
                            double *, double *);
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
int I_compute_ref_equations(struct Ortho_Photo_Points *, double[3], double[3],
                            double[3], double[3]);
=======
int I_compute_ref_equations(struct Ortho_Photo_Points *, double *, double *,
                            double *, double *);
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
/* orthoref.c */
int I_compute_ortho_equations(struct Ortho_Control_Points *,
                              struct Ortho_Camera_File_Ref *,
                              struct Ortho_Camera_Exp_Init *, double *,
                              double *, double *, double *, double *, double *,
                              MATRIX *, MATRIX *);
int I_ortho_ref(double, double, double, double *, double *, double *,
                struct Ortho_Camera_File_Ref *, double, double, double, MATRIX);
int I_inverse_ortho_ref(double, double, double, double *, double *, double *,
                        struct Ortho_Camera_File_Ref *, double, double, double,
                        MATRIX);
void I_ortho_panorama(void);

/* ref_points.c */
int I_new_ref_point(struct Ortho_Photo_Points *, double, double, double, double,
                    int);
int I_get_ref_points(char *, struct Ortho_Photo_Points *);
int I_put_ref_points(char *, struct Ortho_Photo_Points *);

/* cam_info.h */
int I_read_cam_info(FILE *, struct Ortho_Camera_File_Ref *);
int I_new_fid_point(struct Ortho_Camera_File_Ref *, char[30], double, double);
int I_write_cam_info(FILE *, struct Ortho_Camera_File_Ref *);
int I_get_cam_info(char *, struct Ortho_Camera_File_Ref *);
int I_put_cam_info(char *, struct Ortho_Camera_File_Ref *);

/* init_info.c */
int I_read_init_info(FILE *, struct Ortho_Camera_Exp_Init *);
int I_write_init_info(FILE *, struct Ortho_Camera_Exp_Init *);
int I_get_init_info(char *, struct Ortho_Camera_Exp_Init *);
int I_put_init_info(char *, struct Ortho_Camera_Exp_Init *);

#include <grass/ortholib.h>
