#include "global.h"

int report(void)
{
    int unit1, unit2;

<<<<<<< HEAD
    switch (format) {
    case JSON:
        print_json();
        break;
    case PLAIN:
        if (stats_flag == STATS_ONLY)
            return 1;

        if (nunits == 0)
            print_report(0, -1);
        else
            for (unit1 = 0; unit1 < nunits; unit1 = unit2 + 1) {
                unit2 = unit1 + 2;
                if (unit2 >= nunits)
                    unit2 = nunits - 1;
                print_report(unit1, unit2);
            }
        break;
    }
=======
    if (stats_flag == STATS_ONLY)
        return 1;

    if (nunits == 0)
        print_report(0, -1);
    else
        for (unit1 = 0; unit1 < nunits; unit1 = unit2 + 1) {
            unit2 = unit1 + 2;
            if (unit2 >= nunits)
                unit2 = nunits - 1;
            print_report(unit1, unit2);
        }
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

    return 0;
}
