# MODULE:    grass.benchmark
#
# AUTHOR(S): Aaron Saw Min Sern <aaronsms u nus edu>
#            Vaclav Petras <wenzeslaus gmail com>
#
# PURPOSE:   Benchmarking for GRASS GIS modules
#
# COPYRIGHT: (C) 2021 Vaclav Petras, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.


"""Basic functions for benchmarking modules"""

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
import random
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
import random
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
import random
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> osgeo-main
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
import random
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
import random
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
import random
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
import random
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
import shutil
from types import SimpleNamespace

import grass.script as gs


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without chaning anything.
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
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
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without changing anything.
=======
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without chaning anything.
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
def benchmark_single(module, label, repeat=5):
    """Benchmark module as is without chaning anything.
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
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
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

    *module* is an instance of PyGRASS Module class or any object which
    has a *run* method which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    *repeat* sets how many times the each run is repeated.
    *label* is a text to add to the result (for user-facing display).

    Returns an object with attributes *time* (an average execution time),
    *all_times* (list of measured execution times),
    and *label* (the provided parameter as is).
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")

    print("\u2500" * term_size.columns)
    time_sum = 0
    measured_times = []
    for _ in range(repeat):
        module.run()
        print(f"{module.time}s")
        time_sum += module.time
        measured_times.append(module.time)

    avg = time_sum / repeat
    min_avg = min(avg, min_avg)
    print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
    print(f"Best average time - {min_avg}s\n")

    return SimpleNamespace(
        all_times=measured_times,
        time=avg,
        label=label,
    )


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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
def benchmark_nprocs(module, label, max_nprocs, repeat=5, shuffle=True):
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
    Runs are executed in random order, set *shuffle* to false if they
    need to be executed in order based on number of threads.
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
def benchmark_nprocs(module, label, max_nprocs, repeat):
=======
def benchmark_nprocs(module, label, max_nprocs, repeat=5):
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
    """Benchmark module using values of nprocs up to *max_nprocs*.

    *module* is an instance of PyGRASS Module class or any object which
    has a *update* method taking *nprocs* as a keyword argument,
    a *run* which takes no arguments and executes the benchmarked code,
    and attribute *time* which is set to execution time after the *run*
    function returned. Additionally, the object should be convertible to *str*
    for printing.

    The module is executed for each generated value of nprocs. *max_nprocs* is used
    to generate a continuous range of integer values from 1 up to *max_nprocs*.
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``max_nprocs * repeat`` times.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
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

    *label* is a text to add to the result (for user-facing display).
    Optional *nprocs* is passed to the module if present.

    Returns an object with attributes *times* (list of average execution times),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    result = SimpleNamespace(times=[], all_times=[], speedup=[], efficiency=[])
    result.nprocs = list(range(1, max_nprocs + 1))
    result.label = label
    nprocs_list_shuffled = sorted(result.nprocs * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
>>>>>>> osgeo-main
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
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
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
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
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        result.times.append(avg)
        result.all_times.append(times[nprocs])
=======
        avg_times.append(avg)
        all_times.append(times[nprocs])
<<<<<<< HEAD
=======
    *all_times* (list of lists of measured execution times), *nprocs*
    (list of *nprocs* values used), and *label* (the provided parameter as is).
=======
    *all_times* (list of lists of measured execution times),
    *efficiency* (parallel efficiency), *nprocs* (list of *nprocs* values used),
    and *label* (the provided parameter as is).
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
    """
    term_size = shutil.get_terminal_size()
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)

    min_avg = float("inf")
    min_time = None
    serial_avg = None
    avg_times = []
    all_times = []
    efficiency = []
    nprocs_list = list(range(1, max_nprocs + 1))
    nprocs_list_shuffled = sorted(nprocs_list * repeat)
    if shuffle:
        random.shuffle(nprocs_list_shuffled)
    times = {}
    print("\u2500" * term_size.columns)
    for nprocs in nprocs_list_shuffled:
        module.update(nprocs=nprocs)
        module.run()
        print(f"Run with {nprocs} thread(s) took {module.time}s\n")
        if nprocs in times:
            times[nprocs] += [module.time]
        else:
            times[nprocs] = [module.time]
    for nprocs in sorted(times):
        avg = sum(times[nprocs]) / repeat
        avg_times.append(avg)
<<<<<<< HEAD
        all_times.append(measured_times)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
=======
        all_times.append(times[nprocs])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
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
        if nprocs == 1:
            serial_avg = avg
        if avg < min_avg:
            min_avg = avg
            min_time = nprocs
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        efficiency.append(serial_avg / (nprocs * avg))
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
=======
        result.speedup.append(serial_avg / avg)
        result.efficiency.append(serial_avg / (nprocs * avg))
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
        efficiency.append(serial_avg / (nprocs * avg))
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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

    print("\u2500" * term_size.columns)
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> main
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
>>>>>>> main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
    return SimpleNamespace(
        all_times=all_times,
        times=avg_times,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
        efficiency=efficiency,
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        efficiency=efficiency,
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
=======
        efficiency=efficiency,
=======
>>>>>>> osgeo-main
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
        efficiency=efficiency,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
        efficiency=efficiency,
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
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
        nprocs=nprocs_list,
        label=label,
    )
=======
    return result
>>>>>>> c55184d3f6 (grass.benchmark: Compute speedup and enable plotting speedup/efficiency (#3835))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
        print(f"\nResult - {avg}s")

    print("\u2500" * term_size.columns)
<<<<<<< HEAD
    print(f"\nSerial average time - {serial_avg}s")
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    if serial_avg is not None:
        print(f"\nSerial average time - {serial_avg}s")
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
=======
    print(f"Best average time - {min_avg}s ({min_time} threads)\n")

<<<<<<< HEAD
    return result
=======
>>>>>>> osgeo-main
    return SimpleNamespace(
        all_times=all_times,
        times=avg_times,
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
        efficiency=efficiency,
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
        efficiency=efficiency,
=======
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
        efficiency=efficiency,
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
        nprocs=nprocs_list,
        label=label,
    )
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
        nprocs=nprocs_list,
        label=label,
    )
>>>>>>> f541ee3b09 (libpython: Save and load benchmark results (#1711))
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
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


def benchmark_resolutions(module, resolutions, label, repeat=5, nprocs=None):
    """Benchmark module using different resolutions.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
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
    *module* is an instance of PyGRASS Module class or any object
    with attributes as specified in :func:`benchmark_nprocs`
    except that the *update* method is required only when *nprocs* is set.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
    *module* is an instance of PyGRASS Module class.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
    *resolutions* is a list of resolutions to set (current region is currently
    used and changed but that may change in the future).
    *repeat* sets how many times the each run is repeated.
    So, the module will run ``len(resolutions) * repeat`` times.

    *label* is a text to add to the result (for user-facing display).
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
>>>>>>> osgeo-main
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
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
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
    Optional *nprocs* is passed to the module if present
    (the called module does not have to support nprocs parameter).
=======
    Optional *nprocs* is passed to the module if present.
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
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

    Returns an object with attributes *times* (list of average execution times),
    *all_times* (list of lists of measured execution times), *resolutions*
    (the provided parameter as is), *cells* (number of cells in the region),
    and *label* (the provided parameter as is).
    """
    term_size = shutil.get_terminal_size()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
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
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
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
    if hasattr(module, "get_bash"):
        print(module.get_bash())
    else:
        print(module)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> osgeo-main
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
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
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> a4624812dc (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
    print(module.get_bash())
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
>>>>>>> 434bf28e3d (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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

    avg_times = []
    all_times = []
    n_cells = []
    for resolution in resolutions:
        gs.run_command("g.region", res=resolution)
        region = gs.region()
        n_cells.append(region["cells"])
        print("\u2500" * term_size.columns)
        print(f"Benchmark with {resolution} resolution...\n")
        time_sum = 0
        measured_times = []
        for _ in range(repeat):
            if nprocs:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
                module.update(nprocs=nprocs)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                module.update(nprocs=nprocs)
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
>>>>>>> osgeo-main
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
=======
                module.update(nprocs=nprocs)
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
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 923408bf7e (libpython: Save and load benchmark results (#1711))
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> dea3ac3989 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> af1011ff1e (libpython: Save and load benchmark results (#1711))
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8962f3c6a1 (pygrass: Add update parameters method to Module (#1712))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
                module.update(nprocs=nprocs)
=======
                module(nprocs=nprocs)
>>>>>>> da7f79c3f9 (libpython: Save and load benchmark results (#1711))
>>>>>>> 033a57360f (libpython: Save and load benchmark results (#1711))
=======
=======
                module.update(nprocs=nprocs)
>>>>>>> 392c6e8e0b (pygrass: Add update parameters method to Module (#1712))
>>>>>>> 8df6d7d3ff (pygrass: Add update parameters method to Module (#1712))
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
            module.run()
            print(f"{module.time}s")
            time_sum += module.time
            measured_times.append(module.time)

        avg = time_sum / repeat
        avg_times.append(avg)
        all_times.append(measured_times)
        print(f"\nResult - {avg}s")

    return SimpleNamespace(
        all_times=all_times,
        times=avg_times,
        resolutions=resolutions,
        cells=n_cells,
        label=label,
    )
