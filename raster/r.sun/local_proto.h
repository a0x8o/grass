/* main.c */

void where_is_point(double *length, struct SunGeometryVarDay *sunVarGeom,
                    struct GridGeometry *gridGeom);
void where_is_point_parallel(double *length, double *sunVarGeom_zp,
                             double *gridGeom_xx0, double *gridGeom_yy0,
                             double *gridGeom_xg0, double *gridGeom_yg0,
                             double *gridGeom_stepx, double *gridGeom_stepy);
int searching(double *length, struct SunGeometryVarDay *sunVarGeom,
              struct GridGeometry *gridGeom);
int searching_parallel(double *length, double *sunVarGeom_z_orig,
                       double *sunVarGeom_zmax, double *sunVarGeom_zp,
                       double *sunVarGeom_tanSolarAltitude,
                       double *sunVarGeom_stepsinangle,
                       double *sunVarGeom_stepcosangle, double *gridGeom_xx0,
                       double *gridGeom_yy0, double *gridGeom_xg0,
                       double *gridGeom_yg0, double *gridGeom_stepx,
                       double *gridGeom_stepy, double *gridGeom_deltx,
                       double *gridGeom_delty);

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
int useCivilTime(void);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int useCivilTime(void);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
int useCivilTime(void);
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int useCivilTime();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
int useCivilTime(void);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
int useCivilTime();
=======
int useCivilTime(void);
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
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
int useCivilTime(void);
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int useCivilTime();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int useCivilTime(void);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
int useCivilTime(void);
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int useCivilTime();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int useCivilTime(void);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
int useCivilTime(void);
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
int useCivilTime();
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
int useCivilTime(void);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
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
void setUseCivilTime(int val);
int useShadow(void);
void setUseShadow(int val);
int useShadowData(void);
void setUseShadowData(int val);
int useHorizonData(void);
void setUseHorizonData(int val);
double getTimeOffset(void);
void setTimeOffset(double val);
double getHorizonInterval(void);
void setHorizonInterval(double val);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
void setAngularLossDenominator(void);
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
void setAngularLossDenominator(void);
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
=======
void setAngularLossDenominator(void);
=======
>>>>>>> osgeo-main
void setAngularLossDenominator();
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
void setAngularLossDenominator(void);
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
void setAngularLossDenominator();
=======
void setAngularLossDenominator(void);
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
void setAngularLossDenominator(void);
=======
void setAngularLossDenominator();
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
void setAngularLossDenominator(void);
=======
void setAngularLossDenominator();
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
void setAngularLossDenominator(void);
=======
void setAngularLossDenominator();
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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

/* void cube(int, int); */

double com_sol_const(int no_of_day);

double brad(double, double *bh, struct SunGeometryVarDay *sunVarGeom,
            struct SunGeometryVarSlope *sunSlopeGeom,
            struct SolarRadVar *sunRadVar);
double brad_parallel(double sh, double *bh, double *sunVarGeom_z_orig,
                     double *sunVarGeom_solarAltitude,
                     double *sunVarGeom_sinSolarAltitude,
                     double *sunSlopeGeom_slope, double *sunSlopeGeom_aspect,
                     double *sunRadVar_cbh, double *sunRadVar_linke,
                     double *sunRadVar_G_norm_extra);

double drad(double, double bh, double *rr, struct SunGeometryVarDay *sunVarGeom,
            struct SunGeometryVarSlope *sunSlopeGeom,
            struct SolarRadVar *sunRadVar);
double drad_parallel(double sh, double bh, double *rr, int *sunVarGeom_isShadow,
                     double *sunVarGeom_solarAltitude,
                     double *sunVarGeom_sinSolarAltitude,
                     double *sunVarGeom_solarAzimuth,
                     double *sunSlopeGeom_aspect, double *sunSlopeGeom_slope,
                     double *sunRadVar_cdh, double *sunRadVar_linke,
                     double *sunRadVar_G_norm_extra, double *sunRadVar_alb);

double brad_angle_loss(double, double *bh, struct SunGeometryVarDay *sunVarGeom,
                       struct SunGeometryVarSlope *sunSlopeGeom,
                       struct SolarRadVar *sunRadVar);
double drad_angle_loss(double, double bh, double *rr,
                       struct SunGeometryVarDay *sunVarGeom,
                       struct SunGeometryVarSlope *sunSlopeGeom,
                       struct SolarRadVar *sunRadVar);

void com_par(struct SunGeometryConstDay *sungeom,
             struct SunGeometryVarDay *sunVarGeom,
             struct GridGeometry *gridGeom, double latitude, double longitude);
void com_par_parallel(
    double *sunGeom_lum_C11, double *sunGeom_lum_C13, double *sunGeom_lum_C22,
    double *sunGeom_lum_C31, double *sunGeom_lum_C33,
    double *sunGeom_sunrise_time, double *sunGeom_sunset_time,
    double *sunGeom_timeAngle, double *sunVarGeom_solarAltitude,
    double *sunVarGeom_sinSolarAltitude, double *sunVarGeom_tanSolarAltitude,
    double *sunVarGeom_solarAzimuth, double *sunVarGeom_sunAzimuthAngle,
    double *sunVarGeom_stepsinangle, double *sunVarGeom_stepcosangle,
    double *gridGeom_stepxy, double latitude);

void com_par_const(double longitTime, struct SunGeometryConstDay *sungeom,
                   struct GridGeometry *gridGeom);
void com_par_const_parallel(double longitTime, double *sunGeom_lum_C11,
                            double *sunGeom_lum_C13, double *sunGeom_lum_C22,
                            double *sunGeom_lum_C31, double *sunGeom_lum_C33,
                            double *sunGeom_sunrise_time,
                            double *sunGeom_sunset_time,
                            double *sunGeom_timeAngle, double *sunGeom_sindecl,
                            double *sunGeom_cosdecl, double *gridGeom_sinlat,
                            double *gridGeom_coslat);

double lumcline2(struct SunGeometryConstDay *sungeom,
                 struct SunGeometryVarDay *sunVarGeom,
                 struct SunGeometryVarSlope *sunSlopeGeom,
                 struct GridGeometry *gridGeom, unsigned char *horizonpointer);
double lumcline2_parallel(
    double *sunGeom_timeAngle, int *sunVarGeom_isShadow,
    double *sunVarGeom_solarAltitude, double *sunVarGeom_sunAzimuthAngle,
    double *sunVarGeom_z_orig, double *sunVarGeom_zmax, double *sunVarGeom_zp,
    double *sunVarGeom_tanSolarAltitude, double *sunVarGeom_stepsinangle,
    double *sunVarGeom_stepcosangle, double *sunSlopeGeom_longit_l,
    double *sunSlopeGeom_lum_C31_l, double *sunSlopeGeom_lum_C33_l,
    double *gridGeom_xx0, double *gridGeom_yy0, double *gridGeom_xg0,
    double *gridGeom_yg0, double *gridGeom_stepx, double *gridGeom_stepy,
    double *gridGeom_deltx, double *gridGeom_delty,
    unsigned char *horizonpointer);

typedef double (*BeamRadFunc)(double sh, double *bh,
                              struct SunGeometryVarDay *sunVarGeom,
                              struct SunGeometryVarSlope *sunSlopeGeom,
                              struct SolarRadVar *sunRadVar);

typedef double (*DiffRadFunc)(double sh, double bh, double *rr,
                              struct SunGeometryVarDay *sunVarGeom,
                              struct SunGeometryVarSlope *sunSlopeGeom,
                              struct SolarRadVar *sunRadVar);
