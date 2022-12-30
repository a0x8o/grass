/**************************************************************
 * I_find_init (group)
 *
 * Find the a camera initial file in the current group (if it exists)
 **************************************************************/
#include <grass/gis.h>
#include <grass/glocale.h>

int I_find_initial(char *group)
{
<<<<<<< HEAD
    char element[GNAME_MAX + 6];

    if (group == NULL || *group == 0)
        return 0;

    if (snprintf(element, GNAME_MAX, "group/%s", group) >= GNAME_MAX) {
        G_warning(_("Group name <%s> is too long"), group);
        return 0;
    }

=======
    char *element;

    element = (char *)G_malloc(80 * sizeof(char));

    if (group == NULL || *group == 0)
        return 0;
    sprintf(element, "group/%s", group);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    return G_find_file(element, "INIT_EXP", G_mapset()) != NULL;
}
