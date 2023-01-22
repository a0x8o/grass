#include <stdio.h>
#include <grass/gis.h>

#define POLYGON_DIMENSION 20
/* From FAOSOIL CD, after USDA 1951, p209 */

struct vector {
    double sand;
    double clay;
    double silt;
};

double point_in_triangle(double point_x, double point_y, double point_z,
                         double t1_x, double t1_y, double t1_z, double t2_x,
                         double t2_y, double t2_z, double t3_x, double t3_y,
                         double t3_z)
{
    G_debug(1, "point_in_triangle: sand=%5.3f clay=%5.3f silt=%5.3f", point_x,
            point_y, point_z);
    double answer;
    double answer1_x, answer1_y, answer1_z;
    double answer2_x, answer2_y, answer2_z;
    double answer3_x, answer3_y, answer3_z;

    /* Consider three points forming a trinagle from a given soil class boundary
     * ABC */
    /* Consider F an additional point in space */
    double af1, af2, af3; /*Points for vector AF */
    double bf1, bf2, bf3; /*Points for vector BF */
    double cf1, cf2, cf3; /*Points for vector CF */
    double ab1, ab2, ab3; /*Points for vector AB */
    double bc1, bc2, bc3; /*Points for vector BC */
    double ca1, ca2, ca3; /*Points for vector CA */

    /* Create vectors AB, BC and CA */
    ab1 = (t2_x - t1_x);
    ab2 = (t2_y - t1_y);
    ab3 = (t2_z - t1_z);
    bc1 = (t3_x - t2_x);
    bc2 = (t3_y - t2_y);
    bc3 = (t3_z - t2_z);
    ca1 = (t1_x - t3_x);
    ca2 = (t1_y - t3_y);
    ca3 = (t1_z - t3_z);
    /* Create vectors AF, BF and CF */
    af1 = (point_x - t1_x);
    af2 = (point_y - t1_y);
    af3 = (point_z - t1_z);
    bf1 = (point_x - t2_x);
    bf2 = (point_y - t2_y);
    bf3 = (point_z - t2_z);
    cf1 = (point_x - t3_x);
    cf2 = (point_y - t3_y);
    cf3 = (point_z - t3_z);
    /* Calculate the following CrossProducts: */
    /* AFxAB */
    answer1_x = (af2 * ab3) - (af3 * ab2);
    answer1_y = (af3 * ab1) - (af1 * ab3);
    answer1_z = (af1 * ab2) - (af2 * ab1);
    /* G_message("answer(AFxAB)= %f %f %f",answer1_x, answer1_y, answer1_z); */
    /*BFxBC */
    answer2_x = (bf2 * bc3) - (bf3 * bc2);
    answer2_y = (bf3 * bc1) - (bf1 * bc3);
    answer2_z = (bf1 * bc2) - (bf2 * bc1);
    /* G_message("answer(BFxBC)= %f %f %f",answer2_x, answer2_y, answer2_z); */
    /*CFxCA */
    answer3_x = (cf2 * ca3) - (cf3 * ca2);
    answer3_y = (cf3 * ca1) - (cf1 * ca3);
    answer3_z = (cf1 * ca2) - (cf2 * ca1);
    /* G_message("answer(CFxCA)= %f %f %f",answer3_x, answer3_y, answer3_z); */
    answer = 0.0; /*initialize value */
    if ((int)answer1_x >= 0 && (int)answer2_x >= 0 && (int)answer3_x >= 0) {
        answer += 1.0;
    }
    else if ((int)answer1_x <= 0 && (int)answer2_x <= 0 &&
             (int)answer3_x <= 0) {
        answer -= 1.0;
    }
    if ((int)answer1_y >= 0 && (int)answer2_y >= 0 && (int)answer3_y >= 0) {
        answer += 1.0;
    }
    else if ((int)answer1_y <= 0 && (int)answer2_y <= 0 &&
             (int)answer3_y <= 0) {
        answer -= 1.0;
    }
    if ((int)answer1_z >= 0 && (int)answer2_z >= 0 && (int)answer3_z >= 0) {
        answer += 1.0;
    }
    else if ((int)answer1_z <= 0 && (int)answer2_z <= 0 &&
             (int)answer3_z <= 0) {
        answer -= 1.0;
    }
    if (answer == 3 || answer == -3) {
        answer = 1;
    }
    else {
        answer = 0;
    }
    return answer;
}

int prct2tex(double sand_input, double clay_input, double silt_input)
{
    G_debug(1, "%5.3f||%5.3f||%5.3f", sand_input, clay_input, silt_input);

    /* set up index for soil texture classes */
    int index = 20;

    /* set up mark index for inside/outside polygon check */
    double mark[POLYGON_DIMENSION] = {0.0};
    /*G_message("in prct2tex()"); */
    /*setup the 3Dvectors and initialize them */
    /* index 0 */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
=======
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
=======
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
=======
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
=======
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
=======
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
=======
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
=======
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
=======
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
=======
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
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
=======
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
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
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
=======
<<<<<<< HEAD
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
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
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
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
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
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
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> osgeo-main
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
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
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
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
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
<<<<<<< HEAD
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3eda12a66b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a8044361bc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bb025880fe (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f8994c35ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 65b9047faa (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{.sand = 0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    struct vector cls_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 1 */
    struct vector cls_sandy_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 2 */
    struct vector cls_silty_clay[POLYGON_DIMENSION] = {{0.0}};
    /* index 3 */
    struct vector cls_sandy_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 4 */
    struct vector cls_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 5 */
    struct vector cls_silty_clay_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 6 */
    struct vector cls_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 7 */
    struct vector cls_loamy_sand[POLYGON_DIMENSION] = {{0.0}};
    /* index 8 */
    struct vector cls_sandy_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 9 */
    struct vector cls_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 10 */
    struct vector cls_silt_loam[POLYGON_DIMENSION] = {{0.0}};
    /* index 11 */
    struct vector cls_silt[POLYGON_DIMENSION] = {{0.0}};
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2f988a83ac (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
    struct vector cls_silt[POLYGON_DIMENSION] = {{.sand = 0.0}};
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))

    if ((sand_input + clay_input + silt_input) <= 10.0) {
        sand_input = sand_input * 100.0;
        clay_input = clay_input * 100.0;
        silt_input = silt_input * 100.0;
    }
    /*G_message("%5.3f||%5.3f||%5.3f|",sand_input,clay_input,silt_input); */

    /*Feed the polygons for index 0 */
    cls_clay[0].sand = 0.0;
    cls_clay[0].clay = 100.0;
    cls_clay[0].silt = 0.0;
    cls_clay[1].sand = 0.0;
    cls_clay[1].clay = 60.0;
    cls_clay[1].silt = 40.0;
    cls_clay[2].sand = 20.0;
    cls_clay[2].clay = 40.0;
    cls_clay[2].silt = 40.0;
    cls_clay[3].sand = 50.0;
    cls_clay[3].clay = 40.0;
    cls_clay[3].silt = 10.0;
    cls_clay[4].sand = 50.0;
    cls_clay[4].clay = 50.0;
    cls_clay[4].silt = 0.0;
    /* Check for index 0 */
    /* G_message("in prct2tex(): check for index 0"); */
    mark[0] = point_in_triangle(
        sand_input, clay_input, silt_input, cls_clay[0].sand, cls_clay[0].clay,
        cls_clay[0].silt, cls_clay[1].sand, cls_clay[1].clay, cls_clay[1].silt,
        cls_clay[2].sand, cls_clay[2].clay, cls_clay[2].silt);
    mark[1] = point_in_triangle(
        sand_input, clay_input, silt_input, cls_clay[0].sand, cls_clay[0].clay,
        cls_clay[0].silt, cls_clay[2].sand, cls_clay[2].clay, cls_clay[2].silt,
        cls_clay[3].sand, cls_clay[3].clay, cls_clay[3].silt);
    mark[2] = point_in_triangle(
        sand_input, clay_input, silt_input, cls_clay[0].sand, cls_clay[0].clay,
        cls_clay[0].silt, cls_clay[3].sand, cls_clay[3].clay, cls_clay[3].silt,
        cls_clay[4].sand, cls_clay[4].clay, cls_clay[4].silt);
    /* G_message("Clay: mark[0]=%f",mark[0]); */
    /* G_message("Clay: mark[1]=%f",mark[1]); */
    /* G_message("Clay: mark[2]=%f",mark[2]); */
    if (mark[0] == 1 || mark[1] == 1 || mark[2] == 1) {
        index = 0;
        /* G_message("Clay: index labelled as 0"); */
    }
    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 1 */
        cls_sandy_clay[0].sand = 50.0;
        cls_sandy_clay[0].clay = 50.0;
        cls_sandy_clay[0].silt = 0.0;
        cls_sandy_clay[1].sand = 50.0;
        cls_sandy_clay[1].clay = 35.0;
        cls_sandy_clay[1].silt = 15.0;
        cls_sandy_clay[2].sand = 65.0;
        cls_sandy_clay[2].clay = 35.0;
        cls_sandy_clay[2].silt = 0.0;
        /* Check for index 1 */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sandy_clay[0].sand,
            cls_sandy_clay[0].clay, cls_sandy_clay[0].silt,
            cls_sandy_clay[1].sand, cls_sandy_clay[1].clay,
            cls_sandy_clay[1].silt, cls_sandy_clay[2].sand,
            cls_sandy_clay[2].clay, cls_sandy_clay[2].silt);

        /* G_message("Sandy Clay: mark[0]=%f",mark[0]); */
        if (mark[0] == 1) {
            index = 1;
            /* G_message("Sandy Clay: index labelled as 1"); */
        }
    }
    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 2 */
        cls_silty_clay[0].sand = 0.0;
        cls_silty_clay[0].clay = 60.0;
        cls_silty_clay[0].silt = 40.0;
        cls_silty_clay[1].sand = 0.0;
        cls_silty_clay[1].clay = 40.0;
        cls_silty_clay[1].silt = 60.0;
        cls_silty_clay[2].sand = 20.0;
        cls_silty_clay[2].clay = 40.0;
        cls_silty_clay[2].silt = 40.0;
        /* Check for index 2 */
        /* G_message("sand=%5.3f||clay=%5.3f||silt=%5.3f",sand_input,
           clay_input,silt_input); */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_silty_clay[0].sand,
            cls_silty_clay[0].clay, cls_silty_clay[0].silt,
            cls_silty_clay[1].sand, cls_silty_clay[1].clay,
            cls_silty_clay[1].silt, cls_silty_clay[2].sand,
            cls_silty_clay[2].clay, cls_silty_clay[2].silt);

        /* G_message("Silty Clay: mark[0]=%f",mark[0]); */
        if (mark[0] == 1) {
            index = 2;
            /* G_message("Silty Clay: index labelled as 2"); */
        }
    }
    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 3 */
        cls_sandy_clay_loam[0].sand = 65.0;
        cls_sandy_clay_loam[0].clay = 35.0;
        cls_sandy_clay_loam[0].silt = 0.0;
        cls_sandy_clay_loam[1].sand = 50.0;
        cls_sandy_clay_loam[1].clay = 35.0;
        cls_sandy_clay_loam[1].silt = 15.0;
        cls_sandy_clay_loam[2].sand = 50.0;
        cls_sandy_clay_loam[2].clay = 30.0;
        cls_sandy_clay_loam[2].silt = 20.0;
        cls_sandy_clay_loam[3].sand = 55.0;
        cls_sandy_clay_loam[3].clay = 25.0;
        cls_sandy_clay_loam[3].silt = 20.0;
        cls_sandy_clay_loam[4].sand = 75.0;
        cls_sandy_clay_loam[4].clay = 25.0;
        cls_sandy_clay_loam[4].silt = 0.0;
        /* Check for index 0 */
        /* G_message("in prct2tex(): check for index 3"); */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sandy_clay_loam[0].sand,
            cls_sandy_clay_loam[0].clay, cls_sandy_clay_loam[0].silt,
            cls_sandy_clay_loam[1].sand, cls_sandy_clay_loam[1].clay,
            cls_sandy_clay_loam[1].silt, cls_sandy_clay_loam[2].sand,
            cls_sandy_clay_loam[2].clay, cls_sandy_clay_loam[2].silt);
        mark[1] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sandy_clay_loam[0].sand,
            cls_sandy_clay_loam[0].clay, cls_sandy_clay_loam[0].silt,
            cls_sandy_clay_loam[2].sand, cls_sandy_clay_loam[2].clay,
            cls_sandy_clay_loam[2].silt, cls_sandy_clay_loam[3].sand,
            cls_sandy_clay_loam[3].clay, cls_sandy_clay_loam[3].silt);
        mark[2] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sandy_clay_loam[0].sand,
            cls_sandy_clay_loam[0].clay, cls_sandy_clay_loam[0].silt,
            cls_sandy_clay_loam[3].sand, cls_sandy_clay_loam[3].clay,
            cls_sandy_clay_loam[3].silt, cls_sandy_clay_loam[4].sand,
            cls_sandy_clay_loam[4].clay, cls_sandy_clay_loam[4].silt);
        /* G_message("Sandy Clay Loam: mark[0]=%f",mark[0]); */
        /* G_message("Sandy Clay Loam: mark[1]=%f",mark[1]); */
        /* G_message("Sandy Clay Loam: mark[2]=%f",mark[2]); */
        if (mark[0] == 1 || mark[1] == 1 || mark[2] == 1) {
            index = 3;
            /* G_message("Sandy Clay Loam: index labelled as 3"); */
        }
    }
    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 4 */
        cls_clay_loam[0].sand = 20.0;
        cls_clay_loam[0].clay = 40.0;
        cls_clay_loam[0].silt = 40.0;
        cls_clay_loam[1].sand = 20.0;
        cls_clay_loam[1].clay = 30.0;
        cls_clay_loam[1].silt = 50.0;
        cls_clay_loam[2].sand = 50.0;
        cls_clay_loam[2].clay = 30.0;
        cls_clay_loam[2].silt = 20.0;
        cls_clay_loam[3].sand = 10.0;
        cls_clay_loam[3].clay = 50.0;
        cls_clay_loam[3].silt = 40.0;
        /* Check for index 4 */
        /* G_message("in prct2tex(): check for index 4"); */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_clay_loam[0].sand,
            cls_clay_loam[0].clay, cls_clay_loam[0].silt, cls_clay_loam[1].sand,
            cls_clay_loam[1].clay, cls_clay_loam[1].silt, cls_clay_loam[2].sand,
            cls_clay_loam[2].clay, cls_clay_loam[2].silt);
        mark[1] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_clay_loam[0].sand,
            cls_clay_loam[0].clay, cls_clay_loam[0].silt, cls_clay_loam[2].sand,
            cls_clay_loam[2].clay, cls_clay_loam[2].silt, cls_clay_loam[3].sand,
            cls_clay_loam[3].clay, cls_clay_loam[3].silt);
        /* G_message("Clay Loam: mark[0]=%f",mark[0]); */
        /* G_message("Clay Loam: mark[1]=%f",mark[1]); */
        if (mark[0] == 1 || mark[1] == 1) {
            index = 4;
            /* G_message("Clay Loam: index labelled as 4"); */
        }
    }
    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 5 */
        cls_silty_clay_loam[0].sand = 0.0;
        cls_silty_clay_loam[0].clay = 40.0;
        cls_silty_clay_loam[0].silt = 60.0;
        cls_silty_clay_loam[1].sand = 0.0;
        cls_silty_clay_loam[1].clay = 30.0;
        cls_silty_clay_loam[1].silt = 70.0;
        cls_silty_clay_loam[2].sand = 20.0;
        cls_silty_clay_loam[2].clay = 30.0;
        cls_silty_clay_loam[2].silt = 50.0;
        cls_silty_clay_loam[3].sand = 20.0;
        cls_silty_clay_loam[3].clay = 40.0;
        cls_silty_clay_loam[3].silt = 40.0;
        /* Check for index 5 */
        /* G_message("in prct2tex(): check for index 5"); */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_silty_clay_loam[0].sand,
            cls_silty_clay_loam[0].clay, cls_silty_clay_loam[0].silt,
            cls_silty_clay_loam[1].sand, cls_silty_clay_loam[1].clay,
            cls_silty_clay_loam[1].silt, cls_silty_clay_loam[2].sand,
            cls_silty_clay_loam[2].clay, cls_silty_clay_loam[2].silt);
        mark[1] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_silty_clay_loam[0].sand,
            cls_silty_clay_loam[0].clay, cls_silty_clay_loam[0].silt,
            cls_silty_clay_loam[2].sand, cls_silty_clay_loam[2].clay,
            cls_silty_clay_loam[2].silt, cls_silty_clay_loam[3].sand,
            cls_silty_clay_loam[3].clay, cls_silty_clay_loam[3].silt);
        /* G_message("Silty Clay Loam: mark[0]=%f",mark[0]); */
        /* G_message("Silty Clay Loam: mark[1]=%f",mark[1]); */
        if (mark[0] == 1 || mark[1] == 1) {
            index = 5;
            /* G_message("Silty Clay Loam: index labelled as 5"); */
        }
    }
    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 6 */
        cls_sand[0].sand = 85.0;
        cls_sand[0].clay = 15.0;
        cls_sand[0].silt = 0.0;
        cls_sand[1].sand = 85.0;
        cls_sand[1].clay = 0.0;
        cls_sand[1].silt = 15.0;
        cls_sand[2].sand = 100.0;
        cls_sand[2].clay = 0.0;
        cls_sand[2].silt = 0.0;
        /* Check for index 6 */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sand[0].sand,
            cls_sand[0].clay, cls_sand[0].silt, cls_sand[1].sand,
            cls_sand[1].clay, cls_sand[1].silt, cls_sand[2].sand,
            cls_sand[2].clay, cls_sand[2].silt);
        /* G_message("Sand: mark[0]=%f",mark[0]); */
        if (mark[0] == 1) {
            index = 6;
            /* G_message("Sand: index labelled as 6"); */
        }
    }
    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 7 */
        cls_loamy_sand[0].sand = 80.0;
        cls_loamy_sand[0].clay = 20.0;
        cls_loamy_sand[0].silt = 0.0;
        cls_loamy_sand[1].sand = 70.0;
        cls_loamy_sand[1].clay = 0.0;
        cls_loamy_sand[1].silt = 30.0;
        cls_loamy_sand[2].sand = 85.0;
        cls_loamy_sand[2].clay = 0.0;
        cls_loamy_sand[2].silt = 15.0;
        cls_loamy_sand[3].sand = 85.0;
        cls_loamy_sand[3].clay = 15.0;
        cls_loamy_sand[3].silt = 0.0;
        /* Check for index 7 */
        /* G_message("in prct2tex(): check for index 7"); */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_loamy_sand[0].sand,
            cls_loamy_sand[0].clay, cls_loamy_sand[0].silt,
            cls_loamy_sand[1].sand, cls_loamy_sand[1].clay,
            cls_loamy_sand[1].silt, cls_loamy_sand[2].sand,
            cls_loamy_sand[2].clay, cls_loamy_sand[2].silt);
        mark[1] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_loamy_sand[0].sand,
            cls_loamy_sand[0].clay, cls_loamy_sand[0].silt,
            cls_loamy_sand[2].sand, cls_loamy_sand[2].clay,
            cls_loamy_sand[2].silt, cls_loamy_sand[3].sand,
            cls_loamy_sand[3].clay, cls_loamy_sand[3].silt);
        /* G_message("Loamy Sand: mark[0]=%f",mark[0]); */
        /* G_message("Loamy Sand: mark[1]=%f",mark[1]); */
        if (mark[0] == 1 || mark[1] == 1) {
            index = 7;
            /* G_message("Loamy Sand: index labelled as 7"); */
        }
    }

    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 8 */
        cls_sandy_loam[0].sand = 75.0;
        cls_sandy_loam[0].clay = 25.0;
        cls_sandy_loam[0].silt = 0.0;
        cls_sandy_loam[1].sand = 55.0;
        cls_sandy_loam[1].clay = 25.0;
        cls_sandy_loam[1].silt = 20.0;
        cls_sandy_loam[2].sand = 55.0;
        cls_sandy_loam[2].clay = 10.0;
        cls_sandy_loam[2].silt = 35.0;
        cls_sandy_loam[3].sand = 40.0;
        cls_sandy_loam[3].clay = 10.0;
        cls_sandy_loam[3].silt = 50.0;
        cls_sandy_loam[4].sand = 50.0;
        cls_sandy_loam[4].clay = 0.0;
        cls_sandy_loam[4].silt = 50.0;
        cls_sandy_loam[5].sand = 70.0;
        cls_sandy_loam[5].clay = 0.0;
        cls_sandy_loam[5].silt = 30.0;
        cls_sandy_loam[6].sand = 80.0;
        cls_sandy_loam[6].clay = 20.0;
        cls_sandy_loam[6].silt = 0.0;
        /* Check for index 8 */
        /* G_message("in prct2tex(): check for index 8"); */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sandy_loam[2].sand,
            cls_sandy_loam[2].clay, cls_sandy_loam[2].silt,
            cls_sandy_loam[3].sand, cls_sandy_loam[3].clay,
            cls_sandy_loam[3].silt, cls_sandy_loam[4].sand,
            cls_sandy_loam[4].clay, cls_sandy_loam[4].silt);
        mark[1] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sandy_loam[2].sand,
            cls_sandy_loam[2].clay, cls_sandy_loam[2].silt,
            cls_sandy_loam[4].sand, cls_sandy_loam[4].clay,
            cls_sandy_loam[4].silt, cls_sandy_loam[5].sand,
            cls_sandy_loam[5].clay, cls_sandy_loam[5].silt);
        mark[2] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sandy_loam[2].sand,
            cls_sandy_loam[2].clay, cls_sandy_loam[2].silt,
            cls_sandy_loam[5].sand, cls_sandy_loam[5].clay,
            cls_sandy_loam[5].silt, cls_sandy_loam[6].sand,
            cls_sandy_loam[6].clay, cls_sandy_loam[6].silt);
        mark[3] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sandy_loam[2].sand,
            cls_sandy_loam[2].clay, cls_sandy_loam[2].silt,
            cls_sandy_loam[6].sand, cls_sandy_loam[6].clay,
            cls_sandy_loam[6].silt, cls_sandy_loam[0].sand,
            cls_sandy_loam[0].clay, cls_sandy_loam[0].silt);
        mark[4] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_sandy_loam[2].sand,
            cls_sandy_loam[2].clay, cls_sandy_loam[2].silt,
            cls_sandy_loam[0].sand, cls_sandy_loam[0].clay,
            cls_sandy_loam[0].silt, cls_sandy_loam[1].sand,
            cls_sandy_loam[1].clay, cls_sandy_loam[1].silt);
        /* G_message("Sandy Loam: mark[0]=%f",mark[0]); */
        /* G_message("Sandy Loam: mark[1]=%f",mark[1]); */
        if (mark[0] == 1 || mark[1] == 1 || mark[2] == 1 || mark[3] == 1 ||
            mark[4] == 1) {
            index = 8;
            /* G_message("Sandy Loam: index labelled as 8"); */
        }
    }

    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 9 */
        cls_loam[0].sand = 50.0;
        cls_loam[0].clay = 30.0;
        cls_loam[0].silt = 20.0;
        cls_loam[1].sand = 20.0;
        cls_loam[1].clay = 30.0;
        cls_loam[1].silt = 50.0;
        cls_loam[2].sand = 40.0;
        cls_loam[2].clay = 10.0;
        cls_loam[2].silt = 50.0;
        cls_loam[3].sand = 55.0;
        cls_loam[3].clay = 10.0;
        cls_loam[3].silt = 35.0;
        cls_loam[4].sand = 55.0;
        cls_loam[4].clay = 25.0;
        cls_loam[4].silt = 15.0;
        /* Check for index 9 */
        /* G_message("in prct2tex(): check for index 9"); */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_loam[0].sand,
            cls_loam[0].clay, cls_loam[0].silt, cls_loam[1].sand,
            cls_loam[1].clay, cls_loam[1].silt, cls_loam[2].sand,
            cls_loam[2].clay, cls_loam[2].silt);
        mark[1] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_loam[0].sand,
            cls_loam[0].clay, cls_loam[0].silt, cls_loam[2].sand,
            cls_loam[2].clay, cls_loam[2].silt, cls_loam[3].sand,
            cls_loam[3].clay, cls_loam[3].silt);
        mark[2] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_loam[0].sand,
            cls_loam[0].clay, cls_loam[0].silt, cls_loam[3].sand,
            cls_loam[3].clay, cls_loam[3].silt, cls_loam[4].sand,
            cls_loam[4].clay, cls_loam[4].silt);
        /* G_message("Sandy Loam: mark[0]=%f",mark[0]); */
        /* G_message("Sandy Loam: mark[1]=%f",mark[1]); */
        if (mark[0] == 1 || mark[1] == 1 || mark[2] == 1) {
            index = 9;
            /* G_message("Loam: index labelled as 9"); */
        }
    }

    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 10 */
        cls_silt_loam[0].sand = 20.0;
        cls_silt_loam[0].clay = 30.0;
        cls_silt_loam[0].silt = 50.0;
        cls_silt_loam[1].sand = 0.0;
        cls_silt_loam[1].clay = 30.0;
        cls_silt_loam[1].silt = 70.0;
        cls_silt_loam[2].sand = 0.0;
        cls_silt_loam[2].clay = 10.0;
        cls_silt_loam[2].silt = 90.0;
        cls_silt_loam[3].sand = 15.0;
        cls_silt_loam[3].clay = 10.0;
        cls_silt_loam[3].silt = 75.0;
        cls_silt_loam[4].sand = 25.0;
        cls_silt_loam[4].clay = 0.0;
        cls_silt_loam[4].silt = 75.0;
        cls_silt_loam[5].sand = 50.0;
        cls_silt_loam[5].clay = 0.0;
        cls_silt_loam[5].silt = 50.0;
        /* Check for index 10 */
        /* G_message("in prct2tex(): check for index 10"); */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_silt_loam[3].sand,
            cls_silt_loam[3].clay, cls_silt_loam[3].silt, cls_silt_loam[4].sand,
            cls_silt_loam[4].clay, cls_silt_loam[4].silt, cls_silt_loam[5].sand,
            cls_silt_loam[5].clay, cls_silt_loam[5].silt);
        mark[1] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_silt_loam[3].sand,
            cls_silt_loam[3].clay, cls_silt_loam[3].silt, cls_silt_loam[5].sand,
            cls_silt_loam[5].clay, cls_silt_loam[5].silt, cls_silt_loam[0].sand,
            cls_silt_loam[0].clay, cls_silt_loam[0].silt);
        mark[2] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_silt_loam[3].sand,
            cls_silt_loam[3].clay, cls_silt_loam[3].silt, cls_silt_loam[0].sand,
            cls_silt_loam[0].clay, cls_silt_loam[0].silt, cls_silt_loam[1].sand,
            cls_silt_loam[1].clay, cls_silt_loam[1].silt);
        mark[3] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_silt_loam[3].sand,
            cls_silt_loam[3].clay, cls_silt_loam[3].silt, cls_silt_loam[1].sand,
            cls_silt_loam[1].clay, cls_silt_loam[1].silt, cls_silt_loam[2].sand,
            cls_silt_loam[2].clay, cls_silt_loam[2].silt);
        /* G_message("Silt Loam: mark[0]=%f",mark[0]); */
        /* G_message("Silt Loam: mark[1]=%f",mark[1]); */
        /* G_message("Silt Loam: mark[2]=%f",mark[2]); */
        /* G_message("Silt Loam: mark[3]=%f",mark[3]); */
        if (mark[0] == 1 || mark[1] == 1 || mark[2] == 1 || mark[3] == 1) {
            index = 10;
            /* G_message("Silt Loam: index labelled as 10"); */
        }
    }

    if (index == 20) { /* if index not found then continue */
        /*Feed the polygons for index 11 */
        cls_silt[0].sand = 15.0;
        cls_silt[0].clay = 10.0;
        cls_silt[0].silt = 75.0;
        cls_silt[1].sand = 0.0;
        cls_silt[1].clay = 10.0;
        cls_silt[1].silt = 90.0;
        cls_silt[2].sand = 0.0;
        cls_silt[2].clay = 0.0;
        cls_silt[2].silt = 100.0;
        cls_silt[3].sand = 25.0;
        cls_silt[3].clay = 0.0;
        cls_silt[3].silt = 75.0;
        /* Check for index 11 */
        /* G_message("in prct2tex(): check for index 11"); */
        mark[0] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_silt[0].sand,
            cls_silt[0].clay, cls_silt[0].silt, cls_silt[1].sand,
            cls_silt[1].clay, cls_silt[1].silt, cls_silt[2].sand,
            cls_silt[2].clay, cls_silt[2].silt);
        mark[1] = point_in_triangle(
            sand_input, clay_input, silt_input, cls_silt[0].sand,
            cls_silt[0].clay, cls_silt[0].silt, cls_silt[2].sand,
            cls_silt[2].clay, cls_silt[2].silt, cls_silt[3].sand,
            cls_silt[3].clay, cls_silt[3].silt);
        /* G_message("Silt: mark[0]=%f",mark[0]); */
        /* G_message("Silt: mark[1]=%f",mark[1]); */
        if (mark[0] == 1 || mark[1] == 1) {
            index = 11;
            /* G_message("Silt: index labelled as 11"); */
        }
    }
    if (index == 0) {
        G_debug(1, "clay");
    }
    else if (index == 1) {
        G_debug(1, "sandy clay");
    }
    else if (index == 2) {
        G_debug(1, "silty clay");
    }
    else if (index == 3) {
        G_debug(1, "sandy clay loam");
    }
    else if (index == 4) {
        G_debug(1, "clay loam");
    }
    else if (index == 5) {
        G_debug(1, "silty clay loam");
    }
    else if (index == 6) {
        G_debug(1, "sand");
    }
    else if (index == 7) {
        G_debug(1, "loamy sand");
    }
    else if (index == 8) {
        G_debug(1, "sandy loam");
    }
    else if (index == 9) {
        G_debug(1, "loam");
    }
    else if (index == 10) {
        G_message("silt loam");
    }
    else if (index == 11) {
        G_debug(1, "silt");
    }
    else {
        G_debug(1, "Unable to allocate class");
    }
    return index;
}
