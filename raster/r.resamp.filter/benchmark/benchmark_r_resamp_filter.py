"""Benchmarking of r.resamp.filter

@author Aaron Saw Min Sern
"""

from grass.exceptions import CalledModuleError
from grass.pygrass.modules import Module
from subprocess import DEVNULL

import grass.benchmark as bm


def main():
    results = []

    # Users can add more or modify existing reference maps
    benchmark(7071, "r.resamp.filter_50M", results)
    benchmark(10000, "r.resamp.filter_100M", results)
    benchmark(14142, "r.resamp.filter_200M", results)
    benchmark(20000, "r.resamp.filter_400M", results)

    bm.nprocs_plot(results, filename="benchmark.svg")


def benchmark(size, label, results):
    reference = "r_resamp_filter_reference_map"
    output = "benchmark_r_resamp_filter_nprocs"

    generate_map(rows=size, cols=size, fname=reference)
    Module("g.region", flags="pa", s=0, n=size, w=0, e=size, res=1)
    module = Module(
        "r.resamp.filter",
        input=reference,
        filter=["gauss", "box"],
        output=output,
        radius=[6, 9],
        memory=500,
        run_=False,
        stdout_=DEVNULL,
        overwrite=True,
    )
    results.append(bm.benchmark_nprocs(module, label=label, max_nprocs=8, repeat=3))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
    Module("g.remove", quiet=True, flags="f", type="raster", name=(reference, output))
=======
    Module("g.remove", quiet=True, flags="f", type="raster", name=reference)
    Module("g.remove", quiet=True, flags="f", type="raster", name=output)
>>>>>>> 021dfb5d52 (r.terrafow: explicit use of default constructors (#2660))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))
=======
    Module("g.remove", quiet=True, flags="f", type="raster", name=reference)
    Module("g.remove", quiet=True, flags="f", type="raster", name=output)
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
=======
>>>>>>> cd1e658f47 (r.terrafow: explicit use of default constructors (#2660))
=======
>>>>>>> a5b4144f59 (r.horizon manual - fix typo (#2794))


def generate_map(rows, cols, fname):
    Module("g.region", flags="pa", s=0, n=rows, w=0, e=cols, res=3)
    # Generate using r.random.surface if r.surf.fractal fails
    try:
        print("Generating reference map using r.surf.fractal...")
        Module("r.surf.fractal", output=fname)
    except CalledModuleError:
        print("r.surf.fractal fails, using r.random.surface instead...")
        Module("r.random.surface", output=fname)


if __name__ == "__main__":
    main()
