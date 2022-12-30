# MODULE:    Test of grass.benchmark
#
# AUTHOR(S): Vaclav Petras <wenzeslaus gmail com>
#
# PURPOSE:   Benchmarking for GRASS GIS modules
#
# COPYRIGHT: (C) 2021 Vaclav Petras, and by the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

"""Tests of grass.benchmark CLI"""

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
import sys
from pathlib import Path
from subprocess import DEVNULL

import grass
from grass.benchmark import (
    benchmark_nprocs,
    benchmark_resolutions,
    save_results_to_file,
)
<<<<<<< HEAD
=======
from pathlib import Path
from subprocess import DEVNULL

from grass.benchmark import benchmark_resolutions, save_results_to_file
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
import sys
from pathlib import Path
from subprocess import DEVNULL

import grass
from grass.benchmark import (
    benchmark_nprocs,
    benchmark_resolutions,
    save_results_to_file,
)
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
from grass.benchmark.app import main as benchmark_main
from grass.gunittest.case import TestCase
from grass.gunittest.main import test
from grass.pygrass.modules import Module


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
def remove_file(path):
    """Remove filename if exists"""
    if sys.version_info < (3, 8):
        try:
            Path(path).unlink()
        except FileNotFoundError:
            pass
    else:
        Path(path).unlink(missing_ok=True)


<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
class TestBenchmarkCLI(TestCase):
    """Tests that benchmarkin CLI works"""

    json_filename = "plot_test.json"
    png_filenames = [f"plot_test1_{i}.png" for i in range(4)]
    png_filenames.append("plot_test2.png")

    def tearDown(self):
        """Remove test files"""
        remove_file(self.json_filename)
        for filename in self.png_filenames:
            remove_file(filename)

    def test_plot_nprocs_workflow(self):
        """Test that plot nprocs workflow runs"""
        label = "Standard output"
        repeat = 4
        # The benchmark part has only Python API, not CLI.
        try:
            result = benchmark_nprocs(
                module=Module("r.univar", map="elevation", stdout_=DEVNULL, run_=False),
                label=label,
                repeat=repeat,
                max_nprocs=3,
            )
        except grass.exceptions.ParameterError:
            self.skipTest("r.univar without nprocs parameter")
        save_results_to_file([result], self.json_filename)

        metrics = ["time", "speedup", "efficiency"]
        benchmark_main(["plot", "nprocs", self.json_filename, self.png_filenames[0]])
        for png_fname, metric in zip(self.png_filenames[1:4], metrics):
            benchmark_main(
                ["plot", "nprocs", "--metric", metric, self.json_filename, png_fname]
            )
        for filename in self.png_filenames[:4]:
            self.assertTrue(Path(filename).is_file())

    def test_plot_cells_workflow(self):
        """Test that plot cells workflow runs"""
        label = "Standard output"
        repeat = 4
<<<<<<< HEAD
=======
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
class TestBenchmarkCLI(TestCase):
    """Tests that benchmarkin CLI works"""

    json_filename = "plot_test.json"
    png_filename1 = "plot_test1.png"
    png_filename2 = "plot_test2.png"

    def tearDown(self):
        """Remove test files"""
        remove_file(self.json_filename)
        remove_file(self.png_filename1)
        remove_file(self.png_filename2)

    def test_plot_nprocs_workflow(self):
        """Test that plot nprocs workflow runs"""
        label = "Standard output"
        repeat = 4
        # The benchmark part has only Python API, not CLI.
        try:
            result = benchmark_nprocs(
                module=Module("r.univar", map="elevation", stdout_=DEVNULL, run_=False),
                label=label,
                repeat=repeat,
                max_nprocs=3,
            )
        except grass.exceptions.ParameterError:
            self.skipTest("r.univar without nprocs parameter")
        save_results_to_file([result], self.json_filename)
        benchmark_main(["plot", "nprocs", self.json_filename, self.png_filename1])
        self.assertTrue(Path(self.png_filename1).is_file())

    def test_plot_cells_workflow(self):
        """Test that plot cells workflow runs"""
        label = "Standard output"
        repeat = 4
<<<<<<< HEAD
        json_filename = "plot_test.json"
        png_filename = "plot_test.png"
        png_filename_resolutions = "plot_test_resolutions.png"
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        # The benchmark part has only Python API, not CLI.
        result = benchmark_resolutions(
            module=Module("r.univar", map="elevation", stdout_=DEVNULL, run_=False),
            label=label,
            repeat=repeat,
            resolutions=[1000, 500],
        )
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
        save_results_to_file([result], self.json_filename)
        benchmark_main(["plot", "cells", self.json_filename, self.png_filenames[0]])
        self.assertTrue(Path(self.png_filenames[0]).is_file())
        benchmark_main(
            [
                "plot",
                "cells",
                "--resolutions",
                self.json_filename,
                self.png_filenames[-1],
            ]
        )
<<<<<<< HEAD
        self.assertTrue(Path(self.png_filenames[-1]).is_file())
=======
        self.assertTrue(Path(self.png_filename2).is_file())
<<<<<<< HEAD
=======
        save_results_to_file([result], json_filename)
        benchmark_main(["plot", "cells", json_filename, png_filename])
        self.assertTrue(Path(png_filename).is_file())
=======
        save_results_to_file([result], self.json_filename)
        benchmark_main(["plot", "cells", self.json_filename, self.png_filename1])
        self.assertTrue(Path(self.png_filename1).is_file())
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
        benchmark_main(
            ["plot", "cells", "--resolutions", self.json_filename, self.png_filename2]
        )
<<<<<<< HEAD
        self.assertTrue(Path(png_filename_resolutions).is_file())
>>>>>>> ba3c0640fa (libpython: Support benchmarks of non-parallel runs better (#1733))
<<<<<<< HEAD
>>>>>>> ea17e86303 (libpython: Support benchmarks of non-parallel runs better (#1733))
=======
=======
        self.assertTrue(Path(self.png_filename2).is_file())
>>>>>>> 953489b535 (wxGUI: fix layout flag assert in wms dialog (#1764))
<<<<<<< HEAD
>>>>>>> 9f045df12f (wxGUI: fix layout flag assert in wms dialog (#1764))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))


if __name__ == "__main__":
    test()
