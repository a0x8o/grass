#
# AUTHOR(S): Caitlin Haedrich <caitlin DOT haedrich AT gmail>
#
# PURPOSE:   This module contains functions for interactive display
#            in Jupyter Notebooks.
#
# COPYRIGHT: (C) 2021 Caitlin Haedrich, and by the GRASS Development Team
#
<<<<<<< HEAD
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.

import os
import sys
import tempfile
import weakref
from pathlib import Path
import grass.script as gs
from .display import GrassRenderer
from .utils import (
    estimate_resolution,
    get_location_proj_string,
    get_region,
    reproject_region,
    setup_location,
)


class InteractiveMap:
    """This class creates interative GRASS maps with folium.

    Basic Usage:
    >>> m = InteractiveMap()
    >>> m.add_vector("streams")
    >>> m.add_raster("elevation")
    >>> m.add_layer_control()
    >>> m.show()
    """

    def __init__(self, width=400, height=400):
        """Creates a blank folium map centered on g.region.

        :param int height: height in pixels of figure (default 400)
        :param int width: width in pixels of figure (default 400)
        """

        import folium

        self._folium = folium
=======
#            This program is free software under the GNU Gernal Public
#            License (>=v2). Read teh file COPYING that comes with GRASS
#            for details.

import os
from pathlib import Path

import folium

import grass.script as gs


class InteractiveMap:
    """This class creates interative GRASS maps with folium"""

    def __init__(self, width=400, height=400):
        """This initiates a folium map centered on g.region.

        Keyword arguments:
            height -- height in pixels of figure (default 400)
            width -- width in pixels of figure (default 400)"""
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))

        # Store height and width
        self.width = width
        self.height = height
        # Make temporary folder for all our files
<<<<<<< HEAD
        self._tmp_dir = tempfile.TemporaryDirectory()

        # Remember original environment; all environments used
        # in this class are derived from this one
        self._src_env = os.environ.copy()

        # Set up temporary locations  in WGS84 and Pseudo-Mercator
        # We need two because folium uses WGS84 for vectors and coordinates
        # and Pseudo-Mercator for raster overlays
        self.rcfile_psmerc, self._psmerc_env = setup_location(
            "psmerc", self._tmp_dir.name, "3857", self._src_env
        )
        self.rcfile_wgs84, self._wgs84_env = setup_location(
            "wgs84", self._tmp_dir.name, "4326", self._src_env
        )

        # Get Center of temporary GRASS regions
        center = gs.parse_command("g.region", flags="cg", env=self._wgs84_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))

        # Create Folium Map
        self.map = self._folium.Map(
=======
        self.tmp_dir = Path("./tmp/")
        try:
            os.mkdir(self.tmp_dir)
        except FileExistsError:
            pass
        # Create new environment for tmp WGS84 location
        rcfile, self._vector_env = gs.create_environment(
            self.tmp_dir, "temp_folium_WGS84", "PERMANENT"
        )
        # Location and mapset and region
        gs.create_location(
            self.tmp_dir, "temp_folium_WGS84", epsg="4326", overwrite=True
        )
        self._extent = self._convert_extent(
            env=os.environ
        )  # Get the extent of the original area in WGS84
        # Set region to match original region extent
        gs.run_command(
            "g.region",
            n=self._extent["north"],
            s=self._extent["south"],
            e=self._extent["east"],
            w=self._extent["west"],
            env=self._vector_env,
        )
        # Get Center of tmp GRASS region
        center = gs.parse_command("g.region", flags="cg", env=self._vector_env)
        center = (float(center["center_northing"]), float(center["center_easting"]))
        # Create Folium Map
        self.map = folium.Map(
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
            width=self.width,
            height=self.height,
            location=center,
            tiles="cartodbpositron",
        )
<<<<<<< HEAD
        # Set LayerControl default
        self.layer_control = False

        # Cleanup rcfiles with finalizer
        def remove_if_exists(path):
            if sys.version_info < (3, 8):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    pass
            else:
                path.unlink(missing_ok=True)

        def clean_up(paths):
            for path in paths:
                remove_if_exists(path)

        self._finalizer = weakref.finalize(
            self, clean_up, [Path(self.rcfile_psmerc), Path(self.rcfile_wgs84)]
        )
=======
        # Create LayerControl default
        self.layer_control = False

    def _convert_coordinates(self, x, y, proj_in):
        """This function reprojects coordinates to WGS84, the required
        projection for vectors in folium.

        Arguments:
            x -- x coordinate (string)
            y -- y coordinate (string)
            proj_in -- proj4 string of location (for example, the output
            of g.region run with the `g` flag."""

        # Reformat input
        coordinates = f"{x}, {y}"
        # Reproject coordinates
        coords_folium = gs.read_command(
            "m.proj",
            coordinates=coordinates,
            proj_in=proj_in,
            separator="comma",
            flags="do",
        )
        # Reformat from string to array
        coords_folium = coords_folium.strip()  # Remove '\n' at end of string
        coords_folium = coords_folium.split(",")  # Split on comma
        coords_folium = [float(value) for value in coords_folium]  # Convert to floats
        return coords_folium[1], coords_folium[0]  # Return Lat and Lon

    def _convert_extent(self, env=None):
        """This function returns the bounding box of the current region
        in WGS84, the required projection for folium"""

        # Get proj of current GRASS region
        proj = gs.read_command("g.proj", flags="jf", env=env)
        # Get extent
        extent = gs.parse_command("g.region", flags="g", env=env)
        # Convert extent to EPSG:3857, required projection for Folium
        north, east = self._convert_coordinates(extent["e"], extent["n"], proj)
        south, west = self._convert_coordinates(extent["w"], extent["s"], proj)
        extent = {"north": north, "south": south, "east": east, "west": west}
        return extent

    def _folium_bounding_box(self, extent):
        """Reformats extent into bounding box to pass to folium"""
        return [[extent["north"], extent["west"]], [extent["south"], extent["east"]]]
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))

    def add_vector(self, name):
        """Imports vector into temporary WGS84 location,
        re-formats to a GeoJSON and adds to folium map.

<<<<<<< HEAD
        :param str name: name of vector to be added to map;
                         positional-only parameter
        """
=======
        Arguments:
            name -- a positional-only parameter; name of vector to be added
            to map as a string"""
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))

        # Find full name of vector
        file_info = gs.find_file(name, element="vector")
        full_name = file_info["fullname"]
        name = file_info["name"]
<<<<<<< HEAD
        mapset = file_info["mapset"]
        new_name = full_name.replace("@", "_")
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=self._src_env)
        gs.run_command(
            "v.proj",
            input=name,
            output=new_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._wgs84_env,
        )
        # Convert to GeoJSON
        json_file = Path(self._tmp_dir.name) / f"{new_name}.json"
        gs.run_command(
            "v.out.ogr",
            input=new_name,
            output=json_file,
            format="GeoJSON",
            env=self._wgs84_env,
        )
        # Import GeoJSON to folium and add to map
        self._folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_raster(self, name, opacity=0.8):
        """Imports raster into temporary WGS84 location,
        exports as png and overlays on folium map

        :param str name: name of raster to add to display; positional-only parameter
        :param float opacity: raster opacity, number between
                              0 (transparent) and 1 (opaque)
        """

        # Find full name of raster
        file_info = gs.find_file(name, element="cell", env=self._src_env)
        full_name = file_info["fullname"]
        name = file_info["name"]
        mapset = file_info["mapset"]

        # Reproject raster into WGS84/epsg3857 location
        env_info = gs.gisenv(env=self._src_env)
        resolution = estimate_resolution(
            raster=name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._psmerc_env,
        )
        tgt_name = full_name.replace("@", "_")
        gs.run_command(
            "r.proj",
            input=full_name,
            output=tgt_name,
            mapset=mapset,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            resolution=resolution,
            env=self._psmerc_env,
        )
        # Write raster to png file with GrassRenderer
        region_info = gs.region(env=self._src_env)
        png_width = region_info["cols"]
        png_height = region_info["rows"]
        filename = os.path.join(self._tmp_dir.name, f"{tgt_name}.png")
        m = GrassRenderer(
            width=png_width,
            height=png_height,
            env=self._psmerc_env,
            filename=filename,
        )
        m.run("d.rast", map=tgt_name)

        # Reproject bounds of raster for overlaying png
        # Bounds need to be in WGS84
        old_bounds = get_region(self._src_env)
        from_proj = get_location_proj_string(env=self._src_env)
        to_proj = get_location_proj_string(env=self._wgs84_env)
        bounds = reproject_region(old_bounds, from_proj, to_proj)
        new_bounds = [
            [bounds["north"], bounds["west"]],
            [bounds["south"], bounds["east"]],
        ]

        # Overlay image on folium map
        img = self._folium.raster_layers.ImageOverlay(
            image=filename,
            name=name,
            bounds=new_bounds,
            opacity=opacity,
            interactive=True,
            cross_origin=False,
        )
        # Add image to map
        img.add_to(self.map)

    def add_layer_control(self, **kwargs):
        """Add layer control to display"""
        self.layer_control = True
        self.layer_control_object = self._folium.LayerControl(**kwargs)

    def show(self):
        """This function returns a folium figure object with a GRASS raster
=======
        # Reproject vector into WGS84 Location
        env_info = gs.gisenv(env=os.environ)
        gs.run_command(
            "v.proj",
            input=full_name,
            location=env_info["LOCATION_NAME"],
            dbase=env_info["GISDBASE"],
            env=self._vector_env,
        )
        # Convert to GeoJSON
        json_file = self.tmp_dir / f"tmp_{name}.json"
        gs.run_command(
            "v.out.ogr",
            input=name,
            output=json_file,
            format="GeoJSON",
            env=self._vector_env,
        )
        # Import GeoJSON to folium and add to map
        folium.GeoJson(str(json_file), name=name).add_to(self.map)

    def add_layer_control(self, **kwargs):
        self.layer_control = True
        self.layer_control_object = folium.LayerControl(**kwargs)

    def show(self):
        """This function creates a folium map with a GRASS raster
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
        overlayed on a basemap.

        If map has layer control enabled, additional layers cannot be
        added after calling show()."""

        if self.layer_control:
            self.map.add_child(self.layer_control_object)
        # Create Figure
<<<<<<< HEAD
        fig = self._folium.Figure(width=self.width, height=self.height)
=======
        fig = folium.Figure(width=self.width, height=self.height)
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
        # Add map to figure
        fig.add_child(self.map)

        return fig
<<<<<<< HEAD

    def save(self, filename):
        """Save map as an html map.

        :param str filename: name of html file
        """
        self.map.save(filename)
=======
>>>>>>> 01a506d3d3 (libpython: Support benchmarks of non-parallel runs better (#1733))
