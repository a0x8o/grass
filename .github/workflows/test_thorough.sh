#!/usr/bin/env bash

# fail on non-zero return code from a subprocess
set -e

grass --tmp-project XY --exec \
<<<<<<< HEAD
    g.download.project url=https://grass.osgeo.org/sampledata/north_carolina/nc_spm_full_v2alpha2.tar.gz path=$HOME
=======
    g.download.location url=https://grass.osgeo.org/sampledata/north_carolina/nc_spm_full_v2alpha2.tar.gz path=$HOME
>>>>>>> 4c8d884044 (CI: replace --tmp-location with --tmp-project (#3825))

grass --tmp-project XY --exec \
    python3 -m grass.gunittest.main \
    --grassdata $HOME --location nc_spm_full_v2alpha2 --location-type nc \
    --min-success 100 $@
