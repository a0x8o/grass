#include <grass/vector.h>
#include <grass/parson.h>

#define SHELL_NO     0x00
#define SHELL_BASIC  0x02
#define SHELL_REGION 0x04
#define SHELL_TOPO   0x08

enum OutputFormat { PLAIN, SHELL, JSON };

/* level1.c */
int level_one_info(struct Map_info *);

/* parse.c */
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
void parse_args(int, char **, char **, char **, int *, int *, int *,
                enum OutputFormat *);
=======
void parse_args(int, char **, char **, char **, int *, int *, int *);
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
void parse_args(int, char **, char **, char **, int *, int *, int *);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
void parse_args(int, char **, char **, char **, int *, int *, int *);
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))

/* print.c */
void format_double(double, char *);
void print_region(struct Map_info *, enum OutputFormat, JSON_Object *);
void print_topo(struct Map_info *, enum OutputFormat, JSON_Object *);
void print_columns(struct Map_info *, const char *, const char *,
                   enum OutputFormat);
void print_info(struct Map_info *);
void print_shell(struct Map_info *, const char *, enum OutputFormat,
                 JSON_Object *);
