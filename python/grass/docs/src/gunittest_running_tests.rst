Running the test framework of GRASS GIS
=======================================

This is an advanced guide to running tests of GRASS GIS using GRASS
testing framework (`gunittest`). For introduction to this topic,
go to :ref:`test-general`.


.. _running-tests-report:

Running tests and creating report
---------------------------------

To test before commit, run all tests using testing framework.
First start GRASS GIS session and go to the root directory of your
GRASS GIS source code copy::

    cd my/grass/source/code/root

Then execute::

    python -m grass.gunittest.main --location locname --location-type nc

where ``locname`` is a name of location in current GRASS GIS data(base) directory
(GISDBASE) and ``nc`` is a location specified by individual test files
(the later is not yet fully implemented, so just put there ``nc`` every time).

``grass.gunittest.main`` writes a text summary to standard output and
it creates an HTML report from all tests in all ``testsuite`` directories inside
the directory tree. The report is placed in ``testreport`` by default.
Open file ``testreport/index.html`` in you web browser to inspect it.

To execute just part of the tests when fixing something, ``cd`` into some
subdirectory, e.g. ``lib`` and execute the same command as above.
gain, it will execute all tests in all ``testsuite`` subdirectories and
create a report.

For changing GRASS GIS data(base) directory and for other parameters, see
help for ``grass.gunittest.main`` module::

    python -m grass.gunittest.main --help


Running individual test files
-----------------------------

To run a single test file, start GRASS session in the Location and Mapset
suitable for testing and go to the directory where the test file is.
Then run the file as a Python script::

    python test_something.py

If the file is a ``gunittest``-based or ``unittest``-based test,
you will receive a textual output with failed individual tests (test methods).
If the file is a general Python script you need to examine the output carefully
as well as source code itself to see what is expected behavior.

The same as for general Python scripts, applies also to Shell scripts,
so you should examine the output carefully.
You should execute scripts using::

    sh -e -x test_topology_vgeneralize.sh

The ``-x`` is just to see which commands are executed but the ``-e`` flag
is crucial because this is how the GRASS testing framework runs the Shell
scripts. The flag causes execution to stop once some command gives a non-zero
return code.


Setting sensitivity of the test run
-----------------------------------

Sensitivity, specified by the ``--min-success`` parameter, determined
how many tests need to fail for the runner to consider it an error
and return a non-zero return code.
For example, if at least 60% of test is required to succeed, you can
use::

    python -m grass.gunittest.main ... --min-success 60

If all tests should succeed, use ``--min-success 100`` (the default). If you want
to run the test and ``grass.gunittest.main`` returning zero return code
even if some tests fail, use ``--min-success 0``


Excluding test files from testing
---------------------------------

Test files which would be otherwise collected and executed can be excluded
from the testing using the ``exclude`` key in the ``.gunittest.cfg``
configuration file under the ``.gunittest`` section.
The value of ``exclude`` is whitespace-separated list of exclude files
possibly with wildcards (from Python fnmatch).
Directory separators are converted to ``/`` for the matching.
Paths are relative to the directory the testing was started from.

For example, to exclude the whole directory ``vector`` and one specific file,
you would use::

    [gunittest]
    exclude =
        vector/*
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        raster/r.contour/testsuite/testrc.py
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
        raster/r.contour/testsuite/testrc.py
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
        raster/r.contour/testsuite/testrc.py
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
=======
<<<<<<< HEAD
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))
        raster/r.contour/testsuite/test_broken.py
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> osgeo-main
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0b89692930 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3dd5d8c46e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d87535920f (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> b3245b207a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c5e65de1b6 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a6a89d8471 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3cdfc9c11 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 657de3711d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d1a7e51a61 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 44155ccad2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0db65d5784 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> d94037aca8 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0544516662 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ea4e163d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> f01dbb07ac (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> af77d3065d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> afe85dd104 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 0f6c3b23ed (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6cb714f843 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f8f1e78ae8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1d3ab6bea (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e2aaf4c841 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 85c3a81f34 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e092a36981 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 2ef24fe08c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e97d22ce5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b9551b0216 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> a75e392be1 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4be3be03b6 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 6b3d2a4cfb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> c0392b8321 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 659f92e0ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 13398e56a2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 63948171f2 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4385ab760c (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> bda2ada3c0 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f1fe50e39a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> eb0461e127 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cbb81e2ed9 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 31257efc18 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> bf584e8231 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7c712c5b7d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 72ee0b4513 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 80ffe15841 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> cf6e2e0efd (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3ced4bb2db (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 1014ac8589 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 8e84f40070 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e29d325b37 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1c91f3d31b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b974eae31d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 11368ff97a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 41ab2f7485 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 68d3c5771d (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> f209031e69 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> a3451b0781 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 5ec1e27d83 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 738af27d93 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> dc25ab2280 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 800fbf33e4 (Dockerfile: fix broken lib link (#1625))
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8ba79adaf7 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 5251dcdc10 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7772b0ba15 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> ae81d49525 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c87c9f60da (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2ee29772c5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 7ab61fcb65 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 2458a1951e (Dockerfile: fix broken lib link (#1625))
>>>>>>> e39e7f602e (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
>>>>>>> 32d48f992d (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> efa58b1c30 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2c566ccf9d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 0daaa332d3 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a1ee3698d5 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
>>>>>>> 97f6c15849 (Fixes -Wclass-memaccess and -Wdeprecated-declaration warnings0)
=======
>>>>>>> 3979c9f967 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> decbe5b393 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 830e4400c0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 05c87d8d29 (Dockerfile: fix broken lib link (#1625))
>>>>>>> f8bd1aaad8 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> a3ae8c6790 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 03ab9cbc7f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1e47dd9d44 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> dc4ad92f5f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> d6e3a02d5b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> c70eab3a1d (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
=======
        raster/r.contour/testsuite/testrc.py
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> c540dfdbde (Dockerfile: fix broken lib link (#1625))
>>>>>>> 5ac978468c (Dockerfile: fix broken lib link (#1625))
>>>>>>> 42e7bdd0cf (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4dcb386cb0 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b0becb6826 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 751b93eb74 (Dockerfile: fix broken lib link (#1625))
>>>>>>> e630edf2f6 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 2f8632904c (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> c820dbdc0b (Dockerfile: fix broken lib link (#1625))
>>>>>>> ba46588e1c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6621d20c7f (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> da0a3f3c56 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 02677d4b9c (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4e319c2733 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 2e1ad6cb7b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 8c24ed3811 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 09d2c97e04 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 73cc5e30fa (Dockerfile: fix broken lib link (#1625))
>>>>>>> 4e55b69d96 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> d597f9a6d8 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 7de156f16b (Dockerfile: fix broken lib link (#1625))
>>>>>>> e494d37988 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 9087bcf6fe (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> b6e5194011 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 56f3d5a1bd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> b30eba7edb (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> d040029157 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 1d6ad40ebe (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 740bf772d6 (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> f70372cb5d (Dockerfile: fix broken lib link (#1625))
>>>>>>> 7b80a7eedd (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 30a903a5ae (Dockerfile: fix broken lib link (#1625))
>>>>>>> de3b023788 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 1109ae34ce (Dockerfile: fix broken lib link (#1625))
>>>>>>> ea2d110c6b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 67ed37bf9b (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 4d9eb9010a (Dockerfile: fix broken lib link (#1625))
>>>>>>> 3454fc4883 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 6286b6659a (Dockerfile: fix broken lib link (#1625))
=======
=======
>>>>>>> 6242fe69ba (Dockerfile: fix broken lib link (#1625))
>>>>>>> 52e6c1ff9f (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> 4d4ee1c6cc (Dockerfile: fix broken lib link (#1625))


Running tests and creating report
---------------------------------

Currently there is full support only for running all the tests in
the small (basic) version of GRASS GIS sample Location for North Carolina
(see `GRASS GIS sample data`).

.. _GRASS GIS sample data: https://grass.osgeo.org/download/sample-data


Example Bash script to run be used as a cron job
------------------------------------------------

.. code-block:: bash

    #!/bin/bash

    set -e  # fail fast

    REPORTS=".../testreports"
    GRASSSRC=".../grass-src"
    # here we suppose default compilation settings of GRASS and no make install
    GRASSBIN="$GRASSSRC/bin.../grass"
    GRASSDIST="$GRASSSRC/dist..."

    # necessary hardcoded GRASS paths
    GRASSDIST_PYTHON="$GRASSDIST/etc/python"
    GRASS_MULTI_RUNNER="$GRASSSRC/python/grass/gunittest/multirunner.py"
    GRASS_MULTI_REPORTER="$GRASSSRC/python/grass/gunittest/multireport.py"

    DATE_FLAGS="--utc +%Y-%m-%d-%H-%M"
    NOW=$(date $DATE_FLAGS)

    # contains last executed command stdout and stderr
    # here were rely on reports being absolute
    OUTPUT_LOGFILE="$REPORTS/output-$NOW.txt"

    # these are relative to REPORTS
    CURRENT_REPORT_BASENAME="reports_for_date-"
    FINAL_REPORT_DIR="summary_report"
    CURRENT_REPORTS_DIR="$CURRENT_REPORT_BASENAME$NOW"
    LOGFILE="$REPORTS/runs.log"

    GRASSDATA="/grassdata/tests-grassdata"

    echo "Nightly GRASS GIS test started: $NOW" >> $LOGFILE

    # compile current source code from scratch
    cd $GRASSSRC
    make distclean -j4
    git pull
    ./configure ...  # or a script containing all the flags
    make -j4

    # run tests for the current source code
    cd $REPORTS
    mkdir $CURRENT_REPORTS_DIR
    cd $CURRENT_REPORTS_DIR
    python $GRASS_MULTI_RUNNER \
        --grassbin $GRASSBIN \
        --grasssrc $GRASSSRC \
        --grassdata $GRASSDATA \
        --location nc_spm_08_grass7 --location-type nc \
        --location other_location --location-type other_type

    # create overall report of all so far executed tests
    # the script depends on GRASS but just Python part is enough
    export PYTHONPATH="$GRASSDIST_PYTHON:$PYTHONPATH"
    python $GRASS_MULTI_REPORTER --output $FINAL_REPORT_DIR \
        $CURRENT_REPORT_BASENAME*/*

    # although we cannot be sure the tests were executed was successfully
    # so publish or archive results
    rsync -rtvu --delete $REPORTS/ "/var/www/html/grassgistestreports"

    echo "Nightly ($NOW) GRASS GIS test finished: $(date $DATE_FLAGS)" >> $LOGFILE

A script similar to this one can be used as a cron job, on most Linux systems
using ``crontab -e`` and adding a line similar to the following one::

    0 4 * * 1 .../grasstests/test_grass_gis.sh

Which will perform the tests every Monday at 4:00 in the morning (local time).

Particular script and frequency depends on what you want to test and
how many resources you want to use.
