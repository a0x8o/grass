.. _GRASSdatabase-label:

GRASS database management
=========================

PyGRASS implements the classes described bellow:

* :class:`~pygrass.gis.Gisdbase`
* :class:`~pygrass.gis.Location`
* :class:`~pygrass.gis.Mapset`
* :class:`~pygrass.gis.VisibleMapset`

These classes are used to manage the infrastructure of GRASS database:
GIS data directory, Location and Mapset. Details about the GRASS GIS
database management (locations and mapsets) can be found in the `GRASS
GIS 7 User's Manual: GRASS GIS Quickstart
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<<<<<<< HEAD
<<<<<<< HEAD
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
>>>>>>> osgeo-main
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
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
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5af337c699 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 020d15913e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> da1bbb9bd2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 9f683ad6d3 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> eb0df723eb (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 8df9861e42 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 02c6694ef5 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> e14069d05d (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 73a1a8ce38 (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> ff58b46888 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 25682bb3d2 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> b4d79b4a7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 1a0ac2e468 (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 2535753a01 (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 7ae4f4de7e (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
<https://grass.osgeo.org/grass-devel/manuals/helptext.html>`_.
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 0a0b3c899e (Programmer's manual: update GRASS GIS arch drawing (#1610))
<<<<<<< HEAD
>>>>>>> 40aaffdfff (Programmer's manual: update GRASS GIS arch drawing (#1610))
=======
=======
=======
<https://grass.osgeo.org/grass80/manuals/helptext.html>`_.
>>>>>>> 227cbcebbf (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> 14b9d48f9a (Programmer's manual: update GRASS GIS arch drawing (#1610))
>>>>>>> aec07d6302 (Programmer's manual: update GRASS GIS arch drawing (#1610))

.. _Region-label:

Region management
=================

The :class:`~pygrass.gis.region.Region` class it is useful to obtain
information about the computational region and to change it. Details
about the GRASS GIS computational region management can be found in
the `GRASS GIS Wiki: Computational region
<https://grasswiki.osgeo.org/wiki/Computational_region>`_.

The classes are part of the :mod:`~pygrass.gis` module.
