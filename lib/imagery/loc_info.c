#include <grass/imagery.h>
#include <stdio.h>
#include <string.h>
#include <grass/gis.h>

/* makes a three part title with location, mapset info */
char *I_location_info(const char *middle)
{
    char left[80];
    char right[80];
    char *buf;
    int len, buf_len;

    snprintf(left, 80, "LOCATION: %s", G_location());
    snprintf(right, 80, "MAPSET: %s", G_mapset());
    len = 79 - strlen(left) - strlen(middle) - strlen(right);
    buf_len = len + strlen(left) + strlen(middle) + strlen(right);
    buf = (char *)G_calloc(buf_len, sizeof(char));
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    snprintf(buf, buf_len, "%s%*s%s%*s%s", left, len / 2, "", middle, len / 2,
             "", right);
=======
    G_snprintf(buf, buf_len, "%s%*s%s%*s%s", left, len / 2, "", middle, len / 2,
               "", right);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    G_snprintf(buf, buf_len, "%s%*s%s%*s%s", left, len / 2, "", middle, len / 2,
               "", right);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    return buf;
}
