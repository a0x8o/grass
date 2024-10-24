/******************************************************************************
 *
 *      pick_dist.c  inverse square distance distributed probability generator
 *
 * Usage: pick_dist (maxnumber)
 *
 * Notes: prob_invsqr() generates a decreasing probability distribution
 * outward in an inverse square rate. It use three consecutive random number
 * generator:
 *     applying it once gets an UNIFORM distribution in the range of 0-max_num;
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
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
 *     doing it twice gets a SIMPLE INVERSE distribution in that range;
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
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
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
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
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
 *     doing it twice gets a SIMPLE INVERSE distribuion in that range;
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
 *     doing three times gets a INVERSE SQUARE distribution.
 *
 * Author: Jianping Xu, Rutgers University
 * Date: 06/11/1994
 ******************************************************************************/

#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <grass/gis.h>
#include "local_proto.h"

/**
 * @brief Picks one possible distance value from range 0, u
 * @param u maximum potential distance
 * @return value in range 0, u
 */
int pick_dist(int u)
{
    int v;

    v = (int)((u + 0.99999999999) * G_drand48());
    u = (int)((v + 0.99999999999) * G_drand48());
    return ((int)((u + 0.99999999999) * G_drand48())); /*4th for a test */
}
