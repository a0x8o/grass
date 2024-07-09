"""Test SeriesMap functions"""

from pathlib import Path

import pytest

import grass.jupyter as gj

IPython = pytest.importorskip("IPython", reason="IPython package not available")
ipywidgets = pytest.importorskip(
    "ipywidgets", reason="ipywidgets package not available"
)

<<<<<<< HEAD

=======
>>>>>>> a1d9455ddc (pytest: Mark tests using space_time_raster_dataset as needs_solo_run (#3939))
@pytest.mark.needs_solo_run
def test_default_init(space_time_raster_dataset):
    """Check that TimeSeriesMap init runs with default parameters"""
    img = gj.SeriesMap()
    img.add_rasters(space_time_raster_dataset.raster_names)
    assert img._labels == space_time_raster_dataset.raster_names


@pytest.mark.needs_solo_run
def test_render_layers(space_time_raster_dataset):
    """Check that layers are rendered"""
    # create instance of TimeSeriesMap
    img = gj.SeriesMap()
    # test adding base layer and d_legend here too for efficiency (rendering is
    # time-intensive)
    img.d_rast(map=space_time_raster_dataset.raster_names[0])
    img.add_rasters(space_time_raster_dataset.raster_names[1:])
    img.d_barscale()
    # Render layers
    img.render()
    # check files exist
    # We need to check values which are only in protected attributes
    # pylint: disable=protected-access
<<<<<<< HEAD
<<<<<<< HEAD
    for filename in img._base_filename_dict.values():
=======
    for unused_layer, filename in img._base_filename_dict.items():
>>>>>>> ab24029634 (grass.jupyter: Create BaseSeriesMap to remove redundancies in SeriesMap and TimeSeriesMap  (#3468))
=======
    for filename in img._base_filename_dict.values():
>>>>>>> 49624bb6eb (style: Fix incorrect-dict-iterator (PERF102) (#4007))
        assert Path(filename).is_file()


@pytest.mark.needs_solo_run
<<<<<<< HEAD
=======
@pytest.mark.skipif(IPython is None, reason="IPython package not available")
@pytest.mark.skipif(ipywidgets is None, reason="ipywidgets package not available")
>>>>>>> a1d9455ddc (pytest: Mark tests using space_time_raster_dataset as needs_solo_run (#3939))
def test_save(space_time_raster_dataset, tmp_path):
    """Test returns from animate and time_slider are correct object types"""
    img = gj.SeriesMap()
    img.add_rasters(space_time_raster_dataset.raster_names)
    gif_file = img.save(tmp_path / "image.gif")
    assert Path(gif_file).is_file()
