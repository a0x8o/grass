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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
                    snprintf(area, sizeof(area), "%.3f acres",
                             METERSQ_TO_ACRE * cell_size * do_cat->num_cat);
=======
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
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
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
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
=======
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
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
>>>>>>> 5f9feb57ee (r.horizon manual - fix typo (#2794))
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
