#include "watershed.h"
#include "string.h"

int print_output(OUTPUT *output)
{
    double cell_size;
    int b, c;
    CAT *do_cat;
    char *cat_name, area[32];

    cell_size = output->window.ns_res * output->window.ew_res;
    for (c = output->num_basins - 1; c >= 0; c--) {
        if (output->basin_facts[c].valid == 1)
            fprintf(output->out_file,
                    "\nValid Basin: %-5d flows into basin: %-5d at: E=%.1f "
                    "N=%.1f\n",
                    (c + 1) * 2, (output->basin_facts[c].down_basin + 1) * 2,
                    output->basin_facts[c].easting,
                    output->basin_facts[c].northing);
        else
            fprintf(output->out_file,
                    "\nInvalid basin: %-5d flows into basin: %-5d at: E=%.1f "
                    "N=%.1f\n",
                    (c + 1) * 2, (output->basin_facts[c].down_basin + 1) * 2,
                    output->basin_facts[c].easting,
                    output->basin_facts[c].northing);
        fprintf(output->out_file,
                "    Str. length:%-.3f meters, %-.3f feet; Str. slope:%-.4f\n",
                output->basin_facts[c].str_length,
                (double)(output->basin_facts[c].str_length * METER_TO_FOOT),
                output->basin_facts[c].str_slope);
        switch (output->type_area) {
        case 1:
            fprintf(output->out_file, "    Basin Area acres: %-16.4f",
                    output->basin_facts[c].num_cells * cell_size *
                        METERSQ_TO_ACRE);
            break;
        case 2:
            fprintf(output->out_file, "    Basin Area sq. meters: %-11.3f",
                    output->basin_facts[c].num_cells * cell_size);
            break;
        case 3:
            fprintf(output->out_file, "    Basin Area miles sq: %-16.5f",
                    output->basin_facts[c].num_cells * cell_size *
                        METERSQ_TO_MILESQ);
            break;
        case 4:
            fprintf(output->out_file, "    Basin Area hectareas: %-14.4f",
                    output->basin_facts[c].num_cells * cell_size *
                        METERSQ_TO_HECTACRE);
            break;
        case 5:
            fprintf(output->out_file, "    Basin Area kilometers: %-13.4f",
                    output->basin_facts[c].num_cells * cell_size *
                        METERSQ_TO_KILOSQ);
            break;
        case 6:
            fprintf(output->out_file, "    Basin Area in cells: %-16d",
                    output->basin_facts[c].num_cells);
            break;
        }
        fprintf(output->out_file, "             Area       Percent Basin\n");
        for (b = 0; b < output->num_maps; b++) {
            fprintf(output->out_file,
                    "<< %20s >> map layer, average category value: %.2f\n",
                    output->maps[b].name,
                    ((double)output->maps[b].basins[c].sum_values) /
                        output->basin_facts[c].num_cells);
            do_cat = &(output->maps[b].basins[c].first_cat);
            while ((output->maps[b].do_cats != 0) && do_cat) {
                cat_name =
                    Rast_get_c_cat(&(do_cat->cat_val), &(output->maps[b].cats));
                switch (output->type_area) {
                case 1:
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
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
=======
>>>>>>> 8732bd1c8a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> osgeo-main
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
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
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
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
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
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
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
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
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
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
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cd8792567f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1c1d57983f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
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
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d1484cdb51 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 993f78c5dc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7f1e5f8884 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f5392b7882 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ec40ea5aa2 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 418440c09e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> fa7fb2854a (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> be9bc80f0c (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3309d04075 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a55c458ec3 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dad8f82179 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f2a3896383 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> f103e53694 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> ef5435cdca (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5247cc90df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 207a2fa222 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> cf8c11a1bc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 2b4e1fe52e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 9b236f29f2 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 00fecb977b (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
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
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8712352f45 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 5fc304998e (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
>>>>>>> c4c5579bbb (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> e988674846 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 78361f71a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 8a5345ecec (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> a82cfbcefa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 93f0f0bbbc (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 7f1fd5e3ad (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 286cd56e73 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a610274a1c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c1f363e78b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 97e83bc298 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> c686f71e17 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> b92dc799e4 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3b16f7b005 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ee7e1bb8ec (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90b36a3841 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c10636c7fa (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4ece10bc57 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 08a1f16710 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 940b7c1705 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 4763de2e0e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> d1507c3b80 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ba9afcba1b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 287da875f8 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 81d97e00cb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0cfc981774 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 2c0ff799c3 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 85142d03b1 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 641743d544 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2797eab292 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ecb21a9ab (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 9ca218c791 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 82b75069a1 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6a641f7e2e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3d4227f4a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 31f940eb7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 898e6d54a6 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> b345bcbe37 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 776ce10d62 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fbb5219778 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> a3af1d0366 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 945afade8c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> bb9e769d49 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 8d807f37dd (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 0fd6a771d8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c5cb5c01a5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 46f73513a8 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6e838855e2 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 1fbe91036a (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> e4f002b9aa (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> c51212e49e (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 182ddbdeda (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6b3f525ed2 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fe2cfce272 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 819790960a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 233b4f3df4 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 3b4a1c4066 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 3424207483 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 981b1a43cf (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2aef6a7b52 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> da501f639c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1f07e5fd7d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> f5c4d35adb (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2a7efc1085 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 439687cd76 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> d64857ac67 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 40eab5b4ef (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> adc9a513d7 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a258a6de0c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6676a8168a (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dddb74a90a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> af64ae18ab (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 60806474cc (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 4191de5198 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> ba9b3a13b7 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> bf94cb15a9 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 63ea19eb4b (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e86959eb0c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
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
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 711671af6b (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 8922916e15 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
>>>>>>> e8a65191df (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 5a9f81a6c5 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3339528038 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 1903fbe109 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6642b650bd (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> c667b6bfad (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 3c6ff8d9ea (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b856ee1836 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d924e21742 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 089152282a (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57711afe47 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 022a06ee3d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> de41c5c11e (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 146be9abe9 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> b3e4b27026 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 0014ad4c7c (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 3bbe136a0b (r.horizon manual - fix typo (#2794))
>>>>>>> ca49da7f4d (r.horizon manual - fix typo (#2794))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 90e8567102 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 2b0d6b05cd (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> d742feb5c4 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> b12b27a326 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 960ecd077b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ae5ce5d9d0 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
>>>>>>> 6fabde9f92 (Fix missing function prototypes (#2727))
=======
>>>>>>> cb9f97dc6b (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> eeb3562b85 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 2012d6da25 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
>>>>>>> d5a6951b7c (Fix missing function prototypes (#2727))
=======
>>>>>>> 515a872888 (r.horizon manual - fix typo (#2794))
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> e8033a9dcf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 033e7a3234 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
>>>>>>> 1bc99d2b79 (Fix missing function prototypes (#2727))
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 2673808116 (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
                    break;
                case 2:
                    snprintf(area, sizeof(area), "%.2f sq. meters",
                             cell_size * do_cat->num_cat);
                    break;
                case 3:
                    snprintf(area, sizeof(area), "%.4f sq. miles",
                             METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    snprintf(area, sizeof(area), "%.3f hectacres",
                             METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    snprintf(area, sizeof(area), "%.3f sq. km.",
                             METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
<<<<<<< HEAD
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 56185653ee (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======
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
                    snprintf(area, sizeof(area), "%6d cells", do_cat->num_cat);
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> b920cd0c09 (Fix missing function prototypes (#2727))
<<<<<<< HEAD
>>>>>>> 63be8a6dfa (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
>>>>>>> 0d9b51afc4 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
                    sprintf(area, "%.3f acres",
                            METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
                    break;
                case 2:
                    sprintf(area, "%.2f sq. meters",
                            cell_size * do_cat->num_cat);
                    break;
                case 3:
                    sprintf(area, "%.4f sq. miles",
                            METERSQ_TO_MILESQ * cell_size * do_cat->num_cat);
                    break;
                case 4:
                    sprintf(area, "%.3f hectacres",
                            METERSQ_TO_HECTACRE * cell_size * do_cat->num_cat);
                    break;
                case 5:
                    sprintf(area, "%.3f sq. km.",
                            METERSQ_TO_KILOSQ * cell_size * do_cat->num_cat);
                    break;
                case 6:
                    sprintf(area, "%6d cells", do_cat->num_cat);
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 57e3ae6310 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> d9925996f3 (wxpyimgview: explicit conversion to int (#2704))
                    break;
                }
                fprintf(output->out_file, "%3d %-43s %16s %-.4f\n",
                        do_cat->cat_val, cat_name, area,
                        ((double)do_cat->num_cat) /
                            output->basin_facts[c].num_cells);
                do_cat = do_cat->nxt;
            }
        }
    }

    return 0;
}
