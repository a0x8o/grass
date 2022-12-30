# Test suite

Tests are in directories `tests` and `testsuite` under each directory which has tests.
This directory contains additional scripts and information to test functionality
without a focus on a specific part of the code.

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
There are two testing mechanism in place, _pytest_ which is the modern way of testing
GRASS GIS. Tests using _pytest_ are written just as any other Python tests.
=======
=======
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
GRASS GIS testsuite documentation: <https://grass.osgeo.org/grass-devel/manuals/libpython/gunittest_testing.html>
=======
GRASS GIS testsuite documentation: https://grass.osgeo.org/grass80/manuals/libpython/gunittest_testing.html
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> e78917837c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
GRASS GIS testsuite documentation: https://grass.osgeo.org/grass80/manuals/libpython/gunittest_testing.html
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 5cd58fa15c (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
GRASS GIS testsuite documentation: <https://grass.osgeo.org/grass-devel/manuals/libpython/gunittest_testing.html>
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
GRASS GIS testsuite documentation: <https://grass.osgeo.org/grass-devel/manuals/libpython/gunittest_testing.html>
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b5acd78515 (wxpyimgview: explicit conversion to int (#2704))

In parallel, there is also custom unittest-based framework centered around
_grass.gunittest_ package. These tests run in the NC sample datasets and can be
executed using _pytest_ or directly. The unittest-based adds a number of custom
assert methods to accommodate different data and outputs typical in GRASS GIS.
_grass.gunittest_ documentation:
<https://grass.osgeo.org/grass-devel/manuals/libpython/gunittest_testing.html>

## Running tests

Tests can be executed using _pytest_:

```bash
# Setup the Python environment (if not set up already).
# Replace grass by path to the executable if not installed on path.
export PYTHONPATH=\$(grass --config python_path):\$PYTHONPATH
export LD_LIBRARY_PATH=\$(grass --config path)/lib:\$LD_LIBRARY_PATH
# Run the test.
pytest
```

## Test data

To test manually or to write tests, you may need to use the North Carolina
Sample dataset, available from
<https://grass.osgeo.org/sampledata/north_carolina/>.

## CI

<<<<<<< HEAD
Most tests run in the CI. See the `.github` directory for details and
use it as a reference.
=======
Since 2020: For a more advanced test suite, see
<https://github.com/OSGeo/grass/actions>

Until 2019: For a more advanced test suite, see
<http://fatra.cnr.ncsu.edu/grassgistests/summary_report/>
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))

>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> bc7152a288 (wxpyimgview: explicit conversion to int (#2704))
