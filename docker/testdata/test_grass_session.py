<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
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
# Import GRASS GIS Python bindings (requires 8.4+) and test r.in.pdal

# PYTHONPATH=$(grass --config python-path) python
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
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> osgeo-main
# Import GRASS Python bindings
# https://github.com/zarch/grass-session
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
# pip install grass-session
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
# Import GRASS GIS Python bindings (requires 8.4+) and test r.in.pdal

# PYTHONPATH=$(grass --config python-path) python
>>>>>>> 9f7ecdc310 (docker: Use only native Python API, set only necessary variables (#3819))
=======
# Import GRASS GIS Python bindings (requires 8.4+) and test r.in.pdal

# PYTHONPATH=$(grass --config python-path) python
=======
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
>>>>>>> osgeo-main
# Import GRASS Python bindings
# https://github.com/zarch/grass-session
<<<<<<< HEAD
<<<<<<< HEAD
# pip install grass-session
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4ed9bfe3ea (Dockerfile: fix broken lib link (#1625))
=======
=======
# pip install grass-session
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
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
>>>>>>> osgeo-main
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e946d8e472 (Dockerfile: fix broken lib link (#1625))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
# Import GRASS Python bindings
# https://github.com/zarch/grass-session
<<<<<<< HEAD
<<<<<<< HEAD
# pip install grass-session
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 44b23be1c2 (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
>>>>>>> b4039859b5 (Dockerfile: fix broken lib link (#1625))
=======
<<<<<<< HEAD
# Import GRASS Python bindings
# https://github.com/zarch/grass-session
<<<<<<< HEAD
<<<<<<< HEAD
# pip install grass-session
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
<<<<<<< HEAD
>>>>>>> 461452897e (Dockerfile: fix broken lib link (#1625))
=======
=======
=======
>>>>>>> c875f035a5 (Dockerfile: fix broken lib link (#1625))
>>>>>>> 310f1e65b4 (Dockerfile: fix broken lib link (#1625))
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
# Import GRASS Python bindings
# https://github.com/zarch/grass-session
<<<<<<< HEAD
# pip install grass-session
=======
>>>>>>> 756514063b (Dockerfile: fix broken lib link (#1625))
>>>>>>> 92e9b42dca (Dockerfile: fix broken lib link (#1625))
>>>>>>> 705b9dfdcf (Dockerfile: fix broken lib link (#1625))

import grass.script as gs

# full path to new project
project = "/tmp/grasstest_epsg_25832"
gs.create_project(project, epsg="25832")

# hint: do not use ~ as an alias for HOME
with gs.setup.init(project):
    print("GRASS GIS session: tests for PROJ, GDAL, PDAL, GRASS GIS")
    print(gs.parse_command("g.gisenv", flags="s"))

    # simple test: just scan the LAZ file
    gs.run_command(
        "r.in.pdal",
        input="/tmp/simple.laz",
        output="count_1",
        method="n",
        flags="g",
        resolution=1,
        overwrite=True,
    )
