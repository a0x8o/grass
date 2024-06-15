#include <grass/gis.h>
#include <grass/raster.h>
#include "h_measure.h"

typedef struct dimensions {
    int size; /* size of moving window */
    int dist; /* value of distance */
    int nrows;
    int ncols;
    int n_outputs;
    int n_measures;
} dimensions;

typedef struct output_setting {
    int *outfd;
    RASTER_MAP_TYPE out_data_type;
    struct Flag *flag_null;
    struct Flag *flag_ind;
} output_setting;

int execute_texture(CELL **data, struct dimensions *dim,
                    struct menu *measure_menu, int *measure_idx,
<<<<<<< HEAD
                    struct output_setting *out_set, int threads);
=======
                    struct output_setting *out_set);
>>>>>>> 84cd6c77f3 (r.texture: Refactor code, remove global variables (#3785))
