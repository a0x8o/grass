# GRASS GIS docker
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f130b43e6c (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))

## GRASS GIS docker matrix
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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

## GRASS GIS docker matrix
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
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
=======
>>>>>>> osgeo-main
=======
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
<<<<<<< HEAD
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))

[![Docker Pulls](https://img.shields.io/docker/pulls/osgeo/grass-gis.svg)](https://grass.osgeo.org/download/docker/)

Find out included version of GDAL, GEOS, PROJ, PDAL, Python and GRASS GIS using

```bash
grass --tmp-project XY --exec g.version -rge \
    && pdal --version \
    && python3 --version
```

## Requirements

* docker or podman

## Installation

To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):

=======

<<<<<<< HEAD
## GRASS GIS docker matrix
=======
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

<<<<<<< HEAD
<<<<<<< HEAD
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml> and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
=======
Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))

## Requirements

* docker or podman

## Installation

<<<<<<< HEAD
<<<<<<< HEAD
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
```bash
docker pull osgeo/grass-gis:<tag>
```

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

<<<<<<< HEAD
<<<<<<< HEAD
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml> and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
=======
Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

<<<<<<< HEAD
<<<<<<< HEAD
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml> and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
=======
Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
>>>>>>> 446049deb7 (r.horizon manual - fix typo (#2794))
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

<<<<<<< HEAD
<<<<<<< HEAD
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml> and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
=======
Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
>>>>>>> 7dcf663571 (r.horizon manual - fix typo (#2794))
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

<<<<<<< HEAD
<<<<<<< HEAD
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml> and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
=======
Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
>>>>>>> fac93d230e (r.horizon manual - fix typo (#2794))
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))

## Requirements

* docker or podman

## Installation

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======

## GRASS GIS docker matrix
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

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
=======
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

| Base image   | Docker tag      | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|-----------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 20.04 | latest-ubuntu   | 8.3.dev    | 6.3.1 | 3.0.4 | 2.2.0 | 3.8.10 | 1.20 GB    |
| Debian 10.1  | latest-debian   | 8.3.dev    | 5.2.0 | 2.4.0 | 1.8.0 | 3.7.3  | 1.16 GB    |
| Alpine 3.12  | latest-alpine   | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|-----------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 20.04 | stable-ubuntu   | 8.2 branch | 6.3.1 | 3.0.4 | 2.2.0 | 3.8.10 | 1.20 GB    |
| Debian 10.1  | stable-debian   | 8.2 branch | 5.2.0 | 2.4.0 | 1.8.0 | 3.7.3  | 1.16 GB    |
| Alpine 3.12  | stable-alpine   | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |

Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml> and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
=======
| Ubuntu 20.04 | latest-ubuntu | 8.3.dev    | 6.3.1 | 3.0.4 | 2.2.0 | 3.8.10 | 1.20 GB    |
| Debian 10.1  | latest-debian | 8.3.dev    | 5.2.0 | 2.4.0 | 1.8.0 | 3.7.3  | 1.16 GB    |
=======
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
>>>>>>> 08401a0a3a (r.horizon manual - fix typo (#2794))
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))
=======
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
=======
| Ubuntu 20.04 | latest-ubuntu | 8.3.dev    | 6.3.1 | 3.0.4 | 2.2.0 | 3.8.10 | 1.20 GB    |
| Debian 10.1  | latest-debian | 8.3.dev    | 5.2.0 | 2.4.0 | 1.8.0 | 3.7.3  | 1.16 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 20.04 | stable-ubuntu | 8.2 branch | 6.3.1 | 3.0.4 | 2.2.0 | 3.8.10 | 1.20 GB    |
| Debian 10.1  | stable-debian | 8.2 branch | 5.2.0 | 2.4.0 | 1.8.0 | 3.7.3  | 1.16 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))
=======
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
=======
| Ubuntu 20.04 | latest-ubuntu | 8.3.dev    | 6.3.1 | 3.0.4 | 2.2.0 | 3.8.10 | 1.20 GB    |
| Debian 10.1  | latest-debian | 8.3.dev    | 5.2.0 | 2.4.0 | 1.8.0 | 3.7.3  | 1.16 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 20.04 | stable-ubuntu | 8.2 branch | 6.3.1 | 3.0.4 | 2.2.0 | 3.8.10 | 1.20 GB    |
| Debian 10.1  | stable-debian | 8.2 branch | 5.2.0 | 2.4.0 | 1.8.0 | 3.7.3  | 1.16 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))
=======
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
| Ubuntu 20.04 | latest-ubuntu | 8.3.dev    | 6.3.1 | 3.0.4 | 2.2.0 | 3.8.10 | 1.20 GB    |
| Debian 10.1  | latest-debian | 8.3.dev    | 5.2.0 | 2.4.0 | 1.8.0 | 3.7.3  | 1.16 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 20.04 | stable-ubuntu | 8.2 branch | 6.3.1 | 3.0.4 | 2.2.0 | 3.8.10 | 1.20 GB    |
| Debian 10.1  | stable-debian | 8.2 branch | 5.2.0 | 2.4.0 | 1.8.0 | 3.7.3  | 1.16 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 27 Apr 2022 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))

## Requirements

* docker or podman

## Installation

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
=======

=======

>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
## GRASS GIS docker matrix

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)

## Requirements

* docker or podman

## Installation
<<<<<<< HEAD
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> main
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from the table above):
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))

>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
>>>>>>> 171e3bec7d (Fix missing function prototypes (#2727))
=======
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> 498a331298 (Fix missing function prototypes (#2727))

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======

>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
=======
=======

>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
=======
=======

>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
## GRASS GIS docker matrix

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)

## Requirements

* docker or podman

## Installation

To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):

<<<<<<< HEAD
>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from the table above):
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> 488180fefd (Fix missing function prototypes (#2727))

>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ebf041644a (r.horizon manual - fix typo (#2794))
=======
<<<<<<< HEAD
To install a docker image, run (replace `<tag>` with the desired Docker tag from the table above):
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> fce97d24c8 (Fix missing function prototypes (#2727))

>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dd6a87c0fa (r.horizon manual - fix typo (#2794))
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
To install a docker image, run (replace `<tag>` with the desired Docker tag from the table above):
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> 38fb0d903f (Fix missing function prototypes (#2727))

>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5ce081f790 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> osgeo-main
=======
>>>>>>> osgeo-main
=======
=======
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
<<<<<<< HEAD
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from the table above):
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> 68ce655dce (Fix missing function prototypes (#2727))

>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 5d3bd35e0a (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> a56a27343d (r.horizon manual - fix typo (#2794))
=======
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from the table above):
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> 43e21bab04 (Fix missing function prototypes (#2727))

>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 33ce576706 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 838760f612 (r.horizon manual - fix typo (#2794))
=======
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from the table above):
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> 95125e7509 (Fix missing function prototypes (#2727))

>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 17e5fe5619 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 3de174a63e (r.horizon manual - fix typo (#2794))
=======
=======
>>>>>>> osgeo-main
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from the table above):
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))

>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
=======

## GRASS GIS docker matrix

[![Docker Pulls](https://img.shields.io/docker/pulls/mundialis/grass-py3-pdal.svg)](https://grass.osgeo.org/download/software/docker-images/)

<!-- markdownlint-disable line-length -->
| Base image   | Docker tag    | GRASS GIS  | PROJ  | GDAL  | PDAL  | Python | Image size |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | latest-ubuntu | 8.3.dev    | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | latest-debian | 8.3.dev    | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | latest-alpine | 8.3.dev    | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
|--------------|---------------|------------|-------|-------|-------|--------|------------|
| Ubuntu 22.04 | stable-ubuntu | 8.2 branch | 8.2.1 | 3.4.1 | 2.4.3 | 3.10.6 | 2.89 GB    |
| Debian 11    | stable-debian | 8.2 branch | 7.2.1 | 3.2.2 | 2.4.3 | 3.9.2  | 2.93 GB    |
| Alpine 3.12  | stable-alpine | 8.2 branch | 7.0.1 | 3.1.4 | 2.1.0 | 3.8.10 |  186 MB    |
<!-- markdownlint-enable line-length -->

Last update: 22 Jan 2023 (source: <https://github.com/OSGeo/grass/actions/workflows/docker.yml>
and <https://hub.docker.com/r/mundialis/grass-py3-pdal/tags>)

## Requirements

* docker or podman

## Installation

To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):

>>>>>>> 7409ab6716 (r.horizon manual - fix typo (#2794))
>>>>>>> 8a70512c8d (r.horizon manual - fix typo (#2794))
>>>>>>> 7320e7f073 (r.horizon manual - fix typo (#2794))
<<<<<<< HEAD
>>>>>>> 61b5b5fabe (r.horizon manual - fix typo (#2794))
=======
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from the table above):
=======
To install a docker image, run (replace `<tag>` with the desired Docker tag from
the table above):
>>>>>>> 6b0657b022 (Fix missing function prototypes (#2727))

>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
```bash
docker pull mundialis/grass-py3-pdal:<tag>
```

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
<<<<<<< HEAD
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6f30700108 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 8f5c741ca6 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 17e44a46cf (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b49c22396f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
>>>>>>> main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> fb687ccc49 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5788bd15e5 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> osgeo-main
=======
=======
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 68f959884d (Merge branch 'a0x8o' into stag0)
=======
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 25c9f12c84 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 5c730e3bfc (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> dacd5d901f (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 67fc38245a (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 456d653ebc (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 196338e256 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 5e648d6847 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 49258e3437 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> ca7763cb8e (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 12b43eb397 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 71a0ea5620 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 3ab4f90615 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> b784fde58b (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> osgeo-main
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 04de8c7cca (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 88f82c3773 (wxpyimgview: explicit conversion to int (#2704))
=======
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> b7a4108a2f (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 51acb188cd (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> ebc6d3f683 (wxpyimgview: explicit conversion to int (#2704))
<<<<<<< HEAD
>>>>>>> 268b04129d (wxpyimgview: explicit conversion to int (#2704))
=======
=======
>>>>>>> 6cf60c76a4 (wxpyimgview: explicit conversion to int (#2704))
=======
>>>>>>> 8422103f4c (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> a2d9fb4362 (wxpyimgview: explicit conversion to int (#2704))
>>>>>>> 6fc66d242f (wxpyimgview: explicit conversion to int (#2704))
See also: <https://grass.osgeo.org/download/docker/>
