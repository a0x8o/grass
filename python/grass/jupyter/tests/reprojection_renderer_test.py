"""Test ReprojectionRenderer functions"""

from pathlib import Path
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
import pytest
=======
from pytest import approx
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
from pytest import approx
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
=======
from pytest import approx
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
from grass.jupyter.reprojection_renderer import ReprojectionRenderer


# check get_bbox
def test_get_bbox(simple_dataset):
    """Test that get_bbox returns correct bounding box"""
    renderer = ReprojectionRenderer()
    bbox = renderer.get_bbox()
    assert bbox == [[90, 180], [-90, -180]]


# render_raster produces filename and new_bounds
def test_render_raster(simple_dataset):
    """Check render_raster returns image and bbox"""
    renderer = ReprojectionRenderer()
    filename, bbox = renderer.render_raster(simple_dataset.raster_name)
    assert Path(filename).exists()
    # Test bounding box is correct
    # Raster is same extent as region so no need to test bbox for use_region=True
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
    assert bbox[0] == pytest.approx([0.00072155, -85.48874388])
    assert bbox[1] == pytest.approx([0.00000000, -85.48766880])
=======
    assert bbox[0] == approx([0.00072155, -85.48874388])
    assert bbox[1] == approx([0.00000000, -85.48766880])
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))
=======
    assert bbox[0] == approx([0.00072155, -85.48874388])
    assert bbox[1] == approx([0.00000000, -85.48766880])
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
=======
>>>>>>> 3ac340cfe2 (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 4217d7b0d6 (wxpyimgview: explicit conversion to int (#2704))


# render_vector produces json
def test_render_vector(simple_dataset):
    """Check render_vector returns file"""
    renderer = ReprojectionRenderer()
    filename = renderer.render_vector(simple_dataset.vector_name)
    assert Path(filename).exists()
