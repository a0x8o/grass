set grass=%1
set python=%2

<<<<<<< HEAD
call %grass% --tmp-project XY --exec g.download.project url=https://grass.osgeo.org/sampledata/north_carolina/nc_spm_full_v2alpha2.tar.gz path=%USERPROFILE%
call %grass% --tmp-project XY --exec %python% -m grass.gunittest.main --grassdata %USERPROFILE% --location nc_spm_full_v2alpha2 --location-type nc --min-success 96 --config .github\workflows\osgeo4w_gunittest.cfg
=======
call %grass% --tmp-project XY --exec g.download.location url=https://grass.osgeo.org/sampledata/north_carolina/nc_spm_full_v2alpha2.tar.gz path=%USERPROFILE%
call %grass% --tmp-project XY --exec %python% -m grass.gunittest.main --grassdata %USERPROFILE% --location nc_spm_full_v2alpha2 --location-type nc --min-success 80
>>>>>>> 4c8d884044 (CI: replace --tmp-location with --tmp-project (#3825))
